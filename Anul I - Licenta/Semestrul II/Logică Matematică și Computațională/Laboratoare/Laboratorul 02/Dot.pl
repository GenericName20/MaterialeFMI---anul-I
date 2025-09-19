dot([],[],0).
dot([H1|T1], [H2|T2], HeadRes) :-
    dot(T1, T2, TailRes),
    HeadRes is H1 * H2 + TailRes.

% ?- dot([1,2,3],[1,2,3],R).
% R = 14.