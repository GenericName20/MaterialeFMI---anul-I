/*

ACEST DOCUMENT CONȚINE REZOLVĂRILE PROBLEMELOR
- DE PE 99 PROLOG PROBLEMS! ATENȚIE LA DEPENDENȚE!
- DIN MODELELE 2022/2023, 2025 și MODELUL DE COLOCVIU 2025
- ALTE CÂTEVA PROBLEME INVENTATE, UTILE ÎN ÎNȚELEGEREA MATERIEI.


@vlaxcs >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

1. Find the last element from a list

?- my_last(X, [1, 2, 3, 4, 5]).
X = 5 ;

*/

my_last(X, [H]) :- X is H.
my_last(X, [_ | T]) :- my_last(X, T).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

2. The last to one element from a list (penultimul)

?- tibo(X, [1, 2, 3, 4, 5]).   
X = 4

*/

tibo(X, [H | T]) :- length(T, 1), X is H.
tibo(X, [_ | T]) :- tibo(X, T).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

3. K-th element

?- element_at(X, [1, 2, 3, 4, 5], 3).
X = 3

?- element_at(X, [1, 2, 3, 4, 5], 6). 
false.

*/

element_at(X, [H | _], 1) :- X is H.
element_at(X, [H | T], P) :- Next is P - 1, element_at(X, T, Next). 



% 4. The number of elements of a list
% alternative: length(List, N).

find_in(How_Many, [], P) :- How_Many is P.
find_in(How_Many, [H | T], P) :-
    Next is P + 1,
    find_in(How_Many, T, Next).

count_in(How_Many, [H | T]) :-
    find_in(How_Many, [H | T], 0).



% 5. Reverse a list

reverse_list(ToReverse, Result) :-
    my_rev(ToReverse, Result, []).

my_rev([], Result, Result).
my_rev([H | T], Result, X) :-
    my_rev(T, Result, [H | X]).



% 6. Palindrome

is_palindrome(List) :-
    reverse(List, List).



% 7. Flatten

flatten(H, [H]) :- \+ is_list(H).
flatten([], []).
flatten([H | T], Result) :- 
    flatten(H, NewH), 
    flatten(T, NewT), 
    append(NewH, NewT, Result).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

8. Duplicates / Compresie

?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [a,b,c,a,d,e]

compress([], []).
compress([X], [X]).
compress([Current, Current | T], X) :-
    compress([Current | T], X).
compress([Current, Next | T], [Current | T2]) :-
    compress([Next | T], T2).

*/



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P09 (**):  Pack consecutive duplicates of list elements into sublists.

pack(L1,L2) :- the list L2 is obtained from the list L1 by packing
    repeated occurrences of elements into separate sublists.
    (list,list) (+,?)

?- pack([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]] 

*/

pack([],[]).
pack([X | Xs], [Z | Zs]) :- 
    transfer(X, Xs, Ys, Z), 
    pack(Ys, Zs).

%   transfer(X,Xs,Ys,Z) 
%   Ys is the list that remains from the list Xs
%   when all leading copies of X are removed and transfered to Z

transfer(X, [], [], [X]).
transfer(X, [Y | Ys], [Y | Ys], [X]) :- 
    X \= Y.
transfer(X, [X | Xs], Ys, [X | Zs]) :- 
    transfer(X, Xs, Ys, Zs).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P10 (*):  Run-length encoding of a list

encode(L1,L2) :-    the list L2 is obtained from the list L1 by run-length
                    encoding. Consecutive duplicates of elements are encoded as terms [N,E],
                    where N is the number of duplicates of the element E.
                    (list,list) (+,?)


?- encode([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],[1,b],[2,c],[2,a],[1,d][4,e]]

:- ensure_loaded(p9).
*/

encode(L1,L2) :- 
    pack(L1,L), 
    transform(L,L2).

transform([],[]).
transform([[X | Xs] | Ys],[[N, X]| Zs]) :- 
    length([X | Xs], N), 
    transform(Ys, Zs).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P11 (*):  Modified run-length encoding

encode_modified(L1,L2) :- the list L2 is obtained from the list L1 by 
run-length encoding. Consecutive duplicates of elements are encoded 
as terms [N,E], where N is the number of duplicates of the element E.
However, if N equals 1 then the element is simply copied into the 
output list.
(list,list) (+,?)

?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],b,[2,c],[2,a],d,[4,e]]
    
:- ensure_loaded(p10).
*/

encode_modified(L1,L2) :- encode(L1,L), strip(L,L2).

strip([],[]).
strip([[1,X]|Ys],[X|Zs]) :- strip(Ys,Zs).
strip([[N,X]|Ys],[[N,X]|Zs]) :- N > 1, strip(Ys,Zs).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P13 (**): Run-length encoding of a list (direct solution) 

encode_direct(L1,L2) :- the list L2 is obtained from the list L1 by 
    run-length encoding. Consecutive duplicates of elements are encoded 
    as terms [N,E], where N is the number of duplicates of the element E.
    However, if N equals 1 then the element is simply copied into the 
    output list.
    (list,list) (+,?)

?- encode_direct([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],b,[2,c],[2,a],d,[4,e]]

*/

encode_direct([],[]).
encode_direct([X|Xs],[Z|Zs]) :- count(X,Xs,Ys,1,Z), encode_direct(Ys,Zs).

%   count(X,Xs,Ys,K,T) Ys is the list that remains from the list Xs
%    when all leading copies of X are removed. T is the term [N,X],
%    where N is K plus the number of X's that can be removed from Xs.
%    In the case of N=1, T is X, instead of the term [1,X].

count(X,[],[],1,X).
count(X,[],[],N,[N,X]) :- N > 1.
count(X,[Y|Ys],[Y|Ys],1,X) :- X \= Y.
count(X,[Y|Ys],[Y|Ys],N,[N,X]) :- N > 1, X \= Y.
count(X,[X|Xs],Ys,K,T) :- K1 is K + 1, count(X,Xs,Ys,K1,T).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P14 (*) Duplicate the elements of a list.

?- dupli([a,b,c,c,d],X).
X = [a,a,b,b,c,c,c,c,d,d]

*/

dupli([], []).
dupli([H | T], [H, H | X]) :-
    dupli(T, X).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P15 (**) Duplicate the elements of a list a given number of times.
Example:
?- dupli([a,b,c],3,X).
X = [a,a,a,b,b,b,c,c,c]

What are the results of the goal:
?- dupli(X,3,Y).

*/

dupli([], _, []).
dupli([H | T], C, X) :-
    dupli(T, C, X1),
    multiple(H, C, Result),
    append(Result, X1, X).

multiple(_, 0, []).
multiple(H, C, [H | Result]) :-
    C > 0,
    C1 is C - 1,
    multiple(H, C1, Result).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P16 (**) Drop every N'th element from a list.
Example:
?- drop([a,b,c,d,e,f,g,h,i,k],3,X).
X = [a,b,d,e,g,h,k]

*/

drop(List, C, Result) :-
    keep_drop(List, C, C, Result).

