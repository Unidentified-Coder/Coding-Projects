import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil
import os

# initialize variables before being used inside function
label = None
status_label = None
img_display = None

# Function to take in an image as input
def image_uploader():
    
    # Allow different image file types to be accepted
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    # Set variables to global to be later called 
    if file_path:
        global label
        global status_label
        global img_display
        
        if label is not None:
            label.config(image=img_display)
            image = Image.open(file_path)
            image.thumbnail((600, 600)) 
        if img_display is not None:
            img_display = ImageTk.PhotoImage(image)
            label.image = img_display  
        
        # Save the file to a shared directory
        img_path = "image-Folder/shared_image.png"  
        os.makedirs("image-Folder", exist_ok=True)  
        shutil.copy(file_path, img_path)
        if status_label is not None:
            status_label.config(text=f"Image saved as {img_path}", fg="black")

# Tkinter GUI setup
    root = tk.Tk()
    root.title("Image Uploader")

    btn = tk.Button(root, text="Upload Image", command=image_uploader)
    btn.pack()

    label = tk.Label(root)
    label.pack()

    status_label = tk.Label(root, text="No image uploaded", fg="red")
    status_label.pack()

    root.mainloop()

def vehicle_counter():

    # Trained dataset
    cascade_src = ('cars.xml')
    car_cascade = cv2.CascadeClassifier(cascade_src)

    # Save image path as variable for easier access
    img = cv2.imread("image-Folder/Shared_image.png")

    # Throws an error, Exit code if img is not available 
    if img is None:
        print("Error: Image not found or cannot be loaded")
        exit()

    # Convert image into grey scale for identification 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Draws boxes on detected vehicles
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30,30))

    # Initialise the vehicle count variable to be used within for loop
    vehicle_count = 0
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+y,y+h),(0,0,250),2)
        vehicle_count += 1

    height, width, _ = img.shape

    text_x = width - 250
    text_y = height - 250

    # Places text on image to show the amount of vehicles counted in process
    cv2.putText(img, f"Vehicles: {vehicle_count}",(text_x,text_y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA )

    # Output the result in a windows app format 
    cv2.imshow('Detected Vehicles', img)

    # release the contents by freeing up memory used in operation 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

