% Utilizam relatiile de la LAB1, EX2

female(mary).
female(sandra).
female(juliet).
female(lisa).
male(peter).
male(paul).
male(dony).
male(bob).
male(harry).
parent(bob, lisa).
parent(bob, paul).
parent(bob, mary).
parent(juliet, lisa).
parent(juliet, paul).
parent(juliet, mary).
parent(peter, harry).
parent(lisa, harry).
parent(mary, dony).
parent(mary, sandra).

is_father_of(Father, Child) :- parent(Father, Child), male(Father).
is_mother_of(Mother, Child) :- parent(Mother, Child), female(Mother).

is_grandfather_of(Grandfather, Child) :- parent(Grandfather, X), male(Grandfather), parent(X, Child).
is_grandmother_of(Grandmother, Child) :- parent(Grandmother, X), female(Grandmother), parent(X, Child).

is_sister_of(Sister, Person) :- parent(X, Sister), parent(X, Person), female(Sister).
is_brother_of(Brother, Person) :- parent(X, Brother), parent(X, Person), male(Brother).

is_aunt_of(Aunt,Person) :- is_sister_of(Aunt, X), parent(X, Person).
is_uncle_of(Uncle,Person) :- is_brother_of(Uncle, X), parent(X, Person).

% Vizualizăm atributele female, male, parent
% is_grandmother_of(julliet, harry).        (true)
% is_sister_of(lisa, paul).                 (true)
% is_sister_of(paul, lisa).                 (false) - Întrebăm dacă Paul este SORA Lisei, ceea ce e fals.

is_ancestor_of(X, Y) :- parent(X, Y).
is_ancestor_of(X, Y) :- parent(X, Z), is_ancestor_of(Z, Y).