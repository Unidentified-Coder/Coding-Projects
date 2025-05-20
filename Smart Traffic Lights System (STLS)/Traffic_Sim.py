import random
import time
import threading
import pygame
import sys
from Vehicle_Detection import image_uploader, vehicle_counter

# Global variables used later in classes/functions

# Default timer values
defaultGreen = {0: 10, 1: 10, 2: 10, 3: 10}
defaultRed = 150
defaultYellow = 2

signals = []
noOfSignals = 4

# Paired signals setup:
# Original mapping: 0: right, 1: down, 2: left, 3: up
# We group:
#   Pair 0 (east–west): right (index 0) and left (index 2)
#   Pair 1 (north–south): down (index 1) and up (index 3)
pairMapping = {
    0: [0, 2], 
    1: [1, 3]
}
activePair = 0  # start with east–west active

# Global phase for the active pair. For vehicles in the active directions, this tells them if the light is green or yellow.
# (For inactive directions, the phase is always "red".)
currentPhase = "green"  # will be updated within the signal cycle

# Direction mapping used in vehicles
directionNumbers = {0: 'right', 1: 'down', 2: 'left', 3: 'up'}

# Vehicle speeds and starting coordinates
speeds = {'car': 2, 'bus': 1.8, 'truck': 1.8, 'bike': 2.5}
x = {
    'right': [0, 0, 0],
    'down': [755, 727, 697],
    'left': [1400, 1400, 1400],
    'up': [602, 627, 657]
}    
y = {
    'right': [348, 370, 398],
    'down': [0, 0, 0],
    'left': [498, 466, 436],
    'up': [800, 800, 800]
}

vehicles = {
    'right': {0: [], 1: [], 2: []},
    'down':  {0: [], 1: [], 2: []},
    'left':  {0: [], 1: [], 2: []},
    'up':    {0: [], 1: [], 2: []}
}
vehicleTypes ={0: 'car', 1: 'bus', 2: 'truck', 3: 'bike'}

# Coordinates for signals on screen
signalCoods = [(530,230), (810,230), (810,570), (530,570)]
signalTimerCoods = [(530,210), (810,210), (810,550), (530,550)]

# Stop lines (the line vehicles must not cross in red/yellow)
stopLines = {
    'right': 590,  
    'down':  330,  
    'left':  800,  
    'up':    535   
}

# Gap values are in pixels
stoppingGap = 15    # gap when vehicles are stopped
movingGap = 15      # the gap between vehicles 

# Opens the simulation as a separate window
pygame.init()
simulation = pygame.sprite.Group()

