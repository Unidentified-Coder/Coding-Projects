// Constant variable that has every shortlisted characters used for passwords
const characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]",",","|",":",";","<",">",".","?",
"/"];

// Firstly you are going to get the ids from HTML
let password1 = document.getElementById("pas1")
let password2 = document.getElementById("pas2")

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
    for (let i = 0; i < 30; i++){
        // randomize the characters from and push it to the id
        let a = Math.floor(Math.random() * 95 + 1)
        let b = Math.floor(Math.random() * 95 + 1)
        // use a conditional statement to allow a character to be pushed to an array
        if (pass1.length === 14 && pass2.length === 14){
            pass1.push(a) 
            pass2.push(b) 

        }
    // // once array is filled with 15 characters them return them into the html
    // pass1.textContent = password1
    // pass2.textContent = password2
    console.log(pass1)

}
}