keep_drop([], _, _, []).
keep_drop([H | T], Current, Limit, [H | Result]) :-
    Current > 1,
    Next is Current - 1,
    keep_drop(T, Next, Limit, Result).

keep_drop([H | T], 1, Limit, Result) :-
    keep_drop(T, Limit, Limit, Result).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P17 (*) Split a list into two parts; the length of the first part is given.
Do not use any predefined predicates.

Example:
?- split([a,b,c,d,e,f,g,h,i,k],3,L1,L2).
L1 = [a,b,c]
L2 = [d,e,f,g,h,i,k]

*/

split(L, 0, [], L).
split([H | T], C, [H | L1], L2) :-
    C > 0,
    C1 is C - 1,
    split(T, C1, L1, L2).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P18 (**) Extract a slice from a list.
Given two indices, I and K, the slice is the list containing the elements between the I'th and K'th element of the original list (both limits included). Start counting the elements with 1.

Example:
?- slice([a,b,c,d,e,f,g,h,i,k],3,7,L).
X = [c,d,e,f,g]

*/

slice(List, I, J, L) :-
    J1 is J + 1,
    slice(List, 1, I, J1, L).

slice(L, J, I, J, []).
slice([H | T], C, I, J, [H | L]) :-
    C >= I,
    C < J,
    C1 is C + 1,
    slice(T, C1, I, J, L).
slice([H | T], C, I, J, L) :-
    C < I,
    C1 is C + 1,
    slice(T, C1, I, J, L).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P19 (**) Rotate a list N places to the left.

?- rotate([a,b,c,d,e,f,g,h],3,X).
X = [d,e,f,g,h,a,b,c]

?- rotate([a,b,c,d,e,f,g,h],-2,X).
X = [g,h,a,b,c,d,e,f]

*/

rotate(L1, P, L2) :-
    P >= 0,
    length(L1, Len1),
    N1 is P mod Len1,
    rotate_left(L1, N1, L2). 

rotate(L1, P, L2) :-
    P < 0,
    length(L1, Len1),
    N1 is Len1 + (P mod Len1),
    rotate_left(L1, N1, L2).    % From behind

rotate_left(L,0,L).
rotate_left(L1,N,L2) :- 
    N > 0, 
    split(L1,N,S1,S2), 
    append(S2,S1,L2).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P20 (*) Remove the K'th element from a list.
Example:
?- remove_at(X,[a,b,c,d],2,R).
X = b
R = [a,c,d]

*/

remove_at(H, [H | L], 1, L).
remove_at(X, [H | T], K, [H | R]) :-
    K > 1,
    K1 is K - 1,
    remove_at(X, T, K1, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P21 (*) Insert an element at a given position into a list.
Example:
?- insert_at(alfa,[a,b,c,d],2,L).
L = [a,alfa,b,c,d]

*/

insert_at(X, T, 1, [X | T]).
insert_at(X, [H | T], K, [H | R]) :-
    K > 1,
    K1 is K - 1,
    insert_at(X, T, K1, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P22 (*) Create a list containing all integers within a given range.
Example:
?- range(4,9,L).
L = [4,5,6,7,8,9]

*/

range(I, J, []) :- I > J. % From start, if I > J, the list is empty
range(J, J, [J]).
range(I, J, [I | L]) :-
    I < J,
    I1 is I + 1,
    range(I1, J, L).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Examen:

EX1. Expand intervals

?- expand([(1, 4), (2,1), (5, 9)], X).

*/

expand([], []).
expand([(I, J) | T], [L | R]) :-
    range(I, J, L),
    expand(T, R).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P23 (**) Extract a given number of randomly selected elements from a list.
The selected items shall be put into a result list.
Example:
?- rnd_select([a,b,c,d,e,f,g,h],3,L).
L = [e,d,a]

*/

rnd_select(_, 0, []).
rnd_select(List, C, [X | L]) :-
    C > 0,
    C1 is C - 1,
    length(List, R),
    random(0, R, P),
    remove_at(X, List, P, Result),
    rnd_select(Result, C1, L).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P24 (*) Lotto: Draw N different random numbers from the set 1..M.
The selected numbers shall be put into a result list.
Example:
?- rnd_select_lotto(6,49,L).
L = [23,1,17,33,21,37]

*/

rnd_select_lotto(X, Y, Result):-
    range(1, Y, L),
    rnd_select(L, X, Result).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P25 (*) Generate a random permutation of the elements of a list.
Example:
?- rnd_permu([a,b,c,d,e,f],L).
L = [b,a,d,c,e,f]

*/

rnd_permu(List, Result):-
    length(List, N),
    random(0, N, P),
    rotate(List, P, Result).



/*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P26 (**) Generate the combinations of K distinct objects chosen from the N elements of a list
In how many ways can a committee of 3 be chosen from a group of 12 people? We all know that there are C(12,3) = 220 possibilities 
(C(N,K) denotes the well-known binomial coefficients). For pure mathematicians, this result may be great. 
But we want to really generate all the possibilities (via backtracking).

Example:
?- combination(3,[a,b,c,d,e,f],L).
L = [a,b,c] ;
L = [a,b,d] ;
L = [a,b,e] ;

*/
    
combination(0, _ , []).
combination(K, L, [X | Xs]) :- 
    K > 0,
    el(X, L, R), 
    K1 is K - 1, 
    combination(K1, R, Xs).

% Find out what the following predicate el/3 exactly does.

el(X, [X | L], L).
el(X, [_ | L], R) :- 
    el(X, L, R).



/*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P27 (**) Group the elements of a set into disjoint subsets.
a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2, 3 and 4 persons? Write a predicate that generates all the possibilities via backtracking.

Example:
?- group3([aldo,beat,carla,david,evi,flip,gary,hugo,ida],G1,G2,G3).
G1 = [aldo,beat], G2 = [carla,david,evi], G3 = [flip,gary,hugo,ida]
...

b) Generalize the above predicate in a way that we can specify a list of group sizes and the predicate will return a list of groups.

Example:
?- group([aldo,beat,carla,david,evi,flip,gary,hugo,ida],[2,2,5],Gs).
Gs = [[aldo,beat],[carla,david],[evi,flip,gary,hugo,ida]]
...

Note that we do not want permutations of the group members; i.e. [[aldo,beat],...] is the same solution as [[beat,aldo],...]. However, we make a difference between [[aldo,beat],[carla,david],...] and [[carla,david],[aldo,beat],...].

*/

% subtract(+Set, +Delete, -Result)
% ord_subtract(+InOSet, +NotInOSet, -Diff)

% a) USE el from P26
group3(G,G1,G2,G3) :- 
   selectN(2,G,G1),
   subtract(G,G1,R1),

   selectN(3,R1,G2),
   subtract(R1,G2,R2),

   selectN(4,R2,G3),
   subtract(R2,G3,[]).

% b) USE el from P26
group([],[],[]).
group(G,[N1|Ns],[G1|Gs]) :- 
   selectN(N1,G,G1),
   subtract(G,G1,R),
   group(R,Ns,Gs).

% selectN(N,L,S) :- select N elements of the list L and put them in 
%    the set S. Via backtracking return all posssible selections, but
%    avoid permutations; i.e. after generating S = [a,b,c] do not return
%    S = [b,a,c], etc.

