% Rezolvări de punctaj maxim (4/4)

% Minciunescu Vlad-Andrei
% Grupa 151

/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Problema I (1p)

Să se numere de câte ori apare fiecare element al unei liste nesortate.

*/

% Soluția I - Incompletă
% Sortez lista cu quicksort și fac compresie

quicksort([],[]).
quicksort([H|T],L) :- 
    split_qs(H,T,A,B), 
    quicksort(A,M),
    quicksort(B,N), 
    append(M,[H|N],L).

split_qs(_,[],[],[]).
split_qs(X,[H|T],[H|A],B) :- H < X, 
    split_qs(X,T,A,B).
split_qs(X,[H|T],A,[H|B]) :- H >= X, 
    split_qs(X,T,A,B).

encode(L1,L2) :- 
    pack(L1,L), 
    transform(L,L2).

pack([],[]).
pack([X | Xs], [Z | Zs]) :- 
    transfer(X, Xs, Ys, Z), !,
    pack(Ys, Zs).

transfer(X, [], [], [X]).
transfer(X, [Y | Ys], [Y | Ys], [X]) :- 
    X \= Y.
transfer(X, [X | Xs], Ys, [X | Zs]) :- 
    transfer(X, Xs, Ys, Zs), !.

transform([],[]).
transform([[X | Xs] | Ys],[(N, X)| Zs]) :- 
    length([X | Xs], N), 
    transform(Ys, Zs), !.

count_elements(List, X) :-
    quicksort(List, LSorted), !,
    encode(LSorted, X).

/*
Funcționează doar cu numere

1 ?- count_elements([1, 1, 2, 3, 1], R).
R = [(3, 1), (1, 2), (1, 3)].

*/


% Soluția 2 - Incompletă
% Fac o listă cu fiecare element și preiau lungimea fiecăreia.

count_elements_v2([], []).

count_elements_v2([H | T], [(Res, H) | R]) :-
    make_list_of(H, [H | T], L1),
    length(L1, Res),
    count_elements_v2(T, R), !.
    
make_list_of(X, [], []).

make_list_of(X, [X | T], [X | R]) :-
    make_list_of(X, T, R).

make_list_of(X, [H | T], R) :-
    make_list_of(X, T, R).

/*

Expected:
?- count_elements_v2([a, b, a, c, a, b], R).
R = [(3, a), (2, b), (1, c)].

Result:
1 ?- count_elements_v2([a, b, a, c, a, b], R). 
R = [(3, a), (2, b), (2, a), (1, c), (1, a), (1, b)] 

% Reverse și păstrate primele apariții (H, _) în R distincte.

*/

% Soluția 3 - Corectă
% Obțin elementele distincte și calculez de câte ori apare fiecare în lista originală

count_elements_v3([], []).
count_elements_v3(List, R) :-
    get_unique(List, L1), !,
    count_in_list(List, L1, R).

get_unique([], []).
get_unique([H | T], [H | R]) :-
    get_unique(T, R),
    \+ member(H, R), !.

get_unique([H | T], R) :- 
    get_unique(T, R),
    member(H, R), !.

count_in_list(List, [], []).
count_in_list(List, [H | T], [(X, H) | R]) :-
    count_freq(List, H, X),
    count_in_list(List, T, R).

count_freq([], F, 0) :- !.
count_freq([F | T], F, X1) :-
    count_freq(T, F, X), !,
    X1 is X + 1.

count_freq([_ | T], F, X) :-
    count_freq(T, F, X), !.

/*

Expected:
?- count_elements_v3([a, b, a, c, a, b], R).
R = [(3, a), (2, b), (1, c)].

Result:
3 ?- count_elements_v3([a, b, a, c, a, b], R). 
R = [(1, c), (3, a), (2, b)] ;
false.

*/

/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Problema 2 (1.5p)

Se dă o listă L formată din numere naturale.
Verificați dacă L poate fi rescrisă prin concatenarea a două liste L1 și L2, ambele în ordine crescătoare (și nevide).

?- inc_concat([1, 3, 5, 2, 4]).
true.
?- inc_concat([5, 4, 3, 2, 1]).
false.
?- inc_concat([1, 2, 3, 2, 3, 4]).
true.

*/

inc_concat(List) :-
    length(List, N),
    between(1, N, P),       % Pivotez lista pe 
                            % fiecare poziție de la 1 la N cu between

    split(List, P, List1, List2),       % Împart lista în două liste, 
                                        % înainte de și pe pivot, recursiv

    asc(List1), asc(List2), !.    % Verific dacă sunt crescătoare

asc([A]).
asc([A, B]) :- B > A, !.
asc([A, B | T]) :-
    B > A,
    asc([B | T]).

split(L, 0, [], L).
split([H | T], C, [H | L1], L2) :-
    C > 0,
    C1 is C - 1,
    split(T, C1, L1, L2).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Problema 3 (1.5p)

1p    I)    subformula(A, B) trebuie să fie adevărată dacă B este o subformulă a lui A (apare în A)
0.5p II)    proper_subformula(A, B) trebue să fie adevărată dacă B este o subformulă a lui A și este diferită de A

*/

% Subiectul I 

% Baza: orice formulă este subformulă a ei însăși
subformula(F, F).

% subformule pentru non(F)
subformula(non(F), S) :-
    subformula(F, S), !.

% subformule pentru si(F1, F2)
subformula(si(F1, F2), S) :-
    subformula(F1, S);
    subformula(F2, S), !.

% subformule pentru sau(F1, F2)
subformula(sau(F1, F2), S) :-
    subformula(F1, S);
    subformula(F2, S), !.

% Subpunctul II
proper_subformula(A, B) :-
    A \= B,
    subformula(A, B).


/*
Interogări I)

?- subformula(si(a, sau(b, c)), b).               
true.

?- subformula(non(non(a)), non(a)). 
true.

?- subformula(si(sau(a, b), si(a, c)), si(a, c)).
true.

?- subformula(sau(a, b), si(a, b)).    
false.

Interogări II)

?- proper_subformula(si(a, sau(b, c)), b).
true.

?- proper_subformula(non(non(a)), non(a)).
true.

?- proper_subformula(si(sau(a, b), si(a, c)), si(a, c)).
true.

?- proper_subformula(sau(a, b), si(a, b)).
false.

?- proper_subformula(sau(a, b), sau(a, b)).
false.

/*