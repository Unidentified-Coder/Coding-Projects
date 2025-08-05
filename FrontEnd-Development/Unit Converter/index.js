// conversion rates to be used
// 1 meter = 3.281 feet
// 1 liter = 0.264 gallon
// 1 kilogram = 2.204 pound


// First get the ids from HTML
const Length = document.getElementById("Length")
const Volume = document.getElementById("Volume")
const Mass = document.getElementById("Mass")

// Get the id from the user input field

// Function for Length , Volume and Mass
function Convert(){
    const Conversion = parseFloat(document.getElementById("Conversion").value)
    
    if(isNaN(Conversion)){
        alert("Please enter a valid number!")
        return
    }

    const metersToFeet = (Conversion * 3.281).toFixed(3);
    const feetToMeters = (Conversion / 3.281).toFixed(3);

    document.getElementById('Length').innerText =
        `${Conversion} meters = ${metersToFeet} feet | ${Conversion} feet = ${feetToMeters} meters`;

    const litreToGallons = (Conversion * 0.264).toFixed(3);
    const gallonToLitres = (Conversion / 0.264).toFixed(3);

    document.getElementById('Volume').innerText =
        `${Conversion} litres = ${litreToGallons} gallon | ${Conversion} gallon = ${gallonToLitres} litres`;

    const kilogramToPounds = (Conversion * 2.204).toFixed(3);
    const poundsToKilograms = (Conversion / 2.204).toFixed(3);

    document.getElementById('Mass').innerText =
        `${Conversion} Kilograms = ${kilogramToPounds} pounds | ${Conversion} pound = ${poundsToKilograms} Kilograms`;

}