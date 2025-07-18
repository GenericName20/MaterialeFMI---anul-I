# Laborator 10 - ajax

*Folosiți notele de curs ca să vă amintiți conceptele de bază legate de XML, JSON și AJAX din [cursul 10](https://cs.unibuc.ro/~cechirita/tw/c10) și rezolvați următoarele exerciții.*  

## XML, mon amour

1. Scrieți un fișier XML `cinemateca.xml` care să conțină informații despre 2 filme la alegere. Fișierul trebuie să conțină cel puțin următoarele detalii despre fiecare film: titlul (și limba în care e dat titlul), genul, regizorul, anul lansării,
scenaristul, producătorul, actori (1-2, dacă există, și tipul de rol: principal, secundar), scorul.  
[Validați](https://www.w3schools.com/xml/xml_validator.asp) sintaxa fișierului XML și corectați eventualele greșeli.

2. Creați un fișier `cinemateca.html` și un fișier `cinemateca.js`. Convertiți conținutul fișierului `cinemateca.xml` într-un obiect JavaScript folosind `DOMParser`. Afișați în fișierul HTML, folosind liste neordonate, conținutul obiectului JavaScript nou creat.

## JSON

3. Convertiți conținutul fișierului `cinemateca.xml` în format JSON și salvați-l într-un fișier `cinemateca.json`.  
Validați fișierul folosind [https://jsonlint.com/](https://jsonlint.com/) și corectați eventualele greșeli.

## http server up!

4. Mai țineți minte [cum funcționează internetul](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/How_does_the_Internet_work)? Sigur sigur? Dar [un server web](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)?  
Atunci, să pornim un server! Urmați instrucțiunile de [aici](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/set_up_a_local_testing_server) pentru a porni un server http folosind Python.  
Veți folosi acest server pentru a rezolva exercițiile de mai jos.

## AJAX

Descărcați fișierul `fonoteca.zip` din directorul `resources`. Sarcina voastră principală este să modificați fișierele HTML și JavaScript pentru a crea o colecție web de albume de muzică.  

Pagina web va fi împărțită în două: în partea stângă, vom avea o galerie de imagini cu copertele albumelor de muzică. În partea dreaptă, vor fi afișate detaliile unui album la apăsarea imaginii copertei lui.

5. Adăugați cod JavaScript în fișierul `fonoteca.js` pentru a obține, folosind [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/fetch), lista de albume din fișierul `albums.json`.  
*Hint: Nu uitați să accesați pagina `fonoteca.html` folosind serverul web deschis la exercițiul anterior: http://localhost:8000/fonoteca.html*

Adăugați în div-ul `#gallery` imaginile copertelor albumelor și numele lor. *Hint: Folosiți `display:grid`.*

6. La apăsarea unei imagini, lansați un nou `fetch()` pentru a obține fișierul cu mai multe detalii despre albumul selectat. Fișierele sunt denumite corespunzător poziției albumului în Array-ul JSON. Afișați conținutul fișierului în div-ul `#info` (adăugați elemente HTML corespunzătoare, nu afișați conținutul doar ca text nestructurat). 

## extra
7. Adăugați în pagina `fonoteca.html` un câmp de căutare care să filtreze lista de albume afișată în galeria de imagini: vor fi afișate doar albumele care conțin cuvântul introdus în câmpul de căutare ca subșir de caracter al titlului, numelui artistului, ori anului de lansare.  

8. Adăugați cod HTML și CSS pentru a crea o pagină web completă.




