document.addEventListener("DOMContentLoaded", () => {
    let cnt = document.createElement("div")
    cnt.textContent = localStorage.getItem("cntBalloons")
    cnt.style.position = 'absolute'
    cnt.style.right = '10px'
    cnt.style.top = '10px'
    cnt.style.color = 'black'
    cnt.style.fontSize = '20px'

    document.body.append(cnt)

    document.addEventListener("keydown", (e) => {
        if (e.key.toUpperCase() === 'B') {
            let imgContainer = document.createElement("div")
            imgContainer.style.width = '200px'
            imgContainer.style.height = '200px'
            imgContainer.classList.add('baloon')

            let image = document.createElement("img")
            image.src = 'balloon.png'
            image.style.width = '100%'
            image.style.height = '100%'
            image.style.objectFit = 'contain'

            imgContainer.append(image)

            let x = Math.floor(Math.random() * window.innerWidth)
            let y = Math.floor(Math.random() * window.innerHeight)

            imgContainer.style.position = 'absolute'
            imgContainer.style.top = x.toString() + 'px'
            imgContainer.style.left = y.toString() + 'px'

            imgContainer.addEventListener("click", () => {
                imgContainer.children[0].src = 'pow.png'

                if (!localStorage.getItem("cntBalloons")) {
                    localStorage.setItem("cntBalloons", "0")
                } else localStorage.setItem("cntBalloons", (parseInt(localStorage.getItem("cntBalloons")) + 1).toString())
                cnt.textContent = localStorage.getItem("cntBalloons")

                let number = Math.floor(Math.random() * 3) + 1
                let path = `pop-${number}.mp3`

                let audioElem = document.createElement("audio")
                audioElem.src = path
                audioElem.play()

                document.body.append(audioElem)

                setTimeout(() => {
                    imgContainer.removeChild(imgContainer.children[0])
                }, 3000)
            })

            document.body.append(imgContainer)
        } else if (e.key.toUpperCase() === 'P') {
            let timer = setInterval(() => {
                let balloons = document.getElementsByClassName('baloon')
                for (let i = 0; i < balloons.length; i++) {
                    balloons[i].style.top = (parseInt(balloons[i].style.top) - 1).toString() + 'px'
                }
            }, 50)

            document.addEventListener("keydown", (e) => {
                if (e.key.toUpperCase() === 'F') clearInterval(timer)
            })
        }
    })
})