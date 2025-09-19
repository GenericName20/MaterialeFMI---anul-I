# Laborator 6 - javascript

*Folosiți notele de curs ca să vă amintiți conceptele de bază de JavaScript din [cursul 6](https://cs.unibuc.ro/~cechirita/tw/c6) și rezolvați următoarele exerciții.*  

## I'm a cyborg, but that's OK. 

1. Jucați primele 6 niveluri din jocul [jsrobot](https://lab.reaal.me/jsrobot/) pentru o scurtă recapitulare.
 
## X și 0

*Rezolvați exercițiile de mai jos pentru a implementa un joc X și 0 cu o interfață ASCII folosind JavaScript.   
Creați un fișier html `ttt.html` cu elementul `body` gol, în care să includeți un fișier JavaScript `ttt.js`. Rezolvarea următoarelor exerciții se va face editând fișierul `ttt.js`.*

2. Folosind `prompt`, afișați mesajul *"Hai să jucăm X și 0. Cum te cheamă?"* și salvați răspunsul într-o variabilă.

3. Afișați mesajul *"Bună, < nume >. Cu ce vrei să joci? X sau 0? X începe primul."* și salvați răspunsul într-o variabilă. 

4. Folosiți un `Array` pentru a reprezenta tabla de joc. `Arrayul` constă din 9  `Stringuri`: primele 3 elemente reprezintă prima linie a tablei de joc, următoarele 3, a doua linie, iar ultimele 3, linia 3. Inițializați fiecare element cu `Stringul` *"?"*, indicând faptul că toate cele 9 celule sunt goale.  
*Hint: folosiți o instrucțiune de tip `for`.*

5. Scrieți o funcție `printtt` care să returneze o reprezentare ASCII a tablei de joc. De exemplu, pentru tabla `["?", "?", "X", "?", "0", "?", "?", "?", "?"]`, ar putea returna    
`| 1 | 2 | X |`  
`| 4 | 0 | 6 |`  
`| 7 | 8 | 9 |`.  
În reprezentarea de mai sus, în fiecare celulă scriem `X` dacă `Array`-ul conține stringul `"X"` la acea poziție, `0` dacă conține stringul `"0"`, sau poziția ei, dacă celula este goală (adică `Array-ul` conține `"?"` la acea poziție).    

6. Începem să jucăm X și 0 singuri, fără adversar. Folosind `prompt`, afișați tabla de joc și mesajul *"Unde vrei să pui următorul semn?"*. Salvați într-o variabilă poziția din tablă. 

7. Scrieți o funcție `valid` care verifică dacă poziția dată de jucător este validă: dacă este o poziție din tablă (un număr cuprins între 1 și 9) și dacă celula de la poziția respectivă este goală. Funcția trebuie să returneze o valoare `booleană`. 

8. Dacă poziția introdusă de jucător nu este validă, trebuie să afișați un mesaj de atenționare și să repetați pasul 6. Dacă poziția este validă, adăugați semnul jucătorului în tabla de joc și repetați pasul 6. 

Jocul nostru rulează momentan într-o buclă, fără să se termine. Chiar dacă tabla este plină, utilizatorul va fi întâmpinat de un prompt care îi cere următoarea poziție la care vrea să adauge un semn.

9.  Scrieți o funcție `win` care verifică dacă tabla este într-o configurație de câștig (dacă există 3 simboluri de X sau 0 identice pe același rând, pe aceeași coloană, ori pe o diagonală) și care returnează simbolul câștigător. 

10. Scrieți o funcție `draw` care verifică dacă tabla este într-o configurație de remiză, returnând un `boolean`. 

11. Modificați codul jocului astfel încât să verificați, după fiecare mișcare a jucătorului, care este starea jocului și afișați (folosind `alert`):
- mesajul *"Bravo, < nume >, ai câștigat!"*, dacă jucătorul a câștigat, 
- mesajul *"Ai pierdut :("* dacă jucătorul a pierdut, sau 
- mesajul *"Remiză!"* în cazul unei remize.
Continuați jocul altfel.

12. E momentul să primim în joc un adversar: calculatorul. Scrieți o funcție `computer_move` care generează aleator, folosind `Math.random()`, o poziție din tabla de joc corespunzătoare următoarei poziții de jucat de către calculator. Verificați dacă poziția este validă folosind funcția `valid` de la exercițiul 7. Dacă poziția este validă, completați tabla de joc în mod corespunzător. Altfel, apelați din nou funcția `computer_move`. 

13. Integrați codul scris pentru exercițiul de mai sus în așa fel încât jucătorul și calculatorul să facă alternativ câte o mișcare, iar jocul să se termine atunci când este atinsă o configurație de câștig ori remiză. 

14. Bonanza extravaganza! Să jucăm două jocuri de X și 0 în paralel!  
Rescrieți codul în așa fel încât jucătorul să poată juca împotriva calculatorului două jocuri diferite în paralel. Astfel, în fiecare `prompt` vor fi afișate două table, iar jucătorul va introduce două poziții de joc (separate printr-un caracter spațiu), câte una pentru fiecare tablă. Jucătorul continuă să joace până la terminarea ambelor jocuri. 

*Hint: Pentru rezolvarea acestui exercițiu va fi nevoie să creați  obiecte de tip `joc` ce vor conține proprietăți pentru reprezentarea  tablei și a jucătorului (cu proprietăți corespunzătoare numelui, și semnului ales) și metode ce corespund funcțiilor pe care le-ați scris pentru rezolvarea exercițiilor de mai sus (`printtt`, `valid`, `win`, `draw`, `computer-move` etc.).*        

## EXTRA

15. Jucați [Untrusted - The Continuing Adventures of Dr. Eval](https://alexnisnevich.github.io/untrusted/).
 

