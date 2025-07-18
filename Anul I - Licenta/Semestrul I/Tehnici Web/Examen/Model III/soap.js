function updateCounter(){
    cnt = document.getElementById("genucounter");
    if (cnt == undefined){
        localStorage.setItem("totalCounter", 0);
        newCnt = document.createElement("p");
        newCnt.style.position = "absolute";
        newCnt.style.left = "1000px";
        newCnt.id = "genucounter";
        newCnt.innerHTML = "Ai spart 0 baloane copile huaaaaa!";
        document.body.appendChild(newCnt);
    }
    else{
        totalCounter = localStorage.getItem("totalCounter");
        totalCounter++;
        cnt.innerHTML = "Ai spart " + totalCounter + " baloane copile huaaaaa!";
        localStorage.setItem("totalCounter", totalCounter);
    }
}

function cycleImages(element){
    try{
        element.counter++;
        i = element.counter % 4 + 1;
        element.src = "./resources/images/bubble-" + i + ".png";

        if (element.counter == 3){
            updateCounter();
            clearInterval(element.animation);
            document.body.removeChild(element);    
        }
    }
    catch{
        return;
    }
}

function spawnBubble(){
    bubble = document.createElement("img");
    bubble.src = "./resources/images/bubble-1.png";
    bubble.alt = "Bubbles, bubbles, bubbles... Bubbles?";

    bubble.style.position = "absolute";

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    bubble.style.left = `${randomX}px`;
    bubble.style.top = `${randomY}px`;


    bubble.counter = 0;
    bubble.addEventListener("click", function(event){
        event.target.animation = setInterval(cycleImages, 200, event.target);
    });

    document.body.appendChild(bubble);
}

function flyAround(bubble){
    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    bubble.style.left = `${randomX}px`;
    bubble.style.top = `${randomY}px`;
}

activeBallons = false;
function moveBubbles() {
    if (activeBallons == false){
        activeBallons = true;
        const bubbles = document.querySelectorAll("img[alt='Bubbles, bubbles, bubbles... Bubbles?']");
        bubbles.forEach(bubble => {
            const randomX = Math.random() * window.innerWidth;
            const randomY = Math.random() * window.innerHeight;
            bubble.style.transition = "left 1s ease-in-out, top 1s ease-in-out";
            bubble.animation = setInterval(flyAround, 200, bubble);
        });
    }
    else{
        const bubbles = document.querySelectorAll("img[alt='Bubbles, bubbles, bubbles... Bubbles?']");
        bubbles.forEach(bubble => {
            clearInterval(bubble.animation);
        });
        activeBallons = false;
    }
}

window.onload = async function(){
    updateCounter();
    document.addEventListener("keydown", function (event){
        switch (event.key){
            case "s":
                spawnBubble();
                break;
            case "p":
                moveBubbles();
                break;
        } 
    });

}