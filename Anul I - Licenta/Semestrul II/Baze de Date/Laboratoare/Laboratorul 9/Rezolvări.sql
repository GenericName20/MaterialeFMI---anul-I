-- LABORATOR 9 - SĂPTĂMÂNA 13

EX: Să se obțină codurile salariaților atașați tuturor proiectelor 
pentru care s-a alocat un buget egal cu 10000.

SELECT * FROM PROJECT; -- p2 și p3 proiecte cu buget de 10k
SELECT * FROM WORKS_ON; -- 101, 145, 148, 200 
                   --> angajații care lucrează la TOATE proiectele cu buget de 10k

!!! Toate proiectele înseamnă că angajații să lucreze OBLIGATORIU 
la TOATE proiectele cu buget de 10k (la toate - p2 și p3), 
dar și la alte proiecte cu un alt buget.

--Metoda 1 (utilizând de 2 ori NOT EXISTS):

SELECT	DISTINCT employee_id
FROM works_on a -- preluăm toți employee_id din tabela works_on, 
                -- dar numai pe aceia pentru care NU există niciun proiect             
                -- cu buget de 10 000 la care să nu lucreze
                
WHERE NOT EXISTS   -- primul NOT EXISTS (relația universală)
                   -- această condiție filtrează toți angajații care lucrează 
                   -- la toate proiectele cu buget de 10000
                   -- Dacă există măcar un proiect cu buget 10000 
                   -- la care angajatul nu lucrează, acel angajat este exclus
         (SELECT 1
          FROM	project p
          WHERE	budget = 10000
          AND NOT EXISTS   -- are loc verificarea efectivă
                           -- se verifică dacă angajatul curent a.employee_id 
                           -- este atașat proiectului p.project_id
                           -- Dacă nu este, înseamnă că acel proiect îl descalifică 
                           -- deci excludem acel angajat din afișare
                (SELECT	'x'
                 FROM works_on b
                 WHERE p.project_id = b.project_id
                 AND b.employee_id = a.employee_id
                 ) 
          ); 
          
---------------------------------------------------
DIVISION - succesiune de 2 operatori not exists => 
         => Împărțim în două relații:

angajați lucrează la proiecte
proiectele au buget de 10k
----------------------------------------------------


   
--Metoda 2 (simularea diviziunii cu ajutorul funcției COUNT):

SELECT employee_id
FROM works_on
WHERE project_id IN
                (SELECT	project_id
                 FROM  	project
                 WHERE	budget = 10000
                 )
GROUP BY employee_id
HAVING COUNT(project_id)=
                (SELECT COUNT(*)
                 FROM project
                 WHERE budget = 10000
                 );
 
                 
-- EXERCIȚII DIVISION:
  
                 
8.	Să se afișeze lista angajaților care au lucrat numai pe proiecte 
conduse de managerul de proiect având codul 102.

select * from project;  -- managerul 102 conduce două proiecte => p1 și p3

select * from works_on; -- angajații care lucrează NUMAI pe proiecte coduse de 102 => 
                        -- 136, 140, 150, 162, 176
                     
                        
-- Selectăm angajații care lucrează la cel puțin unul dintre proiectele conduse de PM = 102
SELECT employee_id
FROM works_on
WHERE project_id IN (
        -- Selectăm proiectele conduse de PM = 102
        SELECT project_id
        FROM project
        WHERE project_manager = 102
        )
-- și scădem angajații care lucrează la alte proiecte în afara celor selectate
MINUS

SELECT employee_id
FROM works_on
WHERE project_id NOT IN (
        -- Selectăm proiectele conduse de PM = 102
        SELECT project_id
        FROM project
        WHERE project_manager = 102
        );


9.	a) Să se obțină numele angajaților care au lucrat 
cel puțin pe aceleași proiecte ca și angajatul având codul 200.

select * from works_on; -- ang 200 lucrează la p2 și p3
SELECT first_name||' '||last_name as "Nume angajat"
FROM employees
WHERE employee_id IN 
    (SELECT employee_id
    FROM works_on
    WHERE project_id IN (
            SELECT project_id
            FROM works_on
            WHERE employee_id = 200
        ) AND employee_id != 200
    GROUP BY employee_id
    HAVING COUNT(project_id) = (
        SELECT COUNT(*)
        FROM works_on
        WHERE
        employee_id = 200
        )
    );    


b) Să se obțină numele angajaților care au lucrat cel mult pe aceleași proiecte 
ca și angajatul având codul 200.

SELECT employee_id as "ID angajat", first_name||' '||last_name as "Nume angajat"
FROM employees
WHERE employee_id IN (
    SELECT employee_id
    FROM works_on
    WHERE project_id IN (
        SELECT project_id
        FROM works_on
        WHERE employee_id = 200
        ) 
        AND employee_id != 200
    
    MINUS 
    
    SELECT employee_id
    FROM works_on
    WHERE project_id NOT IN (
        SELECT project_id
        FROM works_on
        WHERE employee_id = 200
    )
);    

