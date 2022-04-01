---
title: "Shopping cart"
summary: "Shopping cart."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > dictionaries', 'control flow > conditionals', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
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
