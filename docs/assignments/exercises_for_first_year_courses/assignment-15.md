---
title: "Test Informed Learning with Examples assignment"
author:  Tanja E.J. Vos
...

# Shopping calculator

By [Tanja E.J. Vos](https://www.tanjavos.com).

------------------------------------------------------------------------

Python exercises used for first year programming courses that
have been adapted by using Test Informed Learning with Examples (TILE)
to integrate testing in programming education without it costing (much)
more time. The coloured boxes indicate how they were TILEd.

```testdomaintile
This colour box explains a TILE in the test domain.
```

```testruntile
This colour box explains a TILE related to test runs 
and/or test cases.
```
------------------------------------------------------------------------

# Assignment


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
```


# Metadata

| *Summary*                     | Shopping calculator |
| *TILE aspects*                | Test run TILE-ing is applied. |
| *Topics*                      | Conditional statements, string formatting, number formatting. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Conditional statements. |
| *Testing learning goals*      | Test case design to test the layout. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. |    