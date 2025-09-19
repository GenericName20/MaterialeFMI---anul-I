max([], 0).
max([Head | Tail], M) :- 
    max(Tail, M1), Head > M1, M is Head.
max([Head | Tail], M) :-
    max(Tail, M1), Head < M1, M is M1.

% ?- max([10,4,15,2,8],R).
% R = 15 