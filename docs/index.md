---
title: "Nifty TILE Assignments"
...

# Nifty TILE Assignments

By Niels Doorn [^1], Tanja Vos [^2] and Beatriz Marín [^3]

## Introduction

Test Informed Learning with Examples (TILE), is a new approach to introduce software testing in introductory programming courses in the following ways:

early 
:	introduce students to testing from the very first example program they see and write themselves in exercises;

seamless 
:	testing will be introduced in a smooth and continuous way as an inherent part of programming, and not as a separate activity;

subtle
:	we will make use of clever and indirect methods to teach them testing knowledge and skills.


## Background

Test Informed Learning with Examples was inspired by Test-driven learning (TDL). 
TDL was coined in 2006 by Janzen and Saiedian [^4]. 
It describes a pedagogical approach to teaching computer programming that involves introducing and exploring new programming concepts using examples and exercises that evolve around testing. 
When teaching programming many examples are being given, programming is often learned through examples. 
Examples related to testing take the same effort to present than other examples.
Janzen et. al. [^5] [^6] continued their work more in the direction of Test Driven Development (TDD) such they diverted from their initial TDL ideas. 
As a consequence, at this moment, there does not exist a clearly defined approach that can be used by any teacher to effortless introduce TDL in their programming course. 
To fill this gap, we developed TILE, Test Informed Learning with Examples.

## Types of TILES

There are three main types of TILES:

test run TILES
:	tiles in students are encouraged to write tests

test cases TILES
:	dafdsf

test domain TILES
:	dafsdf

## TILES of each type

We provide some assigments of each type of the approach.

### A test run TILE: Password hashing

#### Introduction into hashing

Hashing is a mathematical algorithm that maps data of arbitrary size (often called the "message") to a bit array of a fixed size (the "hash value", "hash", or "message digest"). 
It is a one-way function, that is, a function which is practically infeasible to invert. 
It is often used to store passwords, for example of users of a website.

Hashes are often subject to attacks to gain access to computer systems. 
Attackers often use sets of calculated hashes known as *rainbow tables*.
These tables contain hashes of common used passwords such as dictionary words or often used password such as "Welcome123", "qwertyuiop" and "123456" (the most often used password in [2020](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)).
Using pre-calculated hashes is much more effective then brute-force attacks.
To improve security of hashes, salting can be used.
A a large random value is added to the password before calculating the hash.
This value is called the *salt*.
This makes hashes much more difficult to crack using rainbow table attacks since an attacker would have to generate rainbow tables for every given salt.
The salt can be stored in plain text along with the hashed value [@Hoch2008].

One of the algorithms used to create hashes is [!MD5]. 
For this algorithm, cases are known where multiple inputs where found for a single output. 
These are called *hash-collisions*.
Because of this, [!MD5] is considered to be an unsafe choice for hashing sensitive data like passwords.
There are many more hashing algorithms which are safer, but many of them have (other) security problems as well.

#### Learning goals

General computer science learning goals:

- Hashing techniques.
- Brute-force attacks.

Testing domain learning goals: 

- Learn about testing for security.
- Testing for intermittent problems.
- Handling random data.
- Using pytest
- Debugging strategies

Programming learning goals:

- Reading from a file and processing the contents.
- Handling comma-separated values.
- Handling Strings and white space.
- Using external libraries for hashing.
- Applying a hashing algorithm.

Prerequisites:

- Variables
- Conditional statements (if/else)
- Loops

#### The Assignment: Notsuchasafebank has a problem

