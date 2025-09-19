counter = 0;

function spawnMush(){
    mushroom = document.createElement("img");
    mushroom.src = "./resources/images/mush.png";
    mushroom.alt = "Mushroom!";
    mushroom.style.position = "absolute";

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    mushroom.style.left = `${randomX}px`;
    mushroom.style.top = `${randomY}px`;

    document.body.appendChild(mushroom);
}

function cycleImages(element){
    if (element.counter == 0){
        setTimeout(() => {
            console.log("Delayed :3");
        }, 1000);
    }
    element.counter++;
    i = element.counter % 4 + 1;
    element.src = "./resources/images/badger-" + i + ".png";

    if (element.counter != 0 && element.counter % 5 == 0){
        updateCounter();
    }
}

function spawnBadger(){
    image = document.createElement("img");
    image.src = "./resources/images/badger-1.png";

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    image.style.left = `${randomX}px`;
    image.style.top = `${randomY}px`;
    image.style.position = "absolute";
    image.counter = 0;

    image.addEventListener("click", function(event){
        event.stopPropagation();
            if (event.target.animation == undefined) {
                event.target.animation = setInterval(cycleImages, 200, event.target);
            }
            else{
                clearInterval(event.target.animation);
                document.body.removeChild(event.target);
            }
        });
    
    document.body.appendChild(image);
}

function playMusic(){
    audio = document.getElementById("funnySound");
    audio.play();
}


function updateCounter(){
    cnt = document.getElementById("genucounter");
    if (cnt == undefined){
        localStorage.setItem("totalCounter", 0);
        newCnt = document.createElement("p");
        newCnt.id = "genucounter";
        newCnt.innerHTML = 0;
        document.body.appendChild(newCnt);
    }
    else{
        totalCounter = localStorage.getItem("totalCounter");
        totalCounter++;
        cnt.innerHTML = totalCounter;
        if (totalCounter % 5 == 0){
            spawnMush();
        }
        localStorage.setItem("totalCounter", totalCounter);
    }
}

window.onload = async function(){
    updateCounter();

    document.addEventListener("keydown", function(event){
        switch (event.key){
            case "b":
                spawnBadger();
                break;
            case "p":
                playMusic();
                break;
        }
    });
}