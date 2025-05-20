let home = 0
let guest = 0

document.getElementById("home_score").textContent = home
document.getElementById("guest_score").textContent = guest

function add_one(){
    home += 1
    document.getElementById("home_score").textContent = home

}

function mid_range(){
    home += 2
    document.getElementById("home_score").textContent = home
}

function from_deep(){
    home += 3
    document.getElementById("home_score").textContent = home
}

function free_throw(){
    guest += 1
    document.getElementById("guest_score").textContent = guest
}

function from_2(){
    guest += 2
    document.getElementById("guest_score").textContent = guest
}

function from_3(){
    guest += 3
    document.getElementById("guest_score").textContent = guest
}