The website of "Notsuchasafebank", a large financial institute, has a registration function for users.
Users are required to choose a secure password and use their e-mail address as the user name.
The website system uses an [MD5](https://nl.wikipedia.org/wiki/MD5) algorithm to [hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function) the passwords, together with a [salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) as additional data to improve security.

However, the systems seems to be defective.
Every now and then, the salt is **not** applied to the password, making the system unsafe.
One of the lead dev-ops engineers at Notsuchasafebank, Marike, managed to produce a file with the passwords, salts and hashes for you to debug this problem.

The file contains example values separated by semicolons, the first line contains the value types.
Here is an example of a few lines of the data of the file in a table:

| Password                           | Salt         | Hash                             |
|------------------------------------|--------------|----------------------------------|
| FiremanshipNoisyStirrup-shaped     | Etiologic    | d252f331a8924d54e1c352f88decccb4 |
| QuizzeryNonemotionallyPediments    | Tenpins      | 83abc62b14f585636f547717c076b209 |
| UnguentariumZinciteStirrup-shaped  | Unguentarium | 27fed6fa4ae5c4ebc47468d51fc95f93 |
| HeardCuratoriallyRyegrasses        | Dismayed     | 5961aa9c671f1d7d58d2f90ecfd143b8 |
| DraftsmenDecemberistImmoderate     | Agentive     | f94f1e45f8ccc708741d42aee4c10c1c |
| NontheatricalWood-culverCavilling  | Fusilladed   | 33609348393312bb584368cb60e3a5df |
| QuizzeryBelligerencyUnchangingness | Cacophony    | f4da2cc176a354e599f5abe2f3ff7f05 |

Table: Passwords, their salts and hashes of Notsuchasafebank.

The data of the file is structured as follows:

- The first field is the password in plain text.
- The second field is the salt, a random value which is added to the password before calculating the hash.
- The last field is the calculated hash.

Marike asked you to write a program to analyse this data and to determine **how many** passwords where not properly salted and hashed.

**remark**:

The last line of the file contains the correct answer which you can use to verify your solution.
Use `pytest` to verify if your answer is correct.


#### Example Solution

The file `hashingTest.py`, which is listed below, is a possible solution using `pytest` to verify the answer with the answer from the password file.
It can be used to automate the process of checking the students answers or be discussed with the students afterwards.

```python
import hashlib

def testPasswordFile():
    # open the file for reading
    f = open("hashes.txt", "r")

    # read all lines except the first line, which contains the header, into a list of lines
    lines = f.readlines()[1:]

    # store the last line with the verification answer in a variable
    lastline = lines[len(lines)-1]

    # remove the last line, which contains the verification answer, from the list of lines
    lines = lines[:-1]
    
    # keep a record of all correctly hashed passwords
    hashedAndSalted = 0

    # process all lines with passwords, salts and hashes
    for line in lines:
        # seperate the fields for each line
        fields = line.split(';')
        password = fields[0]
        salt = fields[1]
        hash = fields[2].strip()

        # check if the salt was used to calculate the hash
        hashWithSalt = hashlib.md5((password+salt).encode('utf-8')).hexdigest()
        if (hash == hashWithSalt):
            hashedAndSalted += 1

    verification = int(lastline.split()[-1])

    # test if the answer matches the verification of the file
    assert hashedAndSalted == verification
```

This file can be run using `pytest`:

```zsh
% pytest -q test_hashing.py
.                                                                        [100%]
1 passed in 0.01s
```

#### Supportive material: A generator for the password files

This assignment can easily be used to create individual versions by using the generator below.

For the lecturer to generate password files the following code can be used:

```python
import hashlib
import random
from random_word import RandomWords

f = open("hashes.txt", "w")
random.seed()
rw = RandomWords()

listOfRandomWords = rw.get_random_words(limit=400)

hashedAndSalted = 0
f.write("password;salt;hash\n")
for i in range(100):
    password = ''
    for j in range(0, 3):
        password += listOfRandomWords[random.randint(0, len(listOfRandomWords) - 1)].capitalize()

    salt = listOfRandomWords[random.randint(0, len(listOfRandomWords) - 1)].capitalize()
    r = random.randint(0, 100)

    if r % 5 != 0:
        # hash and salt
        hashedAndSalted += 1
        hashValue = password + salt;
    else:
        # oops, forgot to salt
        hashValue = password;
    hash = hashlib.md5(hashValue.encode('utf-8')).hexdigest()
    f.write(password+";"+salt+";"+hash+"\n")

f.write("Number of passwords that were hashed and salted: "+str(hashedAndSalted))
```

A generated password file looks like this:

```default
password;salt;hash
ManneristRetainingImpoverishment;Nixon;637def60ff4f11a5f5c63aba08915a47
DemilitarizeSemi-wildRomansh;Godsend;d6907b99b08b967167905df0fce8ee36
(truncated)
TrustfulEbullienceMetallicity;Repave;a3b795df7241ecfdd0329be0a777cda0
AmphetaminesPoddyOutreached;Aquino;6dc91f9cff5bc841416437b176867488
Number of passwords that were hashed and salted: 78
```

#### Possible adaptations

By creating unique versions of the password file for each student, copy-pasting code from other students is discouraged.
It is possible to discourage this even more by using different hashing algorithms such as `SHA-1`.

In this assignment, students have to count the occurrences of defective hashes.
The defective hashes are created randomly.
We could make is more of a testing excersise to truly introduce a defect in the code, for example, all passwords longer then 20 characters are not salted.
Or, all passwords containing the letter Q are not salted.
The students could then try to find such patterns and discover the defect of the salting algorithm of the website.
To do so, they could separate the defective entries and the correct entries and look for patterns.
However, this is not the aim of TILE, which is to incorporate testing into programming and not convert programming courses into testing courses.

### Two

### N

## Metadata

| Summary 		| Test Informed Learning by Example (TILE) based assignments. |
| Topics 		| Testing, programming. |
| Audience 		| Appropriate for a CS1 course. |
| Difficulty 	| These are assignments for novice computer science students, but TILE can be used for more advanced assignments as well. |
| Strengths 	| TILE offers the potential of teaching testing "for free" as early as possible without adding any additional strain on the course schedule. |
| Weaknesses 	| Whilst the teaching doesn't put strain on the course schedule, this approach does require effort to change existing course material in order to apply. We aim to reduce this effort by providing an open databank with assignments. |
| Dependencies 	| This approach integrated into existing programming courses. |
| Variants 		| We identified three main type of TILES, however, this taxonomy can be extended into sub-types or other main types. |


## Acknowledgements

This work was funded by the Erasmus+ project QPeD under contract number 2020-1-NL01-KA203-064626.

## Footnotes                                                                                    

[^1]: [niels.doorn@ou.nl](mailto:niels.doorn@ou.nl)
[^2]: [tanja.vos@ou.nl](mailto:tanja.vos@ou.nl)
[^3]: [bmarin@dsic.upv.es](mailto:bmarin@dsic.upv.es)
[^4]: [Test-driven learning: intrinsic integration of testing into the CS/SE curriculum](http://dl.acm.org/citation.cfm?id=1121419)
[^5]: [Test-driven learning in early programming courses](https://dl.acm.org/doi/10.1145/1352322.1352315) 
[^6]: [Implications of integrating test-driven development into CS1/CS2 curricula](https://dl.acm.org/doi/10.1145/1508865.1508921) 