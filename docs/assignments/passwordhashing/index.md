---
title: "Password hashing"
author: Niels Doorn
...

# Password Hashing
{:.no_toc} 
 
By [Niels Doorn](https://research.nielsdoorn.nl/).

- Table of contents
{:toc}

## Hashing

Hashing is a mathematical algorithm that maps data of arbitrary size (often called the “message”) to a bit array of a fixed size (the “hash value”, “hash”, or “message digest”). It is a one-way function, that is, a function which is practically infeasible to invert. It is often used to store passwords, for example of users of a website.

Hashes are often subject to attacks to gain access to computer systems. Attackers often use sets of calculated hashes known as *rainbow tables*. These tables contain hashes of common used passwords such as dictionary words or often used password such as “Welcome123”, “qwertyuiop” and “123456” (the most often used password in 2020). Using pre-calculated hashes is much more effective then brute-force attacks. To improve security of hashes, salting can be used. A a large random value is added to the password before calculating the hash. This value is called the *salt*. This makes hashes much more difficult to crack using rainbow table attacks since an attacker would have to generate rainbow tables for every given salt. The salt can be stored in plain text along with the hashed value [^1].

One of the algorithms used to create hashes is Message Digest Algorithm 5 (MD5). For this algorithm, cases are known where multiple inputs where found for a single output. These are called *hash-collisions*. Because of this, MD5 is considered to be an unsafe choice for hashing sensitive data like passwords. There are many more hashing algorithms which are safer, but many of them have (other) security problems as well.

## Learning goals

General computer science learning goals:

-   Hashing techniques.
-   Brute-force attacks.

Testing domain learning goals:

-   Learn about testing for security.
-   Testing for intermittent problems.
-   Handling random data.
-   Using pytest
-   Debugging strategies

Programming learning goals:

-   Reading from a file and processing the contents.
-   Handling comma-separated values.
-   Handling Strings and white space.
-   Using external libraries for hashing.
-   Applying a hashing algorithm.

Prerequisites:

-   Variables
-   Conditional statements (if/else)
-   Loops

## Didactic approach

Let’s Look at this assignment from a didactic perspective. What are the obstacles students might encounter before they can confidently start with this assignment.

-   If we give a short description of hashing, without the details such as the fixed length of hashes and the in-reversibility of them, we could present the table with passwords, salts and hashes and discuss what the students see to discover these properties.
-   Students could design a hashing function in pairs, using basic mathematics, maybe with a given interface and test file.
-   Discuss possible attack vectors [^2], and potential problems like random number generators [^3], leading to explaining/discussing rainbow tables.
-   Discuss the concept of salting and brainstorm about ways to apply salting [^4].
-   Than we could present the assignment.

## Assignment: Notsuchasafebank has a problem

The website of “Notsuchasafebank”, a large global financial institute, has a registration function for users. Users are required to choose a secure password and use their e-mail address as the user name. The website system uses an MD5 algorithm to hash the passwords, together with a salt as additional data to improve security.

However, the systems seems to be defective. Every now and then, the salt is **not** applied to the password, making the system unsafe. One of the lead dev-ops engineers at Notsuchasafebank, Marike, managed to produce a file with the passwords, salts and hashes for you to debug this problem.

The file contains example values separated by semicolons, the first line contains the value types. Here is an example of a few lines of the data of the file in a table:

Password                             Salt           Hash
------------------------------------ -------------- ----------------------------------
FiremanshipNoisyStirrup-shaped       Etiologic      d252f331a8924d54e1c352f88decccb4
QuizzeryNonemotionallyPediments      Tenpins        83abc62b14f585636f547717c076b209
UnguentariumZinciteStirrup-shaped    Unguentarium   27fed6fa4ae5c4ebc47468d51fc95f93
HeardCuratoriallyRyegrasses          Dismayed       5961aa9c671f1d7d58d2f90ecfd143b8
DraftsmenDecemberistImmoderate       Agentive       f94f1e45f8ccc708741d42aee4c10c1c
NontheatricalWood-culverCavilling    Fusilladed     33609348393312bb584368cb60e3a5df
QuizzeryBelligerencyUnchangingness   Cacophony      f4da2cc176a354e599f5abe2f3ff7f05
OxbowsAllurementsField-kirk          Veray          64c934dd49db61abbc47a23a30d5011d

The data of the file is structured as follows:

-   The first field is the password in plain text.
-   The second field is the salt, a random value which is added to the password before calculating the hash.    
-   The last field is the calculated hash.

Marike asked you to write a program to analyse this data and to determine **how many** passwords where not properly salted and hashed.

The last line of the file contains the correct answer which you can use to verify your solution. Use to verify if your answer is correct.

## Solution example

The file , which is listed below, is a possible solution using to verify the answer with the answer from the password file. It can be used to automate the process of checking the students answers or be discussed with the students afterwards.

```python   
import hashlib

def testPasswordFile(): 
    # open the file for reading 
    f = open(“hashes.txt”, “r”)

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
        fields = line.split(’;’) 
        password = fields[0] 
        salt = fields[1] 
        hash = fields[2].strip()

        # check if the salt was used to calculate the hash 
        hashWithSalt = hashlib.md5((password+salt).encode(’utf-8’)).hexdigest() 
        if (hash == hashWithSalt): 
            hashedAndSalted += 1

    verification = int(lastline.split()[-1])

    # test if the answer matches the verification of the file 
    assert hashedAndSalted == verification
```

This file can be run using :

```bash
% pytest -q test_hashing.py
.                                                                        [100%]
1 passed in 0.01s
```

### Generator for the password files

This assignment can easily be used to create individual versions by using the generator below.

For the lecturer to generate password files the following code can be used:

```python
import hashlib 
import random 
from random_word import RandomWords

f = open(“hashes.txt”, “w”)
random.seed() 
rw = RandomWords()

listOfRandomWords = rw.get_random_words(limit=400)

hashedAndSalted = 0 
f.write(“password;salt;hash”) 
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
        hashValue = password
    hash = hashlib.md5(hashValue.encode(’utf-8’)).hexdigest() 
    f.write(password+“;”+salt+“;”+hash+“”)

f.write(“Number of passwords that were hashed and salted: ”+str(hashedAndSalted))
```

A generated password file looks like this:

```text
password;salt;hash
ManneristRetainingImpoverishment;Nixon;637def60ff4f11a5f5c63aba08915a47
DemilitarizeSemi-wildRomansh;Godsend;d6907b99b08b967167905df0fce8ee36
(truncated)
TrustfulEbullienceMetallicity;Repave;a3b795df7241ecfdd0329be0a777cda0
AmphetaminesPoddyOutreached;Aquino;6dc91f9cff5bc841416437b176867488
Number of passwords that were hashed and salted: 78
```

## Possible adaptations

By creating unique versions of the password file for each student, copy-pasting code from other students is (a bit) discouraged. It is possible to discourage this even more by using different hashing algorithms as well such as .

In this assignment, students have to count the occurrences of defective hashes. The defective hashes are created randomly. We could make is more interesting to truly introduce a defect in the code, for example, all passwords longer then 20 characters are not salted. Or, all passwords containing the letter Q are not salted. The students could then try to find such patterns and discover the defect of the salting algorithm of the website. To do so, they could separate the defective entries and the correct entries and look for patterns.

## Metadata

| *Summary*         | Understanding hashing techniques |
| *TILE aspects*    | What are the TILE aspects in this assignment. |
| *Topics*          | Hashing. |
| *Audience*        | CS1/CS2 |
| *Learning goals*  | Testing for security, intermittent problems, random data, comma-separated values, strings and white space, using external libraries for hashing. |
| *Prerequisites*   | Variables, conditional statements, loops. |
| *Variants*        | This assignment can be adapted to use different algoritms, other (complicated) defects and more.  |

## References

[^1] J. J. Hoch en A. Shamir, “On the Strength of the Concatenated Hash Combiner When All the Hash Functions Are Weak”, in Automata, Languages and Programming, 2008, bll 616–630.
[^2] N. Mouha, M. S. Raunak, D. R. Kuhn, en R. Kacker, “Finding Bugs in Cryptographic Hash Function Implementations”, IEEE Transactions on Reliability, vol 67, no 3, bll 870–884, 9 2018.
[^3] A. Rukhin, J. Soto, J. Nechvatal, M. Smid, en E. Barker, “A statistical test suite for random and pseudorandom number generators for cryptographic applications”, Booz-allen and hamilton inc mclean va, 2001.
[^4] P. Gauravaram, “Security Analysis of salt||password Hashes”, in 2012 International Conference on Advanced Computer Science Applications and Technologies (ACSAT), 2012, bll 25–30.