# Class used for controlling Lights
class TrafficSignal:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""
# Class for vehicle behavior (Such as Stopping distance, Distance at standstill traffic etc)
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, lane, vehicleClass, direction_number, direction):
        pygame.sprite.Sprite.__init__(self)
        self.lane = lane
        self.vehicleClass = vehicleClass
        self.speed = speeds[vehicleClass]
        self.direction_number = direction_number
        self.direction = direction
        # The spawn coordinate for this vehicle
        self.x = x[direction][lane]
        self.y = y[direction][lane]
        # crossed variable if vehicle has passed the stop line (pixels) it will be 1 otherwise 0
        self.crossed = 0  
        # append self to the appropriate lane for gap checking.
        vehicles[direction][lane].append(self)
        self.index = len(vehicles[direction][lane]) - 1  # position in lanes (2 lanes for each set of lights)
        path = "images/" + direction + "/" + vehicleClass + ".png"
        self.image = pygame.image.load(path)
        
        # adjust spawn positions slightly so vehicles do not overlap.
        if direction == 'right':
            delta = self.image.get_rect().width + stoppingGap
            x[direction][lane] -= delta
        elif direction == 'left':
            delta = self.image.get_rect().width + stoppingGap
            x[direction][lane] += delta
        elif direction == 'down':
            delta = self.image.get_rect().height + stoppingGap
            y[direction][lane] -= delta
        elif direction == 'up':
            delta = self.image.get_rect().height + stoppingGap
            y[direction][lane] += delta
            
        simulation.add(self)
    # Allows vehicles to be drawn on simulation
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def safe_to_move(self):
        if self.index == 0:
            return self.speed  # if no vehicle is infront return to assigned speed
        
        prev = vehicles[self.direction][self.lane][self.index - 1]
        if self.direction in ['right', 'left']:
            my_width = self.image.get_width()
            prev_width = prev.image.get_width()
            if self.direction == 'right':
                max_pos = prev.x - movingGap - my_width
                return max(0, min(self.speed, max_pos - self.x))
            else:  # left
                max_pos = prev.x + prev_width + movingGap
                return max(0, min(self.speed, self.x - max_pos))
        else:
            my_height = self.image.get_height()
            prev_height = prev.image.get_height()
            if self.direction == 'down':
                max_pos = prev.y - movingGap - my_height
                return max(0, min(self.speed, max_pos - self.y))
            else:  # up
                max_pos = prev.y + prev_height + movingGap
                return max(0, min(self.speed, self.y - max_pos))

    # determine vehicles movement behavior dependant on the light  
    def move(self):
        global currentPhase
        activeDirections = [directionNumbers[idx] for idx in pairMapping[activePair]]
        phase = currentPhase if self.direction in activeDirections else "red"

        speed_to_use = self.safe_to_move()

        if self.crossed == 0:
            if phase == "green":
                self.advance(speed_to_use)
                if self.direction == 'right' and self.x + self.image.get_width() >= stopLines['right']:
                    self.crossed = 1
                elif self.direction == 'down' and self.y + self.image.get_height() >= stopLines['down']:
                    self.crossed = 1
                elif self.direction == 'left' and self.x <= stopLines['left']:
                    self.crossed = 1
                elif self.direction == 'up' and self.y <= stopLines['up']:
                    self.crossed = 1
            else:
                # if the light is red/yellow then proceed to stop at the stop line  
                if self.direction == 'right' and self.x + self.image.get_width() < stopLines['right']:
                    self.advance(speed_to_use)
                    if self.x + self.image.get_width() > stopLines['right']:
                        self.x = stopLines['right'] - self.image.get_width()
                elif self.direction == 'down' and self.y + self.image.get_height() < stopLines['down']:
                    self.advance(speed_to_use)
                    if self.y + self.image.get_height() > stopLines['down']:
                        self.y = stopLines['down'] - self.image.get_height()
                elif self.direction == 'left' and self.x > stopLines['left']:
                    self.advance(speed_to_use)
                    if self.x < stopLines['left']:
                        self.x = stopLines['left']
                elif self.direction == 'up' and self.y > stopLines['up']:
                    self.advance(speed_to_use)
                    if self.y < stopLines['up']:
                        self.y = stopLines['up']
        else:
            # Already crossed — keep going
            self.advance(speed_to_use)

    # vehicle movement directions
    def advance(self, speed):
        if self.direction == 'right':
            self.x += speed
        elif self.direction == 'down':
            self.y += speed
        elif self.direction == 'left':
            self.x -= speed
        elif self.direction == 'up':
            self.y -= speed

def initializeSignals():
    # Create signals in order: index 0: right, 1: down, 2: left, 3: up.
    ts0 = TrafficSignal(0, defaultYellow, defaultGreen[0])   # right
    signals.append(ts0)
    ts1 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[1])  # down
    signals.append(ts1)
    ts2 = TrafficSignal(0, defaultYellow, defaultGreen[2])   # left
    signals.append(ts2)
    ts3 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[3])  # up
    signals.append(ts3)
    # Start the signal cycle in a separate thread.
    threading.Thread(target=repeat, daemon=True).start()

