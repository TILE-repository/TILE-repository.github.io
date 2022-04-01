---
title: "Storing customer data - part two"
summary: "Storing customer data - part two."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables > variable declaration', 'imperative programming > variables > assignment']"
concepts practised: "['data > types (built-in) > composite > dictionaries', 'control flow > conditionals', 'control flow > loops']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Storing customer data - part two

The problem with the [Storing customer data](exercises_for_first_year_courses/assignment-89.md) assignment is that each time the program is launched, the data would have to be entered again. To avoid this,
we are going to create two new options that allow us to use files as
backup copies of the data in the dictionary. The menu for the user
with the options will be as shown below:

    (1) Add customer,
    (2) Delete customer,
    (3) Show client,
    (4) List all clients,
    (5) List VIP clients,
    (6) Save to file,
    (7) Read data from file,
    (8) Finish.

The option `(6)` will store the data in a file. Selecting this
option will save the current dictionary data in the customer.txt
file in the following format:

```small
nif; name; address; telephone; email; vip
1234;Michael Myers;2704 Hickman Street;203-355-7551;mm@f.com;True
2345;Marilyn Scott;2834 Washington Street;361-346-8703:ms@f.com:False
```

The option `(7)` will do the opposite operation. It will read the
data from the customer.txt file and store it in the dictionary
(removing all previous data from the dictionary).

Now, the option to terminate will be the `(8)`.

To test your program, run the tests from the previous exercise, but
before ending the program choose the option `(7)`. Then, open the
saved file to check that the content matches the clients.
