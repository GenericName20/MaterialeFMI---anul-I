let movies = [];

async function loadJSON() {
    try {
        const response = await fetch('./resources/zap.json');
        const structure = await response.json();

        for (let key in structure) {
            movies.push(structure[key]);
        }

    } catch (error) {
        console.error('Error fetching data from bachelors.json:', error);
    }
}

function printMovie(){
    info = document.getElementById("info");
    info.style.visibility = "visible";
    data = document.getElementById("data");
    ora_titlu = document.getElementById("ora_titlu");
    poster = document.getElementById("poster");

    let current = Math.floor(Math.random() * movies.length);
    data.innerHTML = movies[current]["date"];
    ora_titlu.innerHTML = movies[current]["time"] + " - " + movies[current]["title"];
    poster.src = "./resources/" + movies[current]["poster"];

    suplimentare = document.getElementById("suplimentare");
    suplimentare.innerHTML = "Cu: " + movies[current]["starring"] + ", Rating: " + movies[current]["rate"];
}

window.onload = async function(){
    await loadJSON();
    tv = document.getElementById("tv");
    info = document.getElementById("info");
    info.style.visibility = "hidden";
    tv.addEventListener("click", (event) => {
        printMovie();
    });
}