# Model subiecte examen

## layout, grid, media query
1. Scrieți un fișier HTML `grid.html` care să conțină un div cu id-ul `wrapper`. În interiorul lui, adăugați încă alte 6 divuri. Creați un fișier `grid.css` în care să adăugați reguli CSS astfel încât pagina să arate ca în imaginea de mai jos și:
- fiecare coloană să aibă lățimea de 150px
- spațiul dintre linii și coloane să fie de 10px
- divurile să aibă padding de 20px
- divurile A, B, C, D vor avea border alb, dashed, de 2px

<img alt="grid" src="./grid.png" width="500px">

2. Scrieți un media query pentru ferestre cu lățimea între 200px și 6oopx astfel încât divurile A, B, C, D să nu mai fie afișate cu layoutul de mai sus, ci în formatul default, unele sub altele, ocupând întreaga lațime a containerului.

## [dots dots dots](https://www.tate.org.uk/art/artists/yayoi-kusama-8094/yayoi-kusamas-obliteration-room): events, forms, localStorage

3. Scrieți un fișier HTML `dots.html` care să conțină un body gol. Adăugați cod JavaScript în fișierul `dots.js`	astfel încât la apăsarea uneia din tastele r, g, y, b să se creeze un div nou în pagină. Fiecare div nou creat va conține o bulină colorată corespunzător tastei apăsate (r: roșu, g: verde, y: galben, b: albastru). Poziția divului în pagină va fi aleatoare. Dimensiunea bulinei va fi dată de valoarea unui element range cu id-ul `size` cu valoarea minimă 20 și valoarea maximă 150.

4. La apăsarea unei buline de pe ecran, se va mai crea o bulină de aceeași culoare și dimensiune.

5. Salvați în `localStorage` numărul de buline create în total și afișați-l în colțul din stânga sus a ecranului.

## 2D graphics, events, fetch

6. Scrieți un fișier HTML `magic.html` astfel încât să desenați, folosind fie elementul `canvas` (și cod JavaScript), fie cod CSS, un [8 magic ball](https://en.wikipedia.org/wiki/Magic_8_Ball) ca în imaginea de mai jos.

<img alt="8 magic ball" src="./magic.png" width="200px">

Dacă nu știți să desenați magic ball-ul folosind canvas sau CSS, puteți folosi imaginea 'resources/images/magic.png' pentru a continua rezolvarea subiectului (cu punctaj parțial, pentru neîndeplinirea primei cerințe).

7. Voi întrebați, bila răspunde: la apăsarea bilei, discul alb din centrul bilei se va colora în roșu, verde, sau portocaliu. 
Scrieți un handler corespunzător evenimentului de click astfel încât să afișați unul din posibilele răspunsuri pe care le poate întoarce 8 magic ball-ul. Răspunsurile sunt salvate în fișierul `magic.json` pe un server http local (porniți un server http folosind, de exemplu, Python). Folosiți fetch și promisiuni pentru a accesa conținutul fișierului. La fiecare click pe bilă, se va alege aleator unul din posibilele răspunsuri. Dacă răspunsul ales este afirmativ, discul alb se va colora verde; dacă răspunsul este negativ, discul se va colora roșu; altfel, se va colora portocaliu. Afișați sub bilă și mesajul răspunsului ales, colorat cu aceeași culoare ca discul din centrul bilei.

<img alt="8 magic ball" src="./magic-maybe.png" width="200px">



