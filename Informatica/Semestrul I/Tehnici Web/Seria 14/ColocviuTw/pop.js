function getRandom(minim,maxim)
{
    return Math.random() * (maxim-minim) + minim;
}

function loadPow(positionX,positionY,body){
     const pow = document.createElement('div');
     pow.innerHTML = '<img src="pow.png" alt="pow">';
     pow.classList.add('pow');
     pow.style.position = "absolute";
     pow.style.top = positionY+"px";
     pow.style.left = positionX+"px";
     body.appendChild(pow);
     setTimeout(() => {
         pow.remove();
     }, 500);
}
document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const scoreDisplay = document.getElementById('score');
    let score = parseInt(localStorage.getItem('score')) || 0;
    let intervalId = null;

    const updateScore = () => {
        scoreDisplay.textContent = `Baloane sparte: ${score}`;
    };

    updateScore();
 
   function createBalloon() {
        const balloon = document.createElement('div');
        balloon.innerHTML = '<img src="balloon.png" alt="balloon">';
        balloon.classList.add('balloon');
        balloon.style.position = "absolute";
        balloon.style.top = getRandom(0,innerHeight)+"px";
        balloon.style.left = getRandom(0,innerWidth)+"px";
        balloon.addEventListener('click', (event) => {
            balloon.classList.add('pop');
            event.clientX = event.clientX;
            event.clientY = event.clientY;
            loadPow(event.clientX,event.clientY,body);
            playPopSound();
            setTimeout(() => {
                balloon.remove();
                score++;
                localStorage.setItem('score', score);
                updateScore();
            }, 300);
        });

        body.appendChild(balloon);
    };

    const playPopSound = () => {
        const sunete = [
            'pop-1.mp3',
            'pop-2.mp3',
            'pop-3.mp3'
        ];
        const sunet = new Audio(sunete[Math.floor(Math.random() * sunete.length)]); 
        sunet.play();
    };

    document.addEventListener('keydown', (event) => {
        if (event.key === 'b') {
            //console.log('b pressed');
            createBalloon();
        } else if (event.key === 'p') {
            //console.log('p pressed');
            if (!intervalId) {
                intervalId = setInterval(() => {
                    const balloons = document.querySelectorAll('.balloon');
                    balloons.forEach(balloon => {
                        const top = parseFloat(balloon.style.top);
                        balloon.style.top = `${top - 2}px`;
                    });
                }, 30);
            }
        } else if (event.key === 'f') {
            //console.log('f pressed');
            if (intervalId) {
                clearInterval(intervalId);
                intervalId = null;
            }
        }
    });
});
