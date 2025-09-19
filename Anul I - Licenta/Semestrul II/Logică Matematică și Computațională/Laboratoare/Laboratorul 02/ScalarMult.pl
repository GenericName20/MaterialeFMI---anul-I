scalarMult(_, [], []).
scalarMult(X, [Head | Tail], [HeadRes | TailRes]) :-
    HeadRes is X * Head,                % Head result
    scalarMult(X, Tail, TailRes).       % Tail result

% ?- scalarMult(3,[2,7,9],Result).
% Result = [6, 21, 27] 