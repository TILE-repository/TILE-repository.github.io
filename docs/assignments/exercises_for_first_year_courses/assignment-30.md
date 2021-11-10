---
title: "Test Informed Learning with Examples assignment"
author: TILEd by Tanja E.J. Vos
...

# Membership card discounts





A book store gives discounts to its customers depending on whether
the customer has the membership card and the price of the purchase
made.

-   below 10 euros no discount is applied to anyone

-   between 10 and 20 euros, a 5% discount is applied when the
    customer has the membership card

-   above 20 euros, a discount of 12% is applied when the customer
    has the membership card, and 6% where there is no card.

Write a program that asks the user by keyboard how much the purchase
is, and whether the customer is a member or not. Depending on these
input data, the program has to show on the screen how much the
customer has to pay for the purchase.

Run the following test cases to ensure that the program works
correctly:

**ID** | **abstract test case**                           | **expected result** 
--------|--------------------------------------------------|---------------------
1      | member with purchase under 10 euros              | discount 0%         
2      | non-member with purchase below 10 euros          | discount 0%         
3      | member with purchase between 10 and 20 euros     | discount 5%         
4      | non-member with purchase between 10 and 20 euros | discount 0%         
5      | member with purchase over 20 euros               | discount 12%        
6      | non-member with purchase over 20 euros           | discount 6%         



We call these test cases *abstract* because, in order to execute
them, we first have to think of concrete values that meet the
conditions of the test case.

```testruntile
Insist that the students test their programs by giving them example
test cases in a table. Also we introduce the concept of abstract vs
concrete test cases.
```

# Metadata

| *Summary*                     | Applying discount rules on purchases. |
| *TILE aspects*                | Test cases and test run TILE-ing is applied. |
| *Topics*                      | Conditional statements, calculating percentages. |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  | Conditional statements, calculating percentages. |
| *Testing learning goals*      | Boundary value testing. |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

