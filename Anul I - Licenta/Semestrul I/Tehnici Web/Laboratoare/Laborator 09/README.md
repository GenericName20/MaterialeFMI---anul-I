# Laborator 9 - formulare

*Folosiți notele de curs ca să vă amintiți conceptele de bază ale definirii formularelor din [cursul 9](https://cs.unibuc.ro/~cechirita/tw/c9) și rezolvați următoarele exerciții.*  

## it's regex time!

Vizitați [tutorialul](https://regexlearn.com/learn/regex101) de definire a [expresiilor regulate în JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions). Vă va fi util în rezolvarea exercițiilor următoare pentru care trebuie să definiți pattern-uri de validare a conținutului câmpului unui formular. Nu trebuie să urmați tot tutorialul acum, dar e util să îl începeți și să reveniți la el când aveți nevoie să definiți expresii mai complexe.

## [space is the place!](https://www.youtube.com/watch?v=vHLOPBx2BaE)

Descărcați fișierele `form.html`, `style.css` și `form.js` din directorul `resources`. Sarcina voastră principală este să modificați fișierele HTML și JavaScript pentru a crea un formular pentru cererea de intrare în Sistemul Solar a vietăților extraterestre. Folosiți imaginea `screenshot.png` din directorul `resources` pentru a vă ghida în scrierea formularului. 

1. Adăugați atribute corespunzătoare elementului html `form`: formularul trebuie să folosească metoda `post` pentru comunicarea cu serverul, URL-ul să fie 'Earth', iar încărcarea răspunsului să fie în aceeași fereastră. 

## [multipass](https://www.youtube.com/watch?v=NVPLqbWXdDA)

2. Adăugați formularului o secțiune care să corespundă datelor personale ale vizitatorului extraterestru.  
Adăugați câte un câmp pentru: 
- nume (lungimea minimă a textului introdus să fie de 3 caractere, iar cea maximă de 30; câmp obligatoriu), 
- ID-ul unic intergalactic (lungime minimă 8, maximă 20; adăugați o verificare de pattern la alegere; câmp obligatoriu), 
- data nașterii (data cea mai recentă 13 mai 2024, cea mai veche 1 ianuarie 1800; câmp obligatoriu), 
- creditul social acumulat (interval între 0 și 2000 de puncte de credit; pasul să fie de 50 de credite; nu uitați să adăugați o etichetă cu valoarea selectată; câmp obligatoriu), 
- o fotografie (să fie acceptată orice extensie de fișier imagine), și
- rasă. Rasa poate fi una din următoarele: [Autobot](https://en.wikipedia.org/wiki/Autobot), [Daimons](https://en.wikipedia.org/wiki/Death_Busters#Daimons), [Deep Ones](https://en.wikipedia.org/wiki/Deep_One), [Experiment](https://en.wikipedia.org/wiki/List_of_Lilo_%26_Stitch_characters#Experiments), [Goa'uld](https://en.wikipedia.org/wiki/Mythology_of_Stargate#Goa'uld), [Hutt](https://en.wikipedia.org/wiki/Hutt_(Star_Wars)), [Jawa](https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(F%E2%80%93J)#Jawa), [Kryptonian](https://en.wikipedia.org/wiki/Krypton_(comics)), [Mandalorians](https://en.wikipedia.org/wiki/Mandalorians), [Martian](https://en.wikipedia.org/wiki/Mars_in_fiction#Life_on_Mars), [Protoss](https://en.wikipedia.org/wiki/StarCraft#Story), [Rodian](https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(P%E2%80%93T)#Rodian), [Romulan](https://en.wikipedia.org/wiki/Romulan), [Tleilaxu](https://en.wikipedia.org/wiki/Bene_Tleilax), [Vogon](https://en.wikipedia.org/wiki/Vogon), [Wookie](https://en.wikipedia.org/wiki/Wookiee), [Xenu](https://en.wikipedia.org/wiki/Xenu), [Yeti](https://en.wikipedia.org/wiki/Yeti_(Doctor_Who)), [Zerg](https://en.wikipedia.org/wiki/StarCraft#Story).  
*GEEK-OH!-METRU: Câte din tipurile de viață extraterestră de mai sus recunoașteți?*

Lista de opțiuni pentru câmpul corespunzător rasei este lungă (20 de opțiuni). Ce fel de element(e) html ar fi mai potrivit să folosim? Vă puteți gândi la o structurare mai bună a datelor? Propuneți o soluție alternativă de prezentare.

3. Adăugați formularului o secțiune care să corespundă datelor de contact ale oaspetelui. Ne interesează care este:
- galaxia din care provine (câmp obligatoriu)
- planeta natală (câmp obligatoriu)
- adresa completă (elementul textarea să nu poată fi redimensionat; câmp obligatoriu)
- numărul de telefon (câmp obligatoriu; folosiți un pattern de verificare a formatului intergalatic la alegere)
- adresa de email (câmp obligatoriu)
- URL-ul paginii web personale (câmp obligatoriu; folosiți un pattern la alegere)

*Care din aceste câmpuri ar putea fi redundante în contextul vizitelor speculative intergalactice?*

## [we're all different](https://www.youtube.com/watch?v=nSRwzP23ifI)

4. Adăugați formularului o secțiune pentru semnalmentele fizice ale vizitatorilor. Adăugați câmpuri pentru:

- înălțime (valori între 10 și 300 cm; câmp obligatoriu)
- greutate (valori între 1 și 500 kg; câmp obligatoriu)
- număr de membre (câmp obligatoriu)
- număr de ochi (câmp obligatoriu)
- culoare (hint: folosiți elementul html pentru selecția de culoare. Culoarea va fi ținută minte de la o vizită la alta a paginii; folosiți `localStorage`. De asemenea, la alegerea unei culori, culoarea de background a paginii se va modifica conform selecției)

## [just visiting](https://www.youtube.com/watch?v=KWMSpxTrfbo)

5. Adăugați formularului o secțiune pentru înregistrarea detaliilor legate de vizită:
- data sosirii (interval de 10 ani începând cu 13 mai 2024; câmp obligatoriu)
- ora estimată a sosirii (câmp obligatoriu)
- tipul de ședere (temporară sau permanentă; valoarea `temporară` preselectată; câmp obligatoriu)
- scopul vizitei (pot fi alese mai multe opțiuni; valoarea `invazie` preselectată; câmp obligatoriu)
- alte detalii legate de vizită.

## [the button](https://www.youtube.com/watch?v=Y0ZuNg17ZdU)

6. Adăugați un buton de trimitere a formularului. La apăsarea butonului se vor apela verificările adiționale (scrise în JavaScript) pentru conținutul câmpurilor. Dacă toate câmpurile sunt validate, înlocuiți formularul cu un mesaj care să anunțe trimiterea datelor. Go wild! (adăugați o imagine sau animație etc.)

## postform 

7. Modificați stilul CSS al formularului. Aliniați elementele, spațiați-le mai bine etc. 

8. Revedeți [lista de criterii]('https://alistapart.com/article/sensibleforms/') de urmat pentru crearea de formulare. Cât de bine structurat este formularul? Au fost folosite mereu cele mai potrivite elemente HTML? Cum ați împărți formularul altfel pentru a nu avea o listă prea lungă de câmpuri de completat pe o singură pagină?





