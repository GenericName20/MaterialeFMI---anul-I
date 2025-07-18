ans = [];

async function loadResponses() {
    try {
        const response = await fetch('./magic.json');
        const replies = await response.json();

        for (let key in replies) {
            ans.push([replies[key].text, replies[key].bool]);
        }

        console.log("Data from magic.json loaded!");
    } catch (error) {
        console.error('Error fetching data from magic.json:', error);
    }
}

window.onload = async function(){
    await loadResponses();
    console.log(ans);
    ball = document.getElementById("magicBall");
    ball.addEventListener("click", function() {
        let current = Math.floor(Math.random() * ans.length);
        let response = ans[current][0];
        let bool = ans[current][1];
        switch (bool){
            case "yes":
                color = "lime";
                break;
            case "maybe":
                color = "yellow";
                break;
            case "no":
                color = "red";
                break;
        }
        let rFace = document.getElementById("responseFace");
        rFace.style.backgroundColor = color;
        let init = document.getElementById("initial");
        if (init != null){
            init.style.display = "none";
        }
        let rZone = document.getElementById("responseZone");
        rZone.style.color = color;
        rZone.innerHTML = response;
    });
}