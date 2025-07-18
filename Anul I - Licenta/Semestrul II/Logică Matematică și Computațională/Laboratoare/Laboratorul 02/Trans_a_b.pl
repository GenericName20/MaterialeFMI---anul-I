trans_a_b([], []).
trans_a_b([a | TailA], [b | TailB]) :- trans_a_b(TailA, TailB).

% ?- trans_a_b([a,a,a], L).
% L = [b, b, b].

% ?- trans_a_b([a,a,a],[b]).
% false.

% ?- trans_a_b(L,[b,b]).       
% L = [a, a].