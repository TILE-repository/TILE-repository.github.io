---
title: "Storing customer data"
author: TILEd by Tanja E.J. Vos
...

# Storing customer data

Write a program that allows you to manage the customer data of a
company. This should be stored in a dictionary in which:

-   the key of each client will be their NIF, and

-   the value will be another dictionary with the customer's data
    (name, address, phone, email, VIP), where the customer will have
    the value True if is a VIP customer.

The program should ask the user for an option from the following
menu:

    (1) Add customer,
    (2) Delete customer,
    (3) Show client,
    (4) List all clients,
    (5) List VIP clients,
    (6) Finish.

Depending on the option chosen, the program must to do the
following:

`(1)`

:   Ask for the customer's data, create a dictionary with the that
    information and add it to the database. If a client with the
    same NIF already exists, a message must be displayed indicating
    it.

`(2)`

:   Ask for the customer's NIF and delete their data from the
    database. If a client with this same NIF does not exist, a
    message must be displayed indicating it.

`(3)`

:   Ask for the customer's NIF and show their data. If a client with
    this same NIF does not exist, a message must be displayed
    indicating it.

`(4)`

:   Show the list of all the clients in the database, with their NIF
    and name.

`(5)`

:   Show the list of the VIP clients from the database, with their
    NIF and name.

`(6)`

:   End the program.

You have to test your program well manually, thinking for each
option which would be good test cases to ensure quality testing. For
example, you can do the following interactions:

\-

:   add a VIP client

\-

:   check that it has been added correctly, by using the options
    `(3)`, `(4)` and `(5)`

\-

:   add a non-VIP customer

\-

:   check that it has been added correctly, by using the options
    `(3)`, `(4)` and `(5)`

\-

:   try to add another client with the same NIF, and check that your
    program does not allow it by giving a message

\-

:   add 3 more clients (1 VIP and 2 non-VIP)

\-

:   try to delete a client that does not exist and check that your
    program shows the corresponding message

\-

:   remove a customer that exists

\-

:   check that it has been deleted correctly, by using the options
    `(3)`, `(4)` y `(5)`

\-

:   end the program with `(6)`






# Metadata

| *Summary*                     | Storing customer data |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