def repeat():
    global activePair, currentPhase

    # Count waiting vehicles in the active directions (not crossed yet)
    def count_waiting_vehicles(directions):
        count = 0
        for direction in directions:
            for lane in vehicles[direction]:
                for v in vehicles[direction][lane]:
                    if v.crossed == 0:
                        count += 1
        return count

    # Get the active and inactive directions
    activeDirections = [directionNumbers[idx] for idx in pairMapping[activePair]]
    inactivePair = 1 - activePair

    # Count vehicles and compute green time (minimum 5 sec, +1 per 2 vehicles)
    waitingVehicles = count_waiting_vehicles(activeDirections)
    greenTime = max(5, 5 + waitingVehicles // 2)  

    # Assign signal times
    for idx in pairMapping[activePair]:
        signals[idx].green = greenTime
        signals[idx].yellow = defaultYellow
        signals[idx].red = 0

    for idx in pairMapping[inactivePair]:
        signals[idx].red = defaultRed
        signals[idx].green = 0
        signals[idx].yellow = 0

    # Green phase
    currentPhase = "green"
    t = greenTime
    while t > 0:
        for idx in pairMapping[activePair]:
            signals[idx].green = t
        time.sleep(1)
        t -= 1

    # Yellow phase
    currentPhase = "yellow"
    t = defaultYellow
    for idx in pairMapping[activePair]:
        signals[idx].yellow = t
        signals[idx].green = 0
    while t > 0:
        for idx in pairMapping[activePair]:
            signals[idx].yellow = t
        time.sleep(1)
        t -= 1

    # End of active phase: reset to default
    for idx in pairMapping[activePair]:
        signals[idx].red = defaultRed
        signals[idx].green = defaultGreen[idx]
        signals[idx].yellow = defaultYellow

    # Switch to the other pair
    activePair = inactivePair
    currentPhase = "green"
    repeat()  # Recursively continue the cycle

                                                                                            
def generateVehicles():
    while True:
        # random number between the 4 vehicles 
        vehicle_type = random.randint(0,3)
        lane_number = random.randint(1,2)
        dice = random.randint(0,99)
        direction_number = 0
        # Use probability ranges to assign direction based on dice roll.
        if dice < 25:
            direction_number = 0
        elif dice < 50:
            direction_number = 1
        elif dice < 75:
            direction_number = 2
        else:
            direction_number = 3
        Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])
        time.sleep(1)  # Adjust spawn rate as needed


class Main:
    def __init__(self):
        # Start the signal initialization thread.
        threading.Thread(target=initializeSignals, daemon=True).start()
        # Start vehicle generation thread.
        threading.Thread(target=generateVehicles, daemon=True).start()
        self.run()

    def run(self):
        # window size spawn when opened 
        black = (0, 0, 0)
        white = (255, 255, 255)
        screenWidth = 1400
        screenHeight = 800
        screenSize = (screenWidth, screenHeight)

        # Below are paths to the images used in the simulation
        background = pygame.image.load('images/intersection.png')
        screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption("SIMULATION")

        redSignal = pygame.image.load('images/signals/red.png')
        yellowSignal = pygame.image.load('images/signals/yellow.png')
        greenSignal = pygame.image.load('images/signals/green.png')
        font = pygame.font.Font(None, 30)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.blit(background, (0, 0))
            # Render signals for each index
            for i in range(noOfSignals):
                # For signals that belong to the active pair, display their green or yellow timer.
                if i in pairMapping[activePair]:
                    if signals[i].green > 0:
                        signals[i].signalText = signals[i].green
                        screen.blit(greenSignal, signalCoods[i])
                    elif signals[i].yellow > 0:
                        signals[i].signalText = signals[i].yellow
                        screen.blit(yellowSignal, signalCoods[i])
                else:
                    # Inactive signals display red.
                    if signals[i].red <= 10:
                        signals[i].signalText = signals[i].red
                    else:
                        signals[i].signalText = "---"
                    screen.blit(redSignal, signalCoods[i])
                textRendered = font.render(str(signals[i].signalText), True, white, black)
                screen.blit(textRendered, signalTimerCoods[i])
            # Update and draw vehicles.
            for vehicle in simulation:
                vehicle.move()
                screen.blit(vehicle.image, (vehicle.x, vehicle.y))
            # Show updated changes in the simulation window 
            pygame.display.update()

if __name__ == '__main__':
    image_uploader()
    vehicle_counter()
    Main()
