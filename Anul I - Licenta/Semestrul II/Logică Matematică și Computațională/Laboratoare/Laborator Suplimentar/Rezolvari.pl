nil                          % arbore vid
tree(Val, Left, Right)      % nod cu valoare și doi subarbori

% Inserarea într-un BST
bt_ins(X, nil, tree(X, nil, nil)).  % inserare într-un arbore vid

bt_ins(X, tree(X, L, R), tree(X, L, R)).  % X deja există, nu îl inserăm din nou

bt_ins(X, tree(Y, L, R), tree(Y, NewL, R)) :- 
    X < Y, 
    bt_ins(X, L, NewL).

bt_ins(X, tree(Y, L, R), tree(Y, L, NewR)) :- 
    X > Y, 
    bt_ins(X, R, NewR).



% Construirea unui BST dintr-o listă
bt_list([], nil).

bt_list([H|T], Tree) :-
    bt_list(T, SubTree),
    bt_ins(H, SubTree, Tree).

% Sortare cu BST
bt_sort(List, Sorted) :-
    bt_list(List, Tree),
    inorder(Tree, Sorted).

inorder(nil, []).

inorder(tree(X, L, R), Sorted) :-
    inorder(L, SL),
    inorder(R, SR),
    append(SL, [X|SR], Sorted).


/*

?- bt_sort([3, 1, 4, 1, 5, 9, 2], Sorted).
Sorted = [1, 1, 2, 3, 4, 5, 9].

*/

% Smart list reverse
reva(L,R) :- revah(L,[],R).
revah([], R, R).
revah([H|T], S, N) :- revah(T,[H|S],N).

% deci Difference list:
revd(L,R) :- revdh(L,(R,[])).
revdh([],(R,R)).
revdh([H|T],(N,S)) :- revdh(T,(N,[H|S]))

% Aplatizarea unei liste
flatten([], []).

flatten([H|T], flatList) :-
    is_list(H), !,
    flatten(H, FH),
    flatten(T, FT),
    append(FH, FT, flatList).

flatten([H|T], [H|FT]) :-
    flatten(T, FT).


% Aplatizarea unei liste cu Difflists
flatten_dl(Xs, Ys) :-
    flatten_dl(Xs, Ys-[]).

flatten_dl([], L-L).

flatten_dl([H|T], L-R) :-
    is_list(H), !,
    flatten_dl(H, L-M),
    flatten_dl(T, M-R).

flatten_dl([H|T], [H|M]-R) :-
    flatten_dl(T, M-R).

flatten_dl_wrapper(Xs, Ys) :- flatten_dl(Xs, Ys).

/* Interogări
?- flatten([1,2,[3,a],[[7],2],5], L).
L = [1, 2, 3, a, 7, 2, 5].

?- flatten_dl_wrapper([1,2,[3,a],[[7],2],5], L).
L = [1, 2, 3, a, 7, 2, 5].

*/

% quicksort_dl(+Lista, -ListaSortata)
% Wrapper pentru a converti lista diferențială în listă normală
quicksort_dl(L, Sorted) :-
    quicksort_dl(L, Sorted-[]).

% quicksort_dl(+Lista, -Difflist)
% Caz de bază: lista goală
quicksort_dl([], R-R).

% Caz general: partajăm și sortăm recursiv
quicksort_dl([H|T], R1-R3) :-
    split(H, T, Less, Greater),
    quicksort_dl(Less, R1-R2),
    R2 = [H|Rmid],
    quicksort_dl(Greater, Rmid-R3).

% split(+Pivot, +List, -Less, -GreaterOrEqual)
split(_, [], [], []).

split(X, [H|T], [H|A], B) :-
    H < X,
    split(X, T, A, B).

split(X, [H|T], A, [H|B]) :-
    H >= X,
    split(X, T, A, B).


% Gramatici
sent(R) :- np(A), vp(B), append(A,B,R).
np(R) :- dete(A), n(B), append(A,B,R).
vp(R) :- tv(A), np(B), append(A,B,R).
vp(R) :- v(R).

% Determinanți 
dete([the]). dete([a]). dete([every]).

% Substantive / nouns
n([teacher]). n([doctor]). n([park]).

% Verbe tranzitive
tv([likes]). v([walks]).


% Si gramatica + difflists
sentd(R) :- sentdh((R,[])).
sentdh((R,S)) :- npdh((R,Z)), vpdh((Z,S)).
npdh((R,S)) :- detedh((R,Z)), ndh((Z,S)).
vpdh((R,S)) :- tvdh((R,Z)), npdh((Z,S)).
vpdh((R,S)) :- vdh((R,S)).
detedh(([the|S],S)). detedh(([a|S],S)).
detedh(([every|S],S)).
ndh(([teacher|S],S)). ndh(([doctor|S],S)).
ndh(([park|S],S)).
tvdh(([likes|S],S)). vdh(([walks|S],S)).


% Gramatică default
% ?- sentgh(R,[]).
% ?- phrase(sentgh,R).

% Caz de bază: lista goală are 0 a-uri → par
parA([], []).

% Dacă întâlnim un 'a', inversăm paritatea → mergem în impA
parA([a|T], R) :-
    impA(T, R).

% Dacă întâlnim un 'b', nu afectează paritatea → rămânem în parA
parA([b|T], R) :-
    parA(T, R).

% Stare intermediară: număr impar de 'a'-uri
impA([a|T], R) :-
    parA(T, R).  % alt 'a' → revenim la paritate pară

impA([b|T], R) :-
    impA(T, R).

% a la N b la N

an_bn([], []).  % cazul de bază: șirul gol e valid

an_bn([a|T1], L2) :-
    an_bn(T1, [b|T2]),
    L2 = T2.



