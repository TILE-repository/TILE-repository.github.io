---
title: "Shopping cart"
author: TILEd by Tanja E.J. Vos
...

# Shopping cart

Write a program that creates a dictionary that simulates a shopping
cart. The program must ask for the item and its price, and add the
pair to the dictionary, until the user decides to finish. Then, the
shopping list and the total cost should be displayed, as in the
following example:

```small
>>> %Run 
    Enter a product: beer
    Enter its price: 1.50
    
    Do you want to continue? (Y/N): Y
    Enter a product: wine
    Enter its price: 4.50
    
    Do you want to continue? (Y/N): Y
    Enter a product: seed pack
    Enter its price: 1.00
    
    Do you want to continue? (Y/N): Y
    Enter a product: fruit
    Enter its price: 8
    
    Do you want to continue? (Y/N): N
    
    Product        Price
    --------------------
    beer           1.50€
    wine           4.50€
    seed pack      1.00€
    fruit          8.00€
    --------------------
    Total         15.00€
```

You can assume that the user only adds 1 sample of each product.
Your tests can be run through the shell manually.






# Metadata

| *Summary*                     | Shopping cart |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

