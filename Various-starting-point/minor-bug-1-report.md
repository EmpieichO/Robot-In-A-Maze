# Minor bug alert!

As depicted in the figure below, there is a minor bug in this code, which occurs only after Reeborg has successfully reached the destination.

## Why the bug occurs?

Short answer: The bug occurs because the code does not enable Reeborg to check that he has reached the destination.

![Figure: ...](../img/start-at-5-4/start-5,4-facing-flag-BUG-001.png)

### Step by step analysis

The bug occurs in the scenario where Reeborg starts off at the (5,4) grid position while facing the exit.

Since there is no wall in front, he moves forward through the exit, and reaches the destination.

The lines of code executed thus far are the lines 27, 28 and 29. That is:

```
while not at_goal():
    if not wall_in_front():
        move()
```

After executing line 29, Reeborg reaches the destination and the `at_goal()` condition is `True`.

However, the next line of code does not check if the `at_goal()` condition is `True` or `False`.

Execution then continues with lines 30 to 33:

```
        if not wall_on_right():
            turn_right()
            if not wall_in_front():
                move()
```

So, since there is no wall on the right, Reeborg turns right.

And after turning right, since there is no wall in front, he moves forward into the mud.

See the fix in [fix-minor-bug-1](fix-minor-bug-1.md)

---

\ \ -------- ... -------- / / [Next starting point >>](<starting-at-(3,2)-position.md>)
