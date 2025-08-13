let home = 0
let guest = 0

document.getElementById("H_Score").textContent = home
document.getElementById("A_Score").textContent = guest

function home_add(pass){
    home += pass
    document.getElementById("H_Score").textContent = home

}

function away_add(pass){
    guest += pass
    document.getElementById("A_Score").textContent = guest
}
