% Knowledge base
likes(john, mary).
likes(john, ice_cream).
likes(mary, chocolate).

% Rule 1: If someone likes ice cream and chocolate, they have a sweet tooth.
sweet_tooth(X) :- likes(X, ice_cream), likes(X, chocolate).

% Rule 2: If someone likes someone else, they may have a crush on them.
crush(X, Y) :- likes(X, Y).

% Queries
?- sweet_tooth(john).
% Expected output: true.

?- crush(john, X).
% Expected output: X = mary.