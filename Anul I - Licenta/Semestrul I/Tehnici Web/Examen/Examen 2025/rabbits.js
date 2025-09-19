function updateCounter(){
    currentCounter = document.getElementById("howManyRabbits");
    if (currentCounter == undefined){
        // i don't really hate localStorage, i fixed it! :3333333333
        s = localStorage.getItem("totalCounter");
        if (s == null)
        {
            localStorage.setItem("totalCounter", 0);
            s = localStorage.getItem("totalCounter");
        }
        newCounter = document.createElement("p");
        newCounter.style.position = "absolute";
        newCounter.style.left = innerWidth - 100 + "px";
        newCounter.style.color = "white";
        newCounter.id = "howManyRabbits";
        newCounter.innerHTML = s;
        document.body.appendChild(newCounter);
    }
    else {
        totalCounter = localStorage.getItem("totalCounter");
        totalCounter++;
        currentCounter.innerHTML = totalCounter;
        localStorage.setItem("totalCounter", totalCounter);
    }
}

function cycleImages(element){
    try {
        element.counter++;
        i = element.counter % 3 + 1;
        element.src = "./resources/images/rabbit-0" + i + ".png";

        if (element.counter == 3){
            document.body.removeChild(element);    
        }
    }
    catch {
        return;
    }
}

function spawnRabbit(){
    image = document.createElement("img");
    image.src = "./resources/images/rabbit-01.png";
    image.alt = "Vlad Iepurescu :))";

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    image.style.left = `${randomX}px`;
    image.style.top = `${randomY}px`;
    image.style.position = "absolute";
    image.counter = 0;

    image.addEventListener("mouseover", function (event){
        event.target.style.cursor = "grab";
    });

    image.addEventListener("click", function(event){
        event.stopPropagation();
            cycleImages(event.target);
        });
    
    updateCounter();
    document.body.appendChild(image);
}

function flyAround(bubble){
    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    bubble.style.left = `${randomX}px`;
    bubble.style.top = `${randomY}px`;
}

activeRabbits = false;
function moveSigmaRabbits() {
    if (activeRabbits == false){
        activeRabbits = true;
        const rabbits = document.querySelectorAll("img[alt='Vlad Iepurescu :))']");
        rabbits.forEach(rabbit => {
            clearInterval(cycleImages);
            const randomX = Math.random() * window.innerWidth;
            const randomY = Math.random() * window.innerHeight;
            rabbit.style.transition = "left 1s ease-in-out, top 1s ease-in-out";
            rabbit.animation = setInterval(flyAround, 200, rabbit);
        });
    }
}

function stopBetaRabbits(){
    const rabbits = document.querySelectorAll("img[alt='Vlad Iepurescu :))']");
    rabbits.forEach(rabbit => {
        clearInterval(rabbit.animation);
    });
    activeRabbits = false;
}

function generateAudio(){
    newAudioPff = document.createElement("audio");
    newAudioPff.src = "./resources/rabbits-ambience.mp3";
    newAudioPff.id = "skibidiRabbit";
    document.body.appendChild(newAudioPff);
}

function playNiceAndBeautifulHyperGalaxicOrbitalMusicForMySoul(){
    myFunnySkibidiSound = document.getElementById("skibidiRabbit");
    myFunnySkibidiSound.play();
}

window.onload = async function(){
    updateCounter();
    generateAudio();

    document.addEventListener("keydown", function(event){
        switch (event.key){
            case "r":
                spawnRabbit();
                break;
            case "p":
                moveSigmaRabbits();
                break;
            case "s":
                stopBetaRabbits();
                break;
            case "a":
                playNiceAndBeautifulHyperGalaxicOrbitalMusicForMySoul();
                break;
            }
    });
}