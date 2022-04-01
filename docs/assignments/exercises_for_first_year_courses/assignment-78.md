---
title: "Creating files with a random number of random numbers"
summary: "Creating files with a random number of random numbers."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > sequences > strings', 'io > files > text > plain']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Creating files with a random number of random numbers

Write a Python program that allows you to generate a certain number of files with a random number (between 1 and 10) of random real numbers (between 1.00 and 200.00). The numbers must be aligned to the right and with 2 decimal places. You can import `random` and use `randint` to randomly generate integers, and `uniform` to randomly generate real numbers.

Your program:

-   first it must ask the user for the number of files he wants to
    generate

-   then it asks for the name to use as the base of the generated
    files. For example, if the user wants 5 files with base name
    `file`, the program will generate the files `file1.txt`,
    `file2.txt`, ..., `file5.txt`.

For example:

```small
>>> %Run 
    How many files?: 4
    What is the base name?: file
>>> 
```

It can generate for example:

| **file1** | **file2** | **file3** | **file4** |
|-----------|-----------|-----------|-----------|
| 133.25    | 29.92     | 50.08     | 6.64      |
| 159.93    | 199.44    | 59.34     | 136.33    |
| 162.02    | 158.01    | 109.88    | 32.02     |
| 23.26     | ...       | 153.48    | 56.16     |
| 147.50    |           | 195.16    | 97.67     |
| ...       |           | 51.95     | 160.56    |
|           |           | 86.55     | ...       |
|           |           | 153.28    |           |
|           |           | ...       |           |
