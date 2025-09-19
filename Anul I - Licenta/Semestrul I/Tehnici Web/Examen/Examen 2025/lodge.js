let info = [];

async function loadJSON() {
    try {
        const response = await fetch('./resources/quotes.json');
        const structure = await response.json();

        for (let key in structure) {
            info.push(structure[key]);
        }

    } catch (error) {
        console.error('Permisul și buletinul? Doesn\'exist', error);
    }
}

function arataSmecherul(){
    character = document.getElementById("character");
    quote = document.getElementById("quote");
    moreInfo = document.getElementById("season_episode");
    let current = Math.floor(Math.random() * info.length);
    
    character.innerHTML = info[current]["character"];
    quote.innerHTML = info[current]["quote"];
    moreInfo.innerHTML = "Season: " + info[current]["season"] + " | Episode: " + info[current]["episode"];
}

function spawnPopaTanda(){
    rose = document.createElement("img");
    rose.src = "./resources/images/rose.webp";
    rose.style.width = "100px";
    rose.style.position = "absolute";
    rose.style.top = "50px";
    rose.style.left = "110px";
    rose.style.cursor = "grab";

    rose.addEventListener("click", function(event){
        arataSmecherul();
    });

    document.body.appendChild(rose);
}

window.onload = async function(){
    await loadJSON();
    spawnPopaTanda();
}