selectN(0,_,[]) :- !.
selectN(N,L,[X|S]) :- 
   N > 0, 
   el(X,L,R), 
   N1 is N-1,
   selectN(N1,R,S).



/*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P28 (**) Sorting a list of lists according to length of sublists
a) We suppose that a list (InList) contains elements that are lists themselves. The objective is to sort the elements of InList according to their length. E.g. short lists first, longer lists later, or vice versa.

Example:
?- lsort([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L).
L = [[o], [d, e], [d, e], [m, n], [a, b, c], [f, g, h], [i, j, k, l]]

b) Again, we suppose that a list (InList) contains elements that are lists themselves. But this time the objective is to sort the elements of InList according to their length frequency; i.e. in the default, where sorting is done ascendingly, lists with rare lengths are placed first, others with a more frequent length come later.

Example:
?- lfsort([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L).
L = [[i, j, k, l], [o], [a, b, c], [f, g, h], [d, e], [d, e], [m, n]]

Note that in the above example, the first two lists in the result L have length 4 and 1, both lengths appear just once. The third and forth list have length 3 which appears, there are two list of this length. And finally, the last three lists have length 2. This is the most frequent length.

*/

% a) length sort
%
% lsort(InList,OutList) :- it is supposed that the elements of InList 
% are lists themselves. Then OutList is obtained from InList by sorting 
% its elements according to their length. lsort/2 sorts ascendingly,
% lsort/3 allows for ascending or descending sorts.
% (list_of_lists,list_of_lists), (+,?)

lsort(InList,OutList) :- lsort(InList,OutList,asc).

% sorting direction Dir is either asc or desc

lsort(InList,OutList,Dir) :-
   add_key(InList,KList,Dir),
   keysort(KList,SKList),
   rem_key(SKList,OutList).

add_key([],[],_).
add_key([X|Xs],[L-p(X)|Ys],asc) :- !, 
	length(X,L), add_key(Xs,Ys,asc).
add_key([X|Xs],[L-p(X)|Ys],desc) :- 
	length(X,L1), L is -L1, add_key(Xs,Ys,desc).

rem_key([],[]).
rem_key([_-p(X)|Xs],[X|Ys]) :- rem_key(Xs,Ys).



