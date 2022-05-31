---
title: "Shopping calculator"
summary: "Shopping calculator."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['expressions > operators > arithmetic operators', 'control flow > conditionals']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Shopping calculator






We want to format a shopping list for a party with the following
products: beer, wine and chips. You have to ask the user for the
prices of the 3 products (we assume that they are always $$< 10$$
euros), and the quantities they want to buy (we assume that they are
always $$<100$$ units). The program must return the purchase itemized
as follows:

```small
>>> %Run 
    Beer price? 9.99
    Wine price? 1.05
    Chips price? 4
    How much beer? 99
    How much wine? 23
    How many bags of chips? 1
    --------------------------
    Total purchase
    --------------------------
    Beer           99   989.01
    Wine           23    24.15
    Chips          01     4.00
                        -----
                Total  1017.16
```

You have to do 2 different implementations of your program. One
using the String module operator % to format, and another with the
`str.format()`. Test your program with different prices ($$<10$$
euros) and quantities ($$<100$$ units) to test that the layout is
always aligned.

```testruntile
We added one sentence explicitly asking the students to test with
some values and check the output.
