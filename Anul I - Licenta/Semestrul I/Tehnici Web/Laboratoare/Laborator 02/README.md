# Laborator 2 - html

*Folosiți notele de curs ca să vă amintiți principalele elemente de HTML și rezolvați următoarele exerciții.*  

În directorul *resources* puteți găsi două screenshoturi ale unor pagini web: `index-screenshot.png` și `mario-screenshot.png`. Sarcina voastră este să reproduceți paginile din imagini folosind celelalte resurse disponibile (imagini și text) și urmând instrucțiunile de mai jos. 

## index.html 

1. Stabiliți structura generală a fișierului, ținând cont de faptul că pagina are trei părți principale: header, conținut propriu-zis, și footer. Conținutul este împărțit la rândul său în trei: 8-bit games, 8-bit graphics, 8-bit music. Alegeți elementele HTML de structurare potrivite (`header`, `h1`-`h6`, `section`, `article` etc.).

2.  Adăugați conținutul headerului: titlul, "8-bit world", și meniul (*hint: folosiți elementul HTML de navigare potrivit*). 

3. Adăugați conținutul primei părți, 8-bit games:

- Folosiți o listă ordonată pentru topul celor mai populare jocuri. Adăugați o hiperlegătură către pagina `mario.html`, pe care o veți scrie pentru a rezolva exercițiile 6-9.
- Folosiți elementul `iframe` pentru a integra modulul de programare pentru NES. 

4. Adăugați conținutul celei de-a doua părți, 8-bit graphics:

- Folosiți elementul HTML `figure` pentru a include imaginea `256colour.png`. 
- Folosiți o listă neordonată pentru a enumera principalele aplicații ale graficii pe 8 biți. 
- Jucați-vă cu [make8bitart](https://make8bitart.com/) și cu [8bitworkshop](https://8bitworkshop.com/dithertron) într-un exces de inspirație de 8 biți. :-)
- Atenție la integrarea celor două clipuri de youtube. Ce element HTML ar fi mai potrivit? `Video` sau `iframe`?

5. Adăugați și conținutul ultimei părți, 8-bit music. Jucați-vă cu playerul [Commodore64](https://www.igorski.nl/application/websid/) pentru a recrea muzica din jocul 8-bit preferat. :-) 

## mario.html
6.  Stabiliți structura generală a fișierului `mario.html`. *Hint: folosiți elementele `section` și `article`.*
7. Soundtrackul este disponibil [aici](https://downloads.khinsider.com/game-soundtracks/album/super-mario-bros/01.%2520Ground%2520Theme.mp3). Salvați-l pe calculator și integrați-l folosind elementul `audio`.
8. Pentru definirea tabelului, folosiți atributele `rowspan` și `colspan` ale elementelor `th` și `td`.
9. Jucați-vă Super Mario Bros! 

## EXTRA

10. Citiți [aici](https://www.onrec.com/news/news-archive/what-is-8-bit-graphics-and-how-it%E2%80%99s-used-nowadays) mai multe despre grafica pe 8 biți. Se mai folosește cu adevărat în zilele noastre? De ce?
11. Ce se întâmplă când ajungi la nivelul 256 al jocului Pac-Man? De ce nu putea Link să strângă mai mult de 255 de rupii în Legend of Zelda?  
12. Adăugați paginilor HTML și alt conținut interesant despre lumea pe 8 biți.

