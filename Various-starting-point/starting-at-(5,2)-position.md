# Starting at (5,2) position in maze

Each of the paths yielded in this round of testing has a detour to the (1,1) position.

![Figure: ...](../img/start-at-5-2/start@-5,2-not-direct-manouvre3.png)

The 192-step path below cost an extra 7 steps of code due to the little loop: _(5,2) -> (5,1) and back to (5,2)_.

![Figure: ...](../img/start-at-5-2/start@-5,2-not-direct-manouvre4.png)

The reason why the 195-step path in the picture below costs more steps of code compared is not noticiable from the pictures.

The 3 additional steps of code spent are due to an odd extra spin Reeborg performs at the (3,1) position.

![Figure: ...](../img/start-at-5-2/start@-5,2-not-direct-manouvre4~.png)

The difference of 4 steps of code between the 199-step path depicted below and the 195-step path seen above is attributable to:

- The odd spin performed at the (4,5) position.
- The number of `move()` functions executed in the subpath -- _(4,3) -> (4,4) -> (2,4) -> (2,5) -> (3,5)_ -- is 5, while it is 3 for the subpath -- _(4,3) -> (3,3) -> (3,5)_.

![Figure: ...](../img/start-at-5-2/start@-5,2-not-direct-manouvre.png)

The difference of 8 steps of code observed between the 207-step path below and the 199-step code above is due to:

- The _turn right_ manoeuvre at the (5,1) position.
- As well as some bizarre spinning around at a position like (3,1).

![Figure: ...](../img/start-at-5-2/start@-5,2-not-direct-manouvre2.png)

[<< Previous starting point](<starting-at-(5,1)-position.md>)

\ \ -------- ... -------- / / [Next starting point >>](<starting-at-(4,2)-position.md>)
