---
title: "Process prices from a file and calculate the VAT"
author: TILEd by Tanja E.J. Vos
...

# Process prices from a file and calculate the VAT

Implement a `calculate_VAT` function in Python that receives a name from a text file (for example `data.txt`) where the prices without VAT of some items are found. Your function must read these prices, apply VAT (21 $$\%$$) to them and save the values with VAT in a file named `data_VAT.txt`. The data in `data_VAT.txt` must be aligned to the right and with 2 decimal places. In addition to generating the file, your function has to return the name of the generated file.

For example: `calculate_VAT("data1.txt")` returns the string
`"data1_VAT.txt"` which is the name of the generated file:

|||
|------------------------|--------------|------------------------|
| 12.05                   |               |                         |
|   6.70                  |     generates | 14.58                   |
| 123.10                  |               |    8.11                 |
| 333.33                  |               |  148.95                 |
|  25.50                  |               |  403.33                 |
| 100                     |               |   30.86                 |
|   9.95                  |               |  121.00                 |
|                         |               |   12.04                 |
|-------------------------+---------------+-------------------------|


# Metadata

| *Summary*                     |  Process prices from a file and calculate the VAT|
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

