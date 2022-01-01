---
title: "DNI number calculation"
author: TILEd by Tanja E.J. Vos
...

# DNI number calculation

Write a function (`dniLetter`) that, given a DNI number, returns the letter that corresponds to it. The algorithm to calculate the control letter of a DNI is the following:

-   Find the remainder by dividing the number by 23

-   The letter is obtained using the remainder as index of the following table:

REMAINDER  | 0  | 1  | 2  | 3  | 4 |  5 |  6 |  7 |  8 |  9 |  10  | 11
-----------| ---| ---| ---| ---| ---| ---| ---| ---| ---| --- |---- |----
LETTER   |  T |  R  | W  | A |  G |  M |  Y |  F  | P |  D  | X  |  B

REMAINDER |  12 |  13 |  14 |  15  | 16  | 17  | 18 |  19 |  20  | 21 |  22
-----------| ----| ----| ----| ----| ----| ----| ----| ---- |----|----| ----
LETTER   |  N  |  J  |  Z   | S  |  Q  |  V  |  H   | L  |  C  |  K  |  E

Complete the table with the number of rows you consider necessary to design your test set and run the automatic tests with pytest.\

**test case number**  |**input** |  **expected output**
------------------ |------- |-----------------
1                 |      |  
2                 ||         
3                 ||         
4                  ||        
5                 ||         
6                 ||   


# Metadata

| *Summary*                     |  |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

