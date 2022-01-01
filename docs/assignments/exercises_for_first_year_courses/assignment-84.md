---
title: "Convert a text to a dictionary of words"
author: TILEd by Tanja E.J. Vos
...

# Convert a text to a dictionary of words

Write a function called `text_to_dic` that receives a text as an
argument. It must create and return a dictionary where the keys are
the words in the text, and their values are the number of
occurrences of each of these in the text.

Use the function you just wrote to define a function called
`file_to_dic` that receives the name of a text file and returns a
dictionary where the keys are the words of the text in the file and
its values the number of appearances of each of these in the text of
the file.

Don't forget your documentation and pytests. To facilitate the
creation of your test cases, in Poliformat there is a `text.txt`
file that contains the following dictionary:

```python
'Es': 13, 'un': 52, 'hecho': 13, 'hace': 11, 'tiempo': 8, 'que': 23, 'lector': 9, 'mira': 13, 'el': 11, 'de': 26, 'texto': 13, 'sitio': 11, 'mientras': 9, 'que.': 3, 'contenido': 10, 'mira.': 10
```

A histogram is a graphical representation of a variable in the form
of bars, where the area of each bar is proportional to the frequency
of the values represented. They are used to obtain a general "first
view" or panorama of the distribution of the population, or of the
sample, regarding a characteristic, quantitative and continuous
(such as length or weight) (see
<https://es.wikipedia.org/wiki/Histograma>).

Write a function `ascii_histogram` that receives as an argument a
dictionary with keys of type string and values of type int, and
returns an ASCII histogram that uses the Python output format. An
example is below:

```small
>>> ascii_histogram(file_to_dic("text.txt"))
                Es +++++++++++++
                un ++++++++++++++++++++++++++++++++++++++++++++++++++++
            hecho +++++++++++++
            hace +++++++++++
            tiempo ++++++++
            que +++++++++++++++++++++++
            lector +++++++++
            mira +++++++++++++
                el +++++++++++
                de ++++++++++++++++++++++++++
            texto +++++++++++++
            sitio +++++++++++
        mientras +++++++++
            que. +++
        contenido ++++++++++
            mira. ++++++++++
```

Create a test case to test the function `ascii_histogram` that
returns as expected result:

```small
>>> ascii_histogram(dic)
                0 
                1 +
                2 ++
                3 +++
                4 ++++
                5 +++++
                6 ++++++
                7 +++++
                8 ++++
                9 +++
                10 ++
                11 +
```





# Metadata

| *Summary*                     | Convert a text to a dictionary of words |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

