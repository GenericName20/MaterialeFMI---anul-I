1. Să se afișeze toate comenzile, împreună cu toți clienții care au plasat 
aceste comenzi și produsele pe care le-au comandat. 
Se vor afișa ID-ul comenzii, ID-ul clientului, data la care a fost plasată
comanda, numele clientului, dar și numele produsului și prețul acestuia. 
Se vor sorta rezultatele crescător, în funcție de ID-ul comenzii, și 
descrescător, în funcție de prețul pe care îl au produsele. 
De asemenea, se vor afișa toți clienții, chiar dacă aceștia nu au plasat 
comenzi. 

SELECT co.id_comanda, cl.id_client, cl.nume||' '||cl.prenume as nume_client, co.data, pa.nume, pa.pret
FROM 
    clienti cl
    FULL JOIN comenzi co ON (cl.id_client = co.id_comanda)
    LEFT JOIN produs_comanda pc ON (pc.id_comanda = co.id_comanda)
    LEFT JOIN produse_alimentare pa ON (pc.id_produs = pa.id_produs)
ORDER BY
    co.id_comanda ASC,
    pa.pret DESC;
    
    
2. Pentru fiecare comandă plasată, să se afișeze numărul de produse 
comandate. Se va afișa numărul de produse doar în cazul în care comanda 
conține mai mult de un produs. 
Se vor afișa ID-ul comenzii, data, ora, prețul total al comenzii și numărul 
total de produse comandate.

-- Selectează comenzile și numărul de produse comandate, având mai mult de una
WITH all_ordered_products AS (
    SELECT co.id_comanda, COUNT(pc.id_produs) as numar_produse_comandate
    FROM comenzi co LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
    GROUP BY co.id_comanda
    HAVING COUNT(pc.id_produs) > 1
)

SELECT aop.id_comanda, co.data, co.ora, co.pret_total, aop.numar_produse_comandate
FROM all_ordered_products aop
LEFT JOIN comenzi co ON (aop.id_comanda = co.id_comanda);


3. Pentru clientul care a plasat cele mai multe comenzi distincte, să se 
afișeze ID-ul și numele acestuia, precum și suma totală a comenzilor care 
conțin exact un singur produs. 

-- Numărul de comenzi plasate de fiecare client
WITH client_orders_count AS (
    SELECT id_client, COUNT(id_comanda) AS comenzi_plasate
    FROM comenzi
    GROUP BY id_client
),

-- Selectăm clientul care are cele mai multe comenzi
max_client_orders AS (
    SELECT id_client
    FROM client_orders_count
    WHERE comenzi_plasate = (SELECT MAX(comenzi_plasate) FROM client_orders_count)
),

-- Selectăm comenzile cu un singur produs, ale clientului maximal
max_client_orders_solo AS (
    SELECT co.id_comanda, COUNT(pc.id_produs) total_produse
    FROM comenzi co LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
    WHERE co.id_client = (SELECT * FROM max_client_orders)
    GROUP BY (co.id_comanda)
    HAVING COUNT(pc.id_produs) = 1
)

SELECT mco.id_client, cl.nume||' '||cl.prenume AS nume_complet, SUM(co.pret_total) AS pret_comenzi_un_produs
FROM max_client_orders mco
LEFT JOIN clienti cl ON mco.id_client = cl.id_client
LEFT JOIN comenzi co ON mco.id_client = co.id_client
RIGHT JOIN max_client_orders_solo mcos ON co.id_comanda = mcos.id_comanda
GROUP BY mco.id_client, cl.nume||' '||cl.prenume;


4. Să se afi?eze clienții care au comandat exclusiv produse din meniul 'Mic 
Dejun Clasic'. Aceștia nu trebuie să fi comandat niciun produs din alte 
meniuri, ci doar din meniul specificat. 

SELECT cl.id_client
FROM clienti cl
WHERE EXISTS (
    SELECT 1
    FROM comenzi co
    LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
    LEFT JOIN produse_alimentare pa ON (pc.id_produs = pa.id_produs)
    LEFT JOIN meniu me ON (pa.id_meniu = me.id_meniu)
    WHERE 
        co.id_client = cl.id_client
        AND me.titlu = 'Mic Dejun Clasic'
)
AND NOT EXISTS (
    SELECT 1
    FROM comenzi co
    LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
    LEFT JOIN produse_alimentare pa ON (pc.id_produs = pa.id_produs)
    LEFT JOIN meniu me ON (pa.id_meniu = me.id_meniu)
    WHERE 
        co.id_client = cl.id_client
        AND me.titlu != 'Mic Dejun Clasic'
);

SELECT cl.id_client, me.titlu
FROM clienti cl
LEFT JOIN comenzi co ON (cl.id_client = co.id_client)
LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
LEFT JOIN produse_alimentare pa ON (pc.id_produs = pa.id_produs)
LEFT JOIN meniu me ON (pa.id_meniu = me.id_meniu);

6. Să se afișeze, pentru fiecare client care a cheltuit în total mai mult 
decât media tuturor comenzilor, următoarele informații: id-ul clientului, 
numele și prenumele clientului, numărul total de produse comandate, suma totală
cheltuită de client, numărul de meniuri distincte din care a comandat produse. 
De asemenea, se vor afișa doar clien?ii care au plasat cel puțin două comenzi.

-- Selectez pe rând, fac join și iau id_client și ce mă mai interesează (grupez)
-- La final, dau join-uri pe id_client

-- Sumele cheltuite de clien?i
WITH all_spent_sums AS (
    SELECT id_client, SUM(pret_total) as suma_totala
    FROM comenzi
    GROUP BY id_client
),

-- Suma medie cheltuit?
average_sum AS (
    SELECT AVG(suma_totala) AS suma_medie
    FROM all_spent_sums
),

-- Clienții care au cheltuit peste medie (WHERE id_client IN above_average_clients)
above_average_clients AS (
    SELECT id_client
    FROM all_spent_sums
    WHERE suma_totala >= (SELECT suma_medie FROM average_sum)
),

-- Clienții care au plasat minim dou? comenzi
above_two_orders AS (
    SELECT cl.id_client
    FROM clienti cl LEFT JOIN comenzi co ON (cl.id_client = co.id_client)
    GROUP BY cl.id_client
    HAVING COUNT(co.id_comanda) >= 2
),

-- Numărul total de produse comandate
product_count AS (
    SELECT co.id_client, COUNT(pc.cantitate) as produse_comandate
    FROM comenzi co LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
    GROUP BY co.id_client
),

-- Numărul total de meniuri diferite
distinct_menus_count AS (
    SELECT co.id_client, COUNT(DISTINCT(pa.id_meniu)) as meniuri_distincte
    FROM 
        comenzi co 
        LEFT JOIN produs_comanda pc ON (co.id_comanda = pc.id_comanda)
        LEFT JOIN produse_alimentare pa ON (pc.id_produs = pa.id_produs)
    GROUP BY co.id_client
)

SELECT pc.id_client, cl.nume||' '||cl.prenume nume_client, pc.produse_comandate, ass.suma_totala, dmc.meniuri_distincte
FROM product_count pc
LEFT JOIN clienti cl ON (cl.id_client = pc.id_client)
LEFT JOIN all_spent_sums ass ON (pc.id_client = ass.id_client)
LEFT JOIN distinct_menus_count dmc ON (ass.id_client = dmc.id_client)
WHERE pc.id_client IN (SELECT * FROM above_average_clients);
