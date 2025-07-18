function genDots(color, size){
    dot = document.createElement("div");
    dot.style.backgroundColor = color;
    dot.style.position = "absolute";

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;
    dot.style.left = `${randomX}px`;
    dot.style.top = `${randomY}px`;
    dot.style.padding = `${size}px`;
    dot.style.borderRadius = "50%";

    dot.addEventListener("click", (event) => {
        genDots(color, size);
    });
    updateCounter();
    document.body.appendChild(dot);
}

function createRange(){
    let sizerContainer = document.createElement("div");
    sizerContainer.style.zIndex = "1001";
    sizerContainer.width = "200";
    sizerContainer.height = "100";
    sizerContainer.id = "sizerContainer";
    sizerContainer.style.zIndex = "1001";
    document.body.appendChild(sizerContainer);

    toAppend = document.getElementById("sizerContainer");

    const sizer = document.createElement("input");
    sizer.type = "range";
    sizer.id = "dotsize";
    sizer.name = "dotsize";
    sizer.min = "20";
    sizer.max = "150";
    sizer.style.zIndex = "1001";
    toAppend.appendChild(sizer);
}

function updateCounter(){
    currentCounter = document.getElementById("dotCounter");
    if (currentCounter == null) {
        localStorage.setItem("clickCount", 0);
        counter = document.createElement("p");
        counter.innerHTML = 0;
        counter.id = "dotCounter";
        document.body.appendChild(counter);
    }
    else {
        clickCount = localStorage.getItem("clickCount");
        clickCount++;
        currentCounter.innerHTML = clickCount;
        localStorage.setItem("clickCount", clickCount);
    }
}

window.onload = async function(){
    updateCounter();
    createRange();

    document.addEventListener('keydown', function (event) {
        range = document.getElementById("dotsize");
        size = range.value;

        switch (event.key.toLowerCase()){ 
            case "r":
                genDots("red", size);
                break;
            case "g":
                genDots("green", size);
                break;
            case "b":
                genDots("blue", size);
                break;
            case "y":
                genDots("yellow", size);
                break;
        }
    });
}