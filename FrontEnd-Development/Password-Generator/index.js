// Constant variable that has every shortlisted characters used for passwords
const characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]",",","|",":",";","<",">",".","?",
"/"];

// Firstly you are going to get the ids from HTML
let password1 = document.getElementById("pass1")
let password2 = document.getElementById("pass2")

// Next test that the ids are passing info through
// let a = 56
// let b = 21

// password1.textContent = a
// password2.textContent = b

// Tests are successful


// A function once clicked can generate 2 random passwords
function new_pass(){
    // array created 
    let pass1 = []
    let pass2 = []
    
    // For loop to go over items in the characters array
    for (let i = 0; i < 15; i++){
        // randomize the characters from and push it to the id
        let a = characters[Math.floor(Math.random() * characters.length)]
        let b = characters[Math.floor(Math.random() * characters.length)]
        
        pass1 += a
        pass2 += b
    // once array is filled with 15 characters theN return them into the html
    password1.textContent = pass1
    password2.textContent = pass2


}
}

new_pass()
