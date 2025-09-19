% Rezolvări de punctaj maxim (4/4)

% :- consult('C:/Users/Dalv/swipl.rc'). % Load user config

% Ghita Vladut Adrian
% Grupa 151

% Subiectul NR1

% Exercitiul 1
expand_intervals([], []).
expand_intervals([(Left, Right)|T], [R|Tr]) :- 
     expand_interval((Left, Right), R),
     expand_intervals(T, Tr).

expand_interval((A, A), [A]).
expand_interval((A, B), []) :- B < A.
expand_interval((A, B), [A|Tr]) :- A < B, A1 is A + 1, expand_interval((A1, B), Tr).





% Exercitiul 2
diferite(L, R) :- 
    length(L, L1), length(R, R1), L1 \== R1.
diferite([H1|_], [H2|_]) :- H1 \== H2.
diferite([H|T1], [H|T2]) :- diferite(T1, T2).

split([], _, [], []).
split([A|Ta], 0, [], [A|T2]) :- split(Ta, 0, [], T2).
split([A|Ta], N, [A|T1], L2) :- N > 0, N1 is N - 1, split(Ta, N1, T1, L2).
rotate([], _, []).
rotate(L, 0, L). 
rotate(L, N, R) :- N < 0, rotate_negative(L, N, R).
rotate(L, N, R) :- N > 0, rotate_positive(L, N, R).
rotate_positive(L, N, R) :- length(L, Len), N =< Len, split(L, N, L1, L2), append(L2, L1, R).
rotate_negative(L, N, R) :- length(L, Len), NP is Len + N, rotate_positive(L, NP, R).

% Rotate este practic o permutare cilculara care are acelasi comportament ca L1 si L2 din enunt
div_concat(L, R) :- 
    length(L, Len),
    Len1 is Len - 1,
    between(1, Len1, N), % Cautam acel N pentru a 'split-ui' L in L1 si L2 care sa fie divizibil cu una dintre liste
    rotate_positive(L, N, R), 
    length(L, Len), Mod is Len / N, integer(Mod),
    diferite(L, R). % Cam redundant, pentru ca permutarea este limitata la Len-1
div_concat(L, R) :- 
    length(L, Len), 
    Len1 is Len - 1,
    between(1, Len1, N), % Cautam acel N pentru a 'split-ui' L in L1 si L2 care sa fie divizibil cu cealalta dintre liste
    rotate_positive(L, N, R), 
    length(L, Len), InvLen is Len - N, Mod is Len / InvLen, integer(Mod),
    diferite(L, R).% Cam redundant, pentru ca permutarea este limitata la Len-1





% Exercitiul 3
vars(A, [A]) :- atom(A).
vars(si(A, B), R) :- vars(A, R1), vars(B, R2), append(R1, R2, R). 

doar_si_si_var(A) :- atom(A).
doar_si_si_var(si(A, B)) :- doar_si_si_var(A), doar_si_si_var(B).

% Punctul a
% Varianta 1: Functioneaza si pentru assoc_and(expresie, NECUNOSCUT)
assoc_and(A, A) :- atom(A).
assoc_and(si(A, B), si(A, B)) :- atom(A), atom(B).

assoc_and(si(si(A, B), C), si(A, si(B, C))) :- atom(A), atom(B), atom(C).
assoc_and(si(A, si(B, C)), si(si(A, B), C)) :- atom(A), atom(B), atom(C).
assoc_and(si(si(A, B), si(C, D)), si(A, si(B, si(C, D)))) :- atom(A), atom(B), atom(C).

assoc_and(si(si(A, B), C), si(A, si(B, C))) :- 
    doar_si_si_var(A), doar_si_si_var(B), doar_si_si_var(C).
assoc_and(si(A, si(B, C)), si(si(A, B), C)) :- 
    doar_si_si_var(A), doar_si_si_var(B), doar_si_si_var(C).

assoc_and(si(si(A, B), si(C, D)), si(A, si(B, si(C, D)))) :- 
    doar_si_si_var(A), doar_si_si_var(B), doar_si_si_var(C), doar_si_si_var(D).

assoc_and(si(A, B), si(C, D)) :-
    doar_si_si_var(A), doar_si_si_var(B), doar_si_si_var(C), doar_si_si_var(D),
    not(atom(A)), not(atom(B)), not(atom(C)), not(atom(D)),
    assoc_and(A, C).

assoc_and(si(A, B), si(C, D)) :-
    doar_si_si_var(A), doar_si_si_var(B), doar_si_si_var(C), doar_si_si_var(D),
    not(atom(A)), not(atom(B)), not(atom(C)), not(atom(D)),
    assoc_and(B, D).

% Varianta 2: Nu functioneaza pentru assoc_and(expresie, NECUNOSCUT), cauta la nesfarsit, dar este o solutie mai scurta
assoc_and(A, A) :- atom(A).
assoc_and(Phi, Psi) :- doar_si_si_var(Phi), doar_si_si_var(Psi), vars(Phi, V), vars(Psi, V).



% Punctul b
assoc_and_right(Phi, Psi) :- doar_si_si_var(Phi), vars(Phi, Vars), make_right_assoc(Vars, Psi).

make_right_assoc([A, B], si(A, B)).
make_right_assoc([A, B|T], si(A, C)) :- make_right_assoc([B|T], C).