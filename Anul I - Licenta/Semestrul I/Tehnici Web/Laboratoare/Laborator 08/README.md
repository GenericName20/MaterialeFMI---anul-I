# Laborator 8 - evenimente

*Folosiți notele de curs ca să vă amintiți conceptele de bază ale tratării evenimentelor DOM cu JavaScript din [cursul 8](https://cs.unibuc.ro/~cechirita/tw/c8) și rezolvați următoarele exerciții.*  

## exersați, exersați, exersați

1. Jucați-vă cu simulatorul de declanșări de evenimente DOM [domevents](https://domevents.dev/). Recapitulați astfel modelul *bubble* și *capture* pentru funcțiile de tratare a evenimentelor, oprirea propagării evenimentelor și prevenirea comportamentului default.

## desenați, desenați, desenați

Revedeți soluțiile pentru laboratorul 7. În continuare veți modifica fișierele `draw.html`, `style.css` și `draw.js` scrise la laboratorul trecut pentru a rezolva exercițiile de mai jos. 

Mai întâi vom modifica tabla de desenat în așa fel încât să putem schimba culoarea unei celule folosind un mouse click.

1. Scrieți o funcție event handler pentru un mouse click pe o celulă din tablă. Handlerul va apela funcția `drawPixel`. 

2. Adăugați în pagină (`draw.html`) un element html pentru selectarea unei culori. *Hint: folosiți [&lt;input type="color"&gt;](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/color), așa cum am învățat în [cursul 9](https://cs.unibuc.ro/~cechirita/tw/c9/#/24).* Modificați handlerul de la exercițiul 1 astfel încât să folosească culoarea aleasă de utilizator cu ajutorul selectorului de culoare ca argument la apelarea funcției `drawPixel`.

Acum vom adăuga alte butoane utile pentru desenat.

3. Adăugați un buton `curcubeu` în pagina `draw.html`. La apăsarea butonului, va apărea un curcubeu pe tabla de desen.  
*Hint: apelați funcția `rainbow` în handlerul pentru evenimentul de tip `onclick`.* 

(opțional) Adăugați butoane similare pentru funcțiile `jumble`, `rotate` (transpose) și `mirror`.

4. Adăugați un buton `clear` care șterge toate culorile de pe tabla de desenat.

## say cheese!

Descărcați fișierele `camera.html`, `style.css` și `camera.js` din directorul `resources`. Sarcina voastră principală este să modificați fișierul JavaScript pentru a scrie o mică aplicație web care imită o cameră foto.  

5. Scrieți o funcție handler pentru evenimente generate de apăsarea tastelor pentru a controla ce se vede prin vizorul camerei (conținutul div-ului `vizor`). La apăsarea tastelor de direcție (arrow keys), mutați imaginea în mod corespunzător. Asigurați-vă că vizorul nu depășește limitele imaginii (apăsarea unei arrow key nu va mai muta imaginea de la un punct încolo).  
*Hint: controlați secțiunea vizibilă a imaginii modificând proprietatea CSS `margin` a elementului `img`.*  

(opțional) Controlați secțiunea vizibilă a imaginii și folosind mouse-ul (cu acțiunea de *drag*). 

6. Zoom in: scrieți o funcție  handler pentru evenimente generate de apăsarea tastelor care să permită scalarea imaginii prin apăsarea tastelor "+" (zooom in) și "-" (zoom out).   
*Hint: folosiți proprietatea CSS `scale`.*   
  
(opțional) Controlați scalarea și folosind mouse-ul, prin scroll.

7. Să facem poze! Scrieți o funcție handler pentru evenimente generate de apăsarea tastelor pentru a *face o poză* la apăsarea tastei 's'. Adăugați o animație ori redați un sunet pentru a semnala capturarea imaginii vizibile prin vizor. Întoarceți, de asemenea, un obiect, copie a elementului div `container` de la momentul capturării.  
*Hint: pentru animație, puteți folosi proprietatea CSS `clip`. Atenție la copierea obiectului: faceți o clonă, nu copie prin referință. Nu uitați de id-ul elementului.*

8. Adăugați în pagina `camera.html` o galerie în care să afișați ultimele imagini capturate. Adăugați galeria sub vizorul camerei.

9. Scrieți o funcție care să permită capturarea unei imagini cu timer, după 5 secunde de la apăsarea tastei 't'. Afișați într-un element `div` secundele rămase până la capturarea imaginii.   
*Hint: folosiți funcția `setTimeout`.* 

(opțional) Permiteți alegerea duratei timer-ului (în loc de 5 secunde) prin apăsarea unei taste numerice după apăsarea tastei 't'.

10. Scrieți o funcție care să permită capturarea mai multor imagini în succesiune rapidă (burst), odată cu apăsarea tastei 'b'. Capturați câte o imagine la fiecare 0.5 secunde, vreme de 2 secunde.   
*Hint: folosiți funcția `setInterval`.*