=> 101 (la ambele)
   145 (la ambele) 
   148 (la ambele)
   150 (doar p3)
   162 (doar p3)
   176 (doar p3)



10. Să se obțină angajații care au lucrat exact pe aceleași proiecte 
ca și angajatul având codul 200.

SELECT employee_id
FROM works_on
WHERE employee_id != 200 -- Eliminăm angajatul 200 din selecție
AND project_id IN (
        -- Selectăm proiectele la care a lucrat angajatul cu ID 200
        SELECT project_id
        FROM works_on
        WHERE employee_id = 200
    )
-- Ne asigurăm că au lucrat la exact aceleași proiecte
GROUP BY(employee_id)
HAVING COUNT(project_id) = (
        SELECT COUNT(*)
        FROM works_on
        WHERE employee_id = 200
    );


-- EXERCIȚII DIVERSE:


1. Să se listeze informații despre angajații care au lucrat în toate proiectele 
demarate în primele 6 luni ale anului 2006.

-- Selectăm angajații care au lucrat în măcar un proiect din subselecție
WITH ANGAJATI_ACTIVI AS (
    SELECT employee_id
    FROM works_on
    WHERE project_id IN (
        -- Selectăm proiectele demarate în primele 6 luni ale anului
        SELECT project_id
        FROM project
        WHERE EXTRACT(year FROM start_date) = 2006 AND EXTRACT(month FROM start_date) <= 6
        )
    GROUP BY(employee_id)
    HAVING COUNT(project_id) = ( -- Același angajat trebuie să fi lucrat la toate proiectele
            -- Numărăm proiectele demarate în primele 6 luni ale anului
            SELECT COUNT(project_id)
            FROM project
            WHERE EXTRACT(year FROM start_date) = 2006 AND EXTRACT(month FROM start_date) <= 6
        )
)
    SELECT *
    FROM employees
    WHERE employee_id IN ( 
        SELECT employee_id 
        FROM ANGAJATI_ACTIVI
    );
_____ 


2.	Să se listeze informații despre proiectele la care au participat toți angajații 
care au deținut alte 2 posturi în firmă.

-- Afișăm detalii despre proiectele care se identifică în subselecție
SELECT *
FROM project
WHERE project_id IN (
    -- Selectăm proiectele la care au participat angajații care respectă condiția
    SELECT DISTINCT(project_id)
    FROM works_on
    WHERE employee_id IN (
        -- Selectăm toți angajații care au avut alte 2 posturi în firmă
        SELECT employee_id
        FROM job_history
        GROUP BY (employee_id)
        HAVING COUNT(employee_id) = 2
        )
    );


_____


3.	Să se obțină numărul de angajați care au avut cel puțin trei job-uri, 
luându-se în considerare și job-ul curent.

-- cel puțin 3 joburi cu jobul curent înseamnă că în job_history să aibă cel puțin două 
-- acolo este istoricul joburilor trecute
SELECT COUNT(*) as "Numărul de angajați care au avut cel puțin 3 job-uri"
FROM (
    SELECT employee_id
    FROM job_history
    GROUP BY(employee_id)
    HAVING COUNT(employee_id) >= 2
);

_____


4.	Pentru fiecare țară, să se afișeze numărul de angajați din cadrul acesteia.

-- Selectăm toți angajații și obținem informații despre locațiile în care lucrează
SELECT l.country_id as "Țara", COUNT(e.employee_id) as "Angajați"
FROM employees e LEFT JOIN departments d ON (e.department_id = d.department_id)
                 RIGHT JOIN locations l ON (d.location_id = l.location_id)
GROUP BY(l.country_id);
_____
   

5.	Să se listeze codurile angajaților și codurile proiectelor pe care au lucrat. 
Listarea va cuprinde și angajații care nu au lucrat pe niciun proiect.

SELECT e.employee_id as "Cod angajat", NVL(TO_CHAR(w.project_id), 'Nu a lucrat') as "Cod proiect"
FROM works_on w RIGHT JOIN employees e ON (w.employee_id = e.employee_id);

______


6.	Să se afișeze angajații care lucrează în același departament 
cu cel puțin un manager de proiect.

-- Selectăm angajații care lucrează în departamentele selectate în subselecție
SELECT employee_id
FROM employees
WHERE department_id IN (
    -- Selectăm departamentele în care lucrează project managerii
    SELECT department_id
    FROM employees
    WHERE employee_id IN (
        -- Selectăm toți project managerii distincți
        SELECT DISTINCT(project_manager)
        FROM project
    )
);

SELECT * FROM employees;


_____


7.	Să se afișeze angajații care nu lucrează în același departament 
cu niciun manager de proiect.

-- Selectăm angajații care nu lucrează în departamentele selectate în subselecție
SELECT employee_id
FROM employees
WHERE department_id NOT IN (
    -- Selectăm departamentele în care lucrează project managerii
    SELECT department_id
    FROM employees
    WHERE employee_id IN (
        -- Selectăm toți project managerii distincți
        SELECT DISTINCT(project_manager)
        FROM project
    )
);

