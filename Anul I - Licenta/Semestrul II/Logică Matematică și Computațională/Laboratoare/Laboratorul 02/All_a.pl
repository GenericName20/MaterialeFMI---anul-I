all_a([a | []]). % [a] este [a | []]
all_a([a | TAIL]) :- all_a(TAIL).

% ?- all_a([a,b,a]).
% false.

% ?- all_a([a,a,a]).
% true.

% ?- all_a([a,a,A]).
% A = a