% Distanta dintre doua puncte pe plan XoY

distance((X1, Y1), (X2, Y2), D) :- D is sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2).