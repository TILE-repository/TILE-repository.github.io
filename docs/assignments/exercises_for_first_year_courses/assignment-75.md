---
title: "Saving names and birth dates to a file"
summary: "Saving names and birth dates to a file."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables']"
concepts practised: "['data > types (built-in) > composite > sequences > strings', 'control flow > loops', 'io > files > text > plain']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Saving names and birth dates to a file

Make an interactive program in Python that asks for the number of people to store, and from each one of them asks for the following data by keyboard: day, month and year of birth (integers) and name of the person (String). Then it must store it in a file called `"dates.txt"` with the following format:

```small
12 03 1996 | Hira Sadler
    16 05 1997 | Roman Connelly
    08 10 1976 | Alexandre Bullock
    04 03 2010 | Tracy Kendall
```

The above file has resulted from the following interactive session:

```small
>>> %Run 
    Number of people to store: 4
    
    Give the data for person 1:
    Day: 12
    Month: 3
    Year: 1996
    Name: Hira Sadler
    
    Give the data for person 2:
    Day: 16
    Month: 5
    Year: 1997
    Name: Roman Connelly
    
    Give the data for person 3:
    Day: 8
    Month: 10
    Year: 1976
    Name: Alexandre Bullock
    
    Give the data for person 4:
    Day: 4
    Month: 3
    Year: 2010
    Name: Tracy Kendall
    
    The file "dates.txt" has been generated.
>>>
```