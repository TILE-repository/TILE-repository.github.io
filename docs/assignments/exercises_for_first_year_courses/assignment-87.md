---
title: "Simulating 1000 roles of two dices and calculating the probability percentage"
summary: "Simulating 1000 roles of two dices and calculating the probability percentage."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > dictionaries', 'control flow > conditionals', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Simulating 1000 roles of two dices and calculating the probability percentage


In this exercise you must simulate 1000 rolls of two dice. First,
write a function called `twoDice()`, which simulates throwing 2
six-sided dice. Your function won't take any parameter and will
return the total that was rolled on two dice as the only result.

Then, write a main program that uses this function to simulate the
rolling of two dice 1000 times. As your program runs, you have to
count the number of times each total occurs and save it to a
dictionary. Then it should display a table that summarizes this
data.

On the one hand you have to show the percentage expected by the
probability theory for each total:

```python
expected_probability = 2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
```

The frequency of each total as a percentage of the number of dice
rolls made. The output is shown below.

    **Total**  | **Simulated Percentage**   |  **Expected Percentage**
    -------|------------------------|---------------------
    6     |  14.20                  |  13.89
    8     |  13.70                  |  13.89
    3     |  5.50                   |  5.56
    7     |  18.00                  |  16.67
    2     |  2.40                   |  2.78
    10    |  8.00                   |  8.33
    5     |  10.70                  |  11.11
    9     |  11.50                  |  11.11
    11    |  6.30                   |  5.56
    4     |  7.40                   |  8.33
    12    |  2.30                   |  2.78
