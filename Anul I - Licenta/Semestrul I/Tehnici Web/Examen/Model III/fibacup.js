let info = [];

async function loadJSON() {
    try {
        const response = await fetch('./resources/fibacup.json');
        const structure = await response.json();

        for (let key in structure) {
            info.push(structure[key]);
        }

    } catch (error) {
        console.error('Hmm..', error);
    }
}

function printInfo(){
    homeflag = document.getElementById("homeflag");
    guestflag = document.getElementById("guestflag");
    date = document.getElementById("date");

    let current = Math.floor(Math.random() * info.length);
    homeflag.src = "./resources/" + info[current]["homeflag"];
    guestflag.src = "./resources/" + info[current]["guestflag"];
    date.innerHTML = info[current]["date"] + " at " + info[current]["time"];

    home = document.getElementById("home");
    guest = document.getElementById("guest");
    home.innerHTML = info[current]["home"];
    guest.innerHTML = info[current]["guest"];
}

window.onload = async function(){
    await loadJSON();

    teren = document.getElementById("teren");
    teren.addEventListener("click", (event) => {
        printInfo();
    });
}