% b) length frequency sort
%
% lfsort (InList,OutList) :- it is supposed that the elements of InList
% are lists themselves. Then OutList is obtained from InList by sorting
% its elements according to their length frequency; i.e. in the default,
% where sorting is done ascendingly, lists with rare lengths are placed
% first, other with more frequent lengths come later.
%
% Example:
% ?- lfsort([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L).
% L = [[i, j, k, l], [o], [a, b, c], [f, g, h], [d, e], [d, e], [m, n]]
%
% Note that the first two lists in the Result have length 4 and 1, both
% length appear just once. The third and forth list have length 3 which
% appears, there are two list of this length. And finally, the last
% three lists have length 2. This is the most frequent length.

lfsort(InList,OutList) :- lfsort(InList,OutList,asc).

% sorting direction Dir is either asc or desc

lfsort(InList,OutList,Dir) :-
	add_key(InList,KList,desc),
   keysort(KList,SKList),
   pack(SKList,PKList),
   lsort(PKList,SPKList,Dir),
   flatten(SPKList,FKList),
   rem_key(FKList,OutList).
   
pack([],[]).
pack([L-X|Xs],[[L-X|Z]|Zs]) :- transf(L-X,Xs,Ys,Z), pack(Ys,Zs).

% transf(L-X,Xs,Ys,Z) Ys is the list that remains from the list Xs
%    when all leading copies of length L are removed and transfed to Z

transf(_,[],[],[]).
transf(L-_,[K-Y|Ys],[K-Y|Ys],[]) :- L \= K.
transf(L-_,[L-X|Xs],Ys,[L-X|Zs]) :- transf(L-X,Xs,Ys,Zs).

test :-
   L = [[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],
   write('L = '), write(L), nl,
   lsort(L,LS),
   write('LS = '), write(LS), nl,
   lsort(L,LSD,desc),
   write('LSD = '), write(LSD), nl,
   lfsort(L,LFS),
   write('LFS = '), write(LFS), nl.


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P31 (**) Determine whether a given integer number is prime.
Example:
?- is_prime(7).
Yes

*/

is_prime(X) :-
    X < 2 -> false; 
    X = 2 -> true; 
    X mod 2 =:= 0 -> false; 
    check_divs(X).

check_divs(X) :-
    check_divs(3, X).

% Stop when C*C > X: no divisor found → prime
check_divs(C, X) :-
    C * C > X, !.

% If X mod C =:= 0: not prime
check_divs(C, X) :-
    X mod C =:= 0, !, fail.

% Else, try next odd C
check_divs(C, X) :-
    C2 is C + 2,
    check_divs(C2, X).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P32 (**) Determine the greatest common divisor of two positive integer numbers.
Use Euclid's algorithm.
Example:
?- gcd(36, 63, G).
G = 9
Define gcd as an arithmetic function; so you can use it like this:
?- G is gcd(36,63).
G = 9

*/

gcd(X, Y, X) :-
    Y < 1.
gcd(X, Y, G) :-
    Y >= 1,
    R is X mod Y,
    gcd(Y, R, G).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P33 (*) Determine whether two positive integer numbers are coprime.
Two numbers are coprime if their greatest common divisor equals 1.
Example:
?- coprime(35, 64).
Yes

*/

coprime(X, Y) :-
    gcd(X, Y, R),
    R is 1.



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P34 (**) Calculate Euler's totient function phi(m).
Euler's so-called totient function phi(m) is defined as the number of positive integers r (1 <= r < m) that are coprime to m.
Example: m = 10: r = 1,3,7,9; thus phi(m) = 4. Note the special case: phi(1) = 1.

?- Phi is totient_phi(10).
Phi = 4

*/

:- arithmetic_function(totient_phi/1).

totient_phi(1,1) :- !.
totient_phi(X, RES) :- phi(X, RES).

phi(X, RES) :- 
    range(1, X, L),
    extract_coprime(L, X, R),
    length(R, RES).

extract_coprime([], _, []).

extract_coprime([H | T], X, R) :-
    \+ coprime(H, X),
    extract_coprime(T, X, R).

extract_coprime([H | T], X, [H | R]) :-
    coprime(H, X),
    extract_coprime(T, X, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P35 (**) Determine the prime factors of a given positive integer.
Construct a flat list containing the prime factors in ascending order.
Example:
?- prime_factors(315, L).
L = [3,3,5,7]

*/

% P35 (**) Determine the prime factors of a given positive integer. 

prime_factors(X, L) :-
    X > 0,
    prime_factors(X, L, 2).

prime_factors(1, [], _) :- !.       % while (X >= 1) - reach the contradiction
prime_factors(X, [D | L], D) :-     
    R is X // D,
    X =:= D * R, !,
    prime_factors(R, L, D).

prime_factors(X, L, D) :-
    next_factor(X, D, NF),
    prime_factors(X, L, NF).

% next_factor(N,F,NF) :- when calculating the prime factors of N
%    and if F does not divide N then NF is the next larger candidate to
%    be a factor of N.

next_factor(_, 2, 3) :- !.
next_factor(X, D, NF) :- D * D < X, !, NF is D + 2.      
next_factor(X, _, X).  % D > sqrt(N)



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P36 (**) Determine the prime factors of a given positive integer (2).
Construct a list containing the prime factors and their multiplicity.
Example:
?- prime_factors_mult(315, L).
L = [[3,2],[5,1],[7,1]]

*/

prime_factors_mult(X, L) :-
    prime_factors(X, Result),
    encode(Result, L1),
    reorder(L1, L).

reorder([], []).
reorder([[A, B] | T], [[factor(B), aparitii(A)] | R]) :-
    reorder(T, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P39 (*) A list of prime numbers.
Given a range of integers by its lower and upper limit, construct a list of all prime numbers in that range.

?- prime_list(1, 10, R).
R = [2, 3, 5, 7].
*/

prime_list(A,B,L) :- 
    A =< 2, !, 
    p_list(2,B,L).

prime_list(A,B,L) :- 
    A1 is (A // 2) * 2 + 1, 
    p_list(A1,B,L).

p_list(A,B,[]) :- A > B, !.
p_list(A,B,[A|L]) :- 
    is_prime(A), !, 
    next(A,A1), 
    p_list(A1,B,L). 

p_list(A,B,L) :- 
    next(A,A1),
    p_list(A1,B,L).

next(2,3) :- !.
next(A,A1) :- A1 is A + 2.



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P40 (**) Goldbach's conjecture.
Goldbach's conjecture says that every positive even number greater than 2 is the sum of two prime numbers. Example: 28 = 5 + 23. It is one of the most famous facts in number theory that has not been proved to be correct in the general case. It has been numerically confirmed up to very large numbers (much larger than we can go with our Prolog system). Write a predicate to find the two prime numbers that sum up to a given even integer.
Example:
?- goldbach(28, L).
L = [5,23]

*/


goldbach(4, [2, 2]) :- !.
goldbach(X, L) :-
    X > 4,
    X mod 2 =:= 0,
    goldbach(X, 3, L).

goldbach(X, B, [A, B]) :-
    A is X - B,
%    is_prime(A).

     is_prime(A), !. 
%       - to stop recursion

goldbach(X, B, L) :-
    B < X,
    next_prime(B, Next),
    goldbach(X, Next, L).

next_prime(P,P1) :- P1 is P + 2, is_prime(P1), !.
next_prime(P,P1) :- P2 is P + 2, next_prime(P2,P1).


% find_goldbach(Y, _, X, []) :-
%     Y is X - 2.
% find_goldbach(_, 2, _, []).
% find_goldbach(L, R, X, [[L, R] | Result]) :-
%     L < X,
%     R > 2,
%     is_prime_sum(L, R, X),
%     L1 is L + 1,
%     R1 is R - 1,
%     find_goldbach(L1, R1, X, Result).

% find_goldbach(L, R, X, Result) :-
%     L < X,
%     R > 2,
%     \+ is_prime_sum(L, R, X),
%     L1 is L + 1,
%     R1 is R - 1,
%     find_goldbach(L1, R1, X, Result).

% is_prime_sum(X, Y, R) :-
%     is_prime(X),
%     is_prime(Y),
%     R is X + Y.



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P41 (**) A list of Goldbach compositions.
Given a range of integers by its lower and upper limit, print a list of all even numbers and their Goldbach composition.
Example:
?- goldbach_list(9,20).
10 = 3 + 7
12 = 5 + 7
14 = 3 + 11
16 = 3 + 13
18 = 5 + 13
20 = 3 + 17

In most cases, if an even number is written as the sum of two prime numbers, one of them is very small. Very rarely, the primes are both bigger than say 50. Try to find out how many such cases there are in the range 2..3000.

Example (for a print limit of 50):
?- goldbach_list(1,2000,50).
992 = 73 + 919
1382 = 61 + 1321
1856 = 67 + 1789
1928 = 61 + 1867

*/

% here we use goldbach/2 from P40, but stop the recursion

goldbach_list(L, U) :-
    L =< U,
    L mod 2 =:= 0,
    goldbach(L, [A, B]),
    format('~w = ~w + ~w~n', [L, A, B]),
    L1 is L + 2,
    goldbach_list(L1, U).

goldbach_list(L, U) :-
    L =< U,
    L mod 2 =\= 0,                % skip odd numbers
    L1 is L + 1,
    goldbach_list(L1, U).

goldbach_list(L, U) :-
    L > U.                        % base case: done


% limit print to LP

goldbach_list(L, U, 0).
goldbach_list(L, U, LP) :-
    L =< U,
    L mod 2 =:= 0,
    goldbach(L, [A, B]),
    format('~w) ~w = ~w + ~w~n', [LP, L, A, B]),
    L1 is L + 2,
    LP1 is LP - 1,
    goldbach_list(L1, U, LP1).

goldbach_list(L, U, LP) :-
    L =< U,
    L mod 2 =\= 0,                % skip odd numbers
    L1 is L + 1,
    goldbach_list(L1, U, LP).

goldbach_list(L, U, LP) :-
    L > U.                        % base case: done



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

LOGICĂ
TABEL DE ADEVĂR

P46 (**) Truth tables for logical expressions.
Define predicates and/2, or/2, nand/2, nor/2, xor/2, impl/2 and equ/2 (for logical equivalence) which succeed or fail according to the result of their respective operations; e.g. and(A,B) will succeed, if and only if both A and B succeed. Note that A and B can be Prolog goals (not only the constants true and fail).
A logical expression in two variables can then be written in prefix notation, as in the following example: and(or(A,B),nand(A,B)).

Now, write a predicate table/3 which prints the truth table of a given logical expression in two variables.

Example:
?- table(A,B,and(A,or(A,B))).
true true true
true fail true
fail true fail
fail fail fail
*/

and(A, B) :- A, B.

or(A, _) :- A.
or(_, B) :- B.

xor(A,B) :- not(equ(A,B)).
equ(A,B) :- or(and(A,B), and(not(A),not(B))).

nor(A,B) :- not(or(A,B)).
nand(A,B) :- not(and(A,B)).
impl(A,B) :- or(not(A),B).

% bind(X) :- instantiate X to be true and false successively

bind(true).
bind(fail).

table(A,B,Expr) :- 
    bind(A), 
    bind(B), 
    do(A,B,Expr), 
    fail.

do(A,B,_) :- 
    write(A), 
    write('  '), 
    write(B), 
    write('  '), 
    fail.

do(_,_,Expr) :- 
    Expr, !, 
    write(true), 
    nl.

do(_,_,_) :- 
    write(fail), 
    nl.



/* 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P47 (*) Truth tables for logical expressions (2).
Continue problem P46 by defining and/2, or/2, etc as being operators. This allows to write the logical expression in the more natural way, as in the example: A and (A or not B). Define operator precedence as usual; i.e. as in Java.
Example:
?- table(A,B, A and (A or not B)).
true true true
true fail true
fail true fail
fail fail fail
*/

% op(precedenta, operanzi, nume)

:- op(900, fy, not).
:- op(910, yfx, and).
:- op(910, yfx, nand).
:- op(920, yfx, or).
:- op(920, yfx, nor).
:- op(930, yfx, impl).
:- op(930, yfx, equ).
:- op(930, yfx, xor).




/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
COLOCVIU 2024

punct(coordX, coordY)

?- lista_puncte([punct(3, 5), punct(5, 2), punct(9, 6)], 3, R).
R = [punct(3, 5), punct(9, 6)]

*/

lista_puncte([], _ , []).

lista_puncte([punct(X, Y) | T], Val, [punct(X,Y) | R]) :-
    Y > Val,
    lista_puncte(T, Val, R).

lista_puncte([punct(_, Y) | T], Val, R) :-
    Y =< Val,
    lista_puncte(T, Val, R).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

COLOCVIU 2024

?- dropN([a, b, c, b], R, 2).
R = [a, b]
?- dropN([a, b, c], R, 5).
false.

*/

dropN(List, R, K) :-
    length(List, N),
    K =< N,
    K1 is N - K,
    dropp(List, R, K1).

dropp(_, [], 0).
dropp([H | T], [H | R], K) :-
    K > 0,
    K2 is K - 1,
    dropp(T, R, K2).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

COLOCVIU 2024

rmdn/2 true <=> Psi este rezultatul eliminării tuturor negațiilor duble din Phi.

?- rmdn(non(non(a)), R).
R = a
?- rmdn(non(imp(non(non(a)), b)), R).
R = non(imp(a, b))
?- rmdn(non(non(non(non(non(sau(a, non(non(b)))))))), R).
R = non(sau(a, b)).

*/

rmdn(Phi, Phi)                  :- atom(Phi).
rmdn(non(Phi), non(Phi))        :- atom(Phi).
rmdn(non(non(Phi)), Psi)        :- rmdn(Phi, Psi).

rmdn(non(si(Phi,Psi)), non(A))      :- rmdn(si(Phi,Psi), A).
rmdn(non(sau(Phi,Psi)), non(A))     :- rmdn(sau(Phi,Psi), A).
rmdn(non(imp(Phi,Psi)), non(A))     :- rmdn(imp(Phi,Psi), A).

rmdn(si(Phi, Psi), si(Phi1, Psi1))      :- rmdn(Phi, Phi1), rmdn(Psi, Psi1).
rmdn(sau(Phi, Psi), sau(Phi1, Psi1))    :- rmdn(Phi, Phi1), rmdn(Psi, Psi1).
rmdn(imp(Phi, Psi), imp(Phi1, Psi1))    :- rmdn(Phi, Phi1), rmdn(Psi, Psi1).
 

/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

10. The length of a list

?- len([1, 2, 3, 4], X).
X = 4.

We also have predefined length/2
?- length(List, X).

*/

len([], 0).
len([H | T], X) :-
    len(T, X1),
    X is X1 + 1.


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

11. Expand intervals

?- expand_intervals([(1, 4), (2,1), (5, 9)], X).

*/

expand_intervals([], []).
expand_intervals([(From, To) | T], [ResLevel | Res]) :-
    expand_this_interval(From, To, ResLevel),
    expand_intervals(T, Res).

expand_this_interval(Top, Top, [Top]).
expand_this_interval(X, Top, []) :- X > Top.
expand_this_interval(Current, Top, [Current | Res]) :-
    Current < Top,
    Next is Current + 1,
    expand_this_interval(Next, Top, Res).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

12. Reduce intervals

?- reduce_intervals([[1, 2, 3, 4], [], [5, 6, 7, 8, 9]], X).

*/

reduce_intervals([], []).
reduce_intervals([List | T], [ResLevel | Res]) :-
    reduce_this_interval(List, ResLevel),
    reduce_intervals(T, Res).

reduce_this_interval([], (0, 0)).
reduce_this_interval([X], (X, X)).
reduce_this_interval([H | T], (H, Last)) :-
    last(T, Last). 


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

COLOCVIU 2025

13. Să se împartă lista L în două liste L1, L2, cu proprietatea că:
Lungimea lui L1 este divizibilă cu lungimea listei L2

Permutări la stânga.

+ get_length(List, R)

?- div_concat([1, 2, 3, 4, 5, 6, 7, 8, 9], X).
X = [2, 3, 4, 5, 6, 7, 8, 9, 1] ;
X = [4, 5, 6, 7, 8, 9, 1, 2, 3] ;
X = [7, 8, 9, 1, 2, 3, 4, 5, 6] ;
X = [9, 1, 2, 3, 4, 5, 6, 7, 8] ;
false.

*/

div_concat(L, R) :-
    length(L, Len),
    LenMinus1 is Len - 1,
    between(1, LenMinus1, N),   % Generează numerele dintr-un interval
        split_at(N, L, L1, L2),
        length(L1, Len1),
        length(L2, Len2),
        (Len1 mod Len2 =:= 0 ; Len2 mod Len1 =:= 0),
        append(L2, L1, R).

% split_at(N, List, Prefix, Suffix)
split_at(0, L, [], L).
split_at(N, [H|T], [H|Prefix], Suffix) :-
    N > 0,
    N1 is N - 1,
    split_at(N1, T, Prefix, Suffix).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

14. Permutări

1 ?- permutation([1, 2, 3, 4, 5, 6, 7, 8, 9], X). 
X = [1, 2, 3, 4, 5, 6, 7, 8, 9] ;
X = [2, 3, 4, 5, 6, 7, 8, 9, 1] ;
X = [3, 4, 5, 6, 7, 8, 9, 1, 2] ;
X = [4, 5, 6, 7, 8, 9, 1, 2, 3] ;
X = [5, 6, 7, 8, 9, 1, 2, 3, 4] ;
X = [6, 7, 8, 9, 1, 2, 3, 4, 5] ;
X = [7, 8, 9, 1, 2, 3, 4, 5, 6] ;
X = [8, 9, 1, 2, 3, 4, 5, 6, 7] ;
X = [9, 1, 2, 3, 4, 5, 6, 7, 8] ;

*/

permutation(L, R) :-
    permutation(L, L, R).

permutation(_, L, L).

permutation(Orig, Current, R) :-
    rotate_left(Current, Next),
    Next \= Orig,
    permutation(Orig, Next, R).

rotate_left([H | T], R) :- 
    append(T, [H], R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

15. Diagonală

1 ?- diag([1, 2, 3, 4, 5, 6, 7, 8, 9], X).
X = [1, 2, 3, 4, 5, 6, 7, 8, 9] ;
X = [_, 2, 3, 4, 5, 6, 7, 8, 9] ;
X = [_, _, 3, 4, 5, 6, 7, 8, 9] ;
X = [_, _, _, 4, 5, 6, 7, 8, 9] ;
X = [_, _, _, _, 5, 6, 7, 8, 9] ;
X = [_, _, _, _, _, 6, 7, 8, 9] ;
X = [_, _, _, _, _, _, 7, 8, 9] ;
X = [_, _, _, _, _, _, _, 8, 9] ;
X = [_, _, _, _, _, _, _, _, 9] ;
X = [_, _, _, _, _, _, _, _, _].    
*/


get_length([], 0).
get_length([H | T], Result) :-
    get_length(T, Result1),
    Result is Result1 + 1.

diag(H, H).
diag([H | T], [ResLevel | Result]) :-
    diag(T, Result).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

16. Join

1 ?- join([1, 2, 3], [a, b, c], R).
R = [1, 2, 3, a, b, c].

*/

join([], L, L).
join([H | T], L2, [H | Result]) :-
    join(T, L2, Result).





% 1_151_Minciunescu_Vlad.pl

/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P1. 

Din enunț:

?- expand_intervals([(1, 3), (5, 5), (5, 3), (2, 6)], R).
R = [[1, 2, 3], [5], [], [2, 3, 4, 5, 6]].


Exemple proprii:

?- expand_exam([(3, 3), (5, 4), (1, 7), (-2, 6)], R). 
R = [[3], [], [1, 2, 3, 4, 5, 6|...], [-2, -1, 0, 1, 2|...]] .

?- expand_exam([(3, 3), (5, 4), (1, 3), (-2, 1)], R).   
R = [[3], [], [1, 2, 3], [-2, -1, 0, 1]] .

*/

% Generez o listă de la A la B prin range/3, pe care o transmit recursiv în următoarele apeluri
expand_exam([(A, B) | T], [L | T]) :-
    range(A, B, L).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P2.
?- div_concat_exam([1, 2, 3, 4, 5, 6, 7, 8, 9], R).
R = [2, 3, 4, 5, 6, 7, 8, 9, 1] ;
R = [4, 5, 6, 7, 8, 9, 1, 2, 3] ;
R = [7, 8, 9, 1, 2, 3, 4, 5, 6] ;
R = [9, 1, 2, 3, 4, 5, 6, 7, 8] ;

?- div_concat_exam([1, 2, 3], [2, 1, 3]).
false


Exemple proprii:

?- div_concat_exam([3, 2, 6, 9, -3], R).            
R = [2, 6, 9, -3, 3] ;
R = [-3, 3, 2, 6, 9] ;
*/

div_concat_exam(L, R) :-
    length(L, N),
    between(1, N, X),
    D is N - X,
    D > 0,
    (N mod X =:= 0 ; N mod D =:= 0),
    rotate(L, X, R),
    L \= R.



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P3.
a) assoc_and primește ca argument două formule Phi, Psi
este adevărat <=> 
- Phi și Psi sunt formate doar din conjuncții și variabile
- Psi se poate obține din Psi prin reasocierea parantezelor

?- assoc_and(si(si(a, b), c), si(a, si(b, c))).
true
?- assoc_and(si(si(a, b), si(c, d)), si(a, si(b, si(c, d)))).
true
?- assoc_and(si(a, b), si(b, a)).
false
?- assoc_and(a, a).
true
?- assoc_and(sau(a, sau(b, c)), sau(sau(a, b), c)).
false

*/

% Utilă pentru ambele subpuncte.
% Adevărată doar dacă doar și-urile se reduc.
only_var_si(A) :- atom(A).
only_var_si(si(A, B)) :-
    only_var_si(A),
    only_var_si(B).


extract_vars(A, [A]) :- atom(A).
extract_vars(si(A, B), R) :-
    extract_vars(A, L1),
    extract_vars(B, L2),
    append(L1, L2, R).


% Punctul A)
assoc_and(Phi, Phi) :- atom(Phi), !.
assoc_and(Phi, Psi) :- atom(Phi), atom(Psi).
assoc_and(si(si(A, B), C), si(A, si(B, C))) :- atom(A), atom(B), atom(C). 
assoc_and(si(A, si(B, C)), si(si(A, B), C)) :- atom(A), atom(B), atom(C).

assoc_and(si(si(A, B), C), si(A, si(B, C))) :-
    only_var_si(A),
    only_var_si(B),
    only_var_si(C).

assoc_and(si(si(a, b), si(c, d)), si(a, si(b, si(c, d)))) :- atom(A), atom(B), atom(C), atom(D).
assoc_and(si(si(a, b), si(c, d)), si(a, si(b, si(c, d)))) :-
    only_var_si(A),
    only_var_si(B),
    only_var_si(C),
    only_var_si(D).

assoc_and(si(A, B), si(C, D)) :-
    only_var_si(A),
    only_var_si(B),
    only_var_si(C),
    only_var_si(D),
    not(atom(A)), not(atom(B)), not(atom(C)), not(atom(D)),
    assoc_and(A, C).

assoc_and(si(A, B), si(C, D)) :-
    only_var_si(A),
    only_var_si(B),
    only_var_si(C),
    only_var_si(D),
    not(atom(A)), not(atom(B)), not(atom(C)), not(atom(D)),
    assoc_and(B, D).

% Punctul B)
assoc_and_right(Phi, Psi) :-
    only_var_si(Phi),
    extract_vars(Phi, Vars),
    make_right_assoc(Vars, Psi).

make_right_assoc([A, B], si(A, B)).
make_right_assoc([A, B | T], si(A, C)) :-
    make_right_assoc([B | T], C).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

P4.

?- assoc_or(sau(sau(a, b), c), sau(a, sau(b, c))).
true
?- assoc_or(sau(sau(a, b), sau(c, d)), sau(a, sau(b, sau(c, d)))).
true
?- assoc_or(sau(a, b), sau(b, a)).
false
?- assoc_or(a, a).
true
?- assoc_or(si(a, si(b, c)), si(si(a, b), c)).
false

*/

% Necesar pentru ambele subpuncte

only_vars_disj(A) :- atom(A).
only_vars_disj(sau(A, B)) :-
    only_vars_disj(A),
    only_vars_disj(B).

disj_vars(A, [A]) :- atom(A).
disj_vars(sau(A, B), R) :-
    disj_vars(A, L1),
    disj_vars(B, L2),
    append(L1, L2, R).

% Punctul A

assoc_or(Phi, Phi) :- atom(Phi), !. % nu e necesară și verificarea ulterioară
assoc_or(Phi, Psi) :- atom(Phi), atom(Psi).

assoc_or(sau(sau(A, B), C), sau(A, sau(B, C))) :- atom(A), atom(B), atom(C).
assoc_or(sau(A, sau(B, C)), sau(sau(A, B), C)) :- atom(A), atom(B), atom(C).

assoc_or(sau(sau(A, B), sau(C, D)), sau(a, sau(b, sau(C, D)))) :- atom(A), atom(B), atom(C), atom(D), !.
assoc_or(sau(sau(A, B), sau(C, D)), sau(a, sau(b, sau(C, D)))) :-
    only_vars_disj(A), only_vars_disj(B), only_vars_disj(C), only_vars_disj(D),
    not(atom(A)), not(atom(B)), not(atom(C)), not(atom(D)),
    assoc_or(A, C).
assoc_or(sau(sau(A, B), sau(C, D)), sau(a, sau(b, sau(C, D)))) :-
    only_vars_disj(A), only_vars_disj(B), only_vars_disj(C), only_vars_disj(D),
    not(atom(A)), not(atom(B)), not(atom(C)), not(atom(D)),
    assoc_or(B, D).

% Punctul B
assoc_or_right(Phi, Psi) :-
    only_vars_disj(Phi),
    disj_vars(Phi, R),
    make_right_assoc_or(R, Psi).

make_right_assoc_or([A, B], sau(A, B)).
make_right_assoc_or([A, B | T], sau(A, C)) :-
    make_right_assoc_or([B | T], C).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Examen 2022/2023

?- consec([1,2,3,4,5]).
true
?- consec([1,2,4,5,6]).
false

*/

consec([A]).
consec([A, B]) :- B - A =:= 1, !.
consec([A, B | T]) :-
    B - A =:= 1,
    consec([B | T]).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Examen 2022/2023

lista_angajati(ListaAngajati, SalariuPrag, ListaRezultat)

?- lista_angajati([angajat(ion, 1000), angajat(mirela, 4000), angajat(mihai, 1200), angajat(ioana, 3500)], 2000, R).
R = [mirela, ioana]

*/

lista_angajati([], _, []).
lista_angajati([angajat(Nume, Suma) | T], SalariuPrag, [Nume | ListaRezultat]) :-
    Suma > SalariuPrag,
    lista_angajati(T, SalariuPrag, ListaRezultat).

lista_angajati([angajat(Nume, Suma) | T], SalariuPrag, ListaRezultat) :-
    Suma =< SalariuPrag,
    lista_angajati(T, SalariuPrag, ListaRezultat).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Examen 2022 / 2023

?- consec_desc([5,4,3,2,1]).
true
?- consec_desc([6,5,4,2,1]).
false

*/

consec_desc([A, B]) :- A - B =:= 1, !. 
consec_desc([A]) :- !.
consec_desc([A, B | T]) :-
    A - B =:= 1,
    consec_desc([B | T]).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Examen 2022 / 2023

listare_studenti(ListaStudenti, PragNota, ListareRezultat)

- listare_studenti([student(ionel, 8), student(maria, 10), student(gabriela, 5), student(luca, 9)], 9, R).

*/

listare_studenti([], _, []).

listare_studenti([student(Nume, Nota) | T], Prag, [Nume | R]) :-
    Nota < Prag,
    listare_studenti(T, Prag, R).

listare_studenti([student(Nume, Nota) | T], Prag, R) :-
    Nota >= Prag,
    listare_studenti(T, Prag, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

?- desparte([[1, 2, 3, 5, 6], [7, 8, 9, 11, 12]], R).
R = [[1, 2, 3], [5, 6], [7, 8, 9], [11, 12]].

*/

desparte([], []).
desparte([H | T], R) :-
    desparte_lista(H, L1),
    desparte(T, L2),
    append(L1, L2, R).

desparte_lista([X], [[X]]).

desparte_lista([A, B | T], [[A | [B | Sub]] | Rest]) :-
    (B - A =:= 1 ; B - A =:= 0),
    desparte_lista([B | T], [[B | Sub] | Rest]).

desparte_lista([A, B | T], [[A] | Rest]) :-
    B - A =\= 1,
    B - A =\= 0,
    desparte_lista([B | T], Rest).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

?- inchide([[1, 2, 3], [4, 5], [7], [8, 9]], R).
R = [[1, 2, 3, 4, 5], [7, 8, 9]]


?- inchide([[1, 2, 3], [4, 5, 7], [7], [8, 9]], R).

*/

inchide(List, R) :-
    flatten(List, L1),
    desparte_lista(L1, R).
 


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

VARS

?- vars(imp(non(a),imp(a,b)),S).
S = [a, b]

*/

vars(A, [A]) :- atom(A).

vars(imp(A, B), R) :-
    vars(A, L1),
    vars(B, L2),
    union(L1, L2, R).

vars(sau(A, B), R) :-
    vars(A, L1),
    vars(B, L2),
    union(L1, L2, R).

vars(si(A, B), R) :-
    vars(A, L1),
    vars(B, L2),
    union(L1, L2, R).

vars(non(A), R) :-
    vars(A, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

EVALUARE E(V)

?- val(b,[(a,1),(b,0)],A).
A = 0

4 ?- val(A,[(a,1),(b,0),(c, 0)],0). 
A = b ;
A = c ;

*/

val(A, [(A, V) | T], V).
val(A, [_ | T], V) :-
    val(A, T, V).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

bnon/2, bsi/3, bsau/3, bimp/3 

?- bsi(1,0,C).
C = 0
?- bimp(A,0,0).
A = 1
?- bimp(0,B,0).
false

*/

bnon(1, 0). bnon(0, 1).
bsi(1, 1, 1). bsi(1, 0, 0). bsi(0, 1, 0). bsi(0, 0, 0).
bsau(0, 0, 0). bsau(0, 1, 1). bsau(1, 0, 1). bsau(1, 1, 1).

% X -> Y = (non X) sau Y
bimp(X, Y, Z) :-
    bnon(X, NX), 
    bsau(NX, Y, Z), !.



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

EVALUARE expresie

?- eval(imp(b,d),[(a,1), (b,0), (d,1)],A).
A = 1
?- eval(imp(d,b),[(a,1), (b,0), (d,1)],A).
A = 0

*/

eval(V, E, A) :-
    atom(V),
    val(V, E, A).

eval(non(X), E, A) :-
    eval(X, E, B),
    bnon(B, A).

eval(si(X, Y), E, A) :-
    eval(X, E, B),
    eval(Y, E, C),
    bsi(B, C, A).

eval(sau(X, Y), E, A) :-
    eval(X, E, B),
    eval(Y, E, C),
    bsau(B, C, A).

eval(imp(X, Y), E, A) :-
    eval(X, E, B),
    eval(Y, E, C),
    bimp(B, C, A).


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

EVALUARi EXPRESIE

?- evals(imp(d,b),[[(a,1), (b,0), (d,1)], [(a,1), (b,1), (d,0)]],As).
As = [0, 1]

*/

evals(_, [], []).
evals(X, [E | T], [L | R]) :-
    eval(X, E, L),
    evals(X, T, R).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Es LISTA DE EVALUARI ÎN S

evs/2
evs(S, Es).

?- evs([c,b],Es).
Es = [[(c,0), (b,0)], [(c,1), (b,0)], [(c,0), (b,1)], [(c,1), (b,1)]]

*/

evs([],[ [] ]).

evs([V | T], Es) :- 
    evs(T, Esp), 
    adauga(V, Esp, Es).

adauga(_,[],[]).
adauga(V, [E | T], 
    [
        [(V, 0) | E], 
        [(V, 1) | E] 
    | Es ]
    ) 
    :- adauga(V,T,Es).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Toate evaluările expresiei X apar în As

all_evals/2
all_evals(X,As)

?- all_evals(imp(a,a),As).
As = [1, 1]
?- all_evals(imp(a,b),As).
As = [1, 0, 1, 1]


*/

all_evals(X, As) :-
    vars(X, R),
    evs(R, L),
    evals(X, L, As).



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Tautologie
<=> Toate evaluările expresiei X sunt 1

?- taut(imp(a,a)).
true
?- taut(imp(a,b)).
false

*/

taut(X) :-
    all_evals(X, As),
    \+ member(0, As), !.


/*
setof(X,(member(X,[1,2,2,2,3]),member(Y,[0,1,2,3,4,5]),X<Y),L).

1 ?- setof(X,(member(X,[1,2,2,2,3]),member(Y,[0,1,2,3,4,5]),X<Y),L).
Y = 2,
L = [1] ;
Y = 3,
L = [1, 2] ;
Y = 4,
L = [1, 2, 3] ;
Y = 5,
L = [1, 2, 3].

*/



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Predicate Logic to clausal logic 

*/

% transform(Formula,Clauses):-
%    rewrite_implications(Formula,F1),
%    negations_inside(F1,F2),
%    prenex_normal_form(F2,F3),
%    skolemise(F3,F4),
%    conjunctive_normal_form(F4,F5),
%    clausal_form(F5,Clauses).



% % rewrite_implications(F1,F2) <- F2 is a PL formula
% %                                without implications,
% %                                log. equivalent with F1

% rewrite_implications(A,A):-             % base case
%     literal(A).
% rewrite_implications(A => B, -C v D):-  % implication
%     rewrite_implications(A,C),
%     rewrite_implications(B,D).
% rewrite_implications(A & B, C & D):-    % no change;
%     rewrite_implications(A,C),          % try rest of
%     rewrite_implications(B,D).          % formula
% rewrite_implications(A v B, C v D):-
%     rewrite_implications(A,C),
%     rewrite_implications(B,D).
% rewrite_implications(-A,-C):-
%     rewrite_implications(A,C).
% rewrite_implications(forall(X,B), forall(X,D)):-
%     rewrite_implications(B,D).
% rewrite_implications(exists(X,B), exists(X,D)):-
%     rewrite_implications(B,D).



% % negations_inside(F1,F2) <- F2 is a PL formula with
% %                            negs. only preceding literals
% %                            log. equivalent with F1

% negations_inside(A,A):-               % base case
%     literal(A).
% negations_inside(-(A & B), C v D):-   % De Morgan (1)
%     negations_inside(-A,C),
%     negations_inside(-B,D).
% negations_inside(-(A v B), C & D):-   % De Morgan (2)
%     negations_inside(-A,C),
%     negations_inside(-B,D).
% negations_inside(-(-A),B):-           % double negation
%     negations_inside(A,B).
% negations_inside(-exists(X,A),forall(X,B)):- % quantifiers
%     negations_inside(-A,B).
% negations_inside(-forall(X,A),exists(X,B)):-
%     negations_inside(-A,B).
% negations_inside(A & B, C & D):-      % no change;
%     negations_inside(A,C),            % try rest of
%     negations_inside(B,D).            % formula
% negations_inside(A v B, C v D):-
%     negations_inside(A,C),
%     negations_inside(B,D).
% negations_inside(exists(X,A),exists(X,B)):-
%     negations_inside(A,B).
% negations_inside(forall(X,A),forall(X,B)):-
%     negations_inside(A,B).



% % prenex_normal_form(F1,F2) <- F2 is a PL formula
% %                              with all quant.s in front,
% %                              log. equivalent with F1
% prenex_normal_form(F,PNF):-
%     pnf(F,PNF,B,B).
% pnf(A,V,V,A):-               % base case
%     literal(A).
% pnf(forall(X,F),forall(X,Quants),V,Body):-
%     pnf(F,Quants,V,Body).
% pnf(exists(X,F),exists(X,Quants),V,Body):-
%     pnf(F,Quants,V,Body).
% pnf(A & B,Quants,V,BodyA & BodyB):-
%     pnf(A,Quants,QB,BodyA),
%     pnf(B,QB,V,BodyB).
% pnf(A v B,Quants,V,BodyA v BodyB):-
%     pnf(A,Quants,QB,BodyA),
%     pnf(B,QB,V,BodyB).



% % skolemise(F1,F2) <- F2 is obtained from F1 by replacing
% %                     all existentially quantified
% %                     variables by Skolem terms

% skolemise(F1,F2):-
%     skolemise(F1,[],1,F2).

% skolemise(forall(X,F1),VarList,N,F2):-!,  % remove univ.
%     skolemise(F1,[X|VarList],N,F2).       % quantifier
% skolemise(exists(X,F1),VarList,N,F2):-!,
%     skolem_term(X,VarList,N),             % unify with
%     N1 is N+1,                            % Skolem term
%     skolemise(F1,VarList,N1,F2).
% skolemise(F,V,N,F).                       % copy rest of formula

% skolem_term(X,VarList,N):-
%     C is N+48,                            % number -> character
%     name(Functor,[115,107,C]),            % Skolem functor skN
%     X =.. [Functor|VarList].

% %%%%%%%%%%%%%%%%%%%%% FNC

% conjunctive_normal_form(A,A):-              % base case
%     disjunction_of_literals(A),!.
% conjunctive_normal_form((A & B) v C, D & E ):-!,
%     conjunctive_normal_form(A v C,D),       % distribution
%     conjunctive_normal_form(B v C,E).
% conjunctive_normal_form(A v (B & C), D & E ):- !,
%     conjunctive_normal_form(A v B,D),       % distribution
%     conjunctive_normal_form(A v C,E).
% conjunctive_normal_form(A & B,C & D):-      % conjuction
%     conjunctive_normal_form(A,C),
%     conjunctive_normal_form(B,D).
% conjunctive_normal_form(A v B,E):-          % other cases
%     conjunctive_normal_form(A,C),
%     conjunctive_normal_form(B,D),
%     conjunctive_normal_form(C v D,E).

% %%%%%%%%%%%%%%%%%%%%% Clausal Form

% clausal_form(A,[Clause]):-
%     disjunction_of_literals(A),
%     make_clause(A,Clause).
% clausal_form(A & B,Clauses):-
%     clausal_form(A,ClausesA),
%     clausal_form(B,ClausesB),
%     append(ClausesA,ClausesB,Clauses).

% make_clause(P,([P]:-[])):-
%     logical_atom(P).
% make_clause(-N,([]:-[N])):-
%     logical_atom(N).
% make_clause(A v B,(HeadAB:-BodyAB)):-
%     make_clause(A,(HeadA:-BodyA)),
%     make_clause(B,(HeadB:-BodyB)),
%     append(HeadA,HeadB,HeadAB),
%     append(BodyA,BodyB,BodyAB).

% %%% Disjuncții de literali

% disjunction_of_literals(A):-
%     literal(A).
% disjunction_of_literals(C v D):-
%     disjunction_of_literals(C),
%     disjunction_of_literals(D).

% literal(A):-
%     logical_atom(A).
% literal(-A):-
%     logical_atom(A).

% logical_atom(A):-
%     functor(A,P,N),
%     not logical_symbol(P).

% logical_symbol(=>).
% logical_symbol(<=>).
% logical_symbol(-).
% logical_symbol(&).
% logical_symbol(v).
% logical_symbol(exists).
% logical_symbol(forall).