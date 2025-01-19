

let field = document.getElementById("field")

field.addEventListener("click", async () => {
    try {
        const response = await fetch('champ')
        const data = await response.json()
        console.log(data)

        let number = Math.floor(Math.random() * data.length)
        let meci = data[number]

        // /// let steag
        // field.addEventListener("mouseover", () => {
        //
        // })

        console.log(meci)
    } catch(e) {
        //
    }
})