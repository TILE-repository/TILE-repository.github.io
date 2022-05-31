---
title: "Calculate the variance of the numbers from a file"
summary: "Calculate the variance of the numbers from a file."
prerequisites: "['io > standard > input', 'data > types (built-in) > primitive > numeric', 'data > types (built-in) > composite > sequences > strings', 'imperative programming > variables]"
concepts practised: "['data > types (built-in) > composite > sequences > lists', 'io > files > text > plain', 'expressions > operators > arithmetic operators']"
target audience: "CS1"
author: Tanja E.J. Vos
license: "CC-BY"
...

# Calculate the variance of the numbers from a file

Write a function `calculate_variance` in Python that receives the name of a file and reads a number of real numbers from this file, storing them in a list. Then it shows the variance of these data on the screen. The variance is calculated as the sum of the squared differences between each element in the list, v[i], and the mean, all divided by the number of elements (N): $$w = \frac{\sum_{i=1}{n} (x[i]-mean)^{2}}{N}$$

For example, imagine we have:

```small
6.64 
136.33 
32.02 
56.16 
97.67 
160.56 
```

```small
>>> calculate_variance("numbers.txt")
    3035.443822222222
```

To test your function we are going to use Exercise
[[generate_files]](#generate_files){reference-type="ref"
reference="generate_files"} to generate a number of files (eg 5
files `numbers1.txt`, `numbers2.txt`, `numbers3.txt`, `numbers4.txt`
and `numbers5.txt`).

Then we go to
<https://www.calculatorsoup.com/calculators/statistics/variance-calculator.php>
to calculate the variance of the data in these 5 files. In this way
we have the expected results of our function.

Then finish the following pytest code to run your tests
automatically:

```python
import pytest

@pytest.mark.parametrize("testcase, f_input, expected_output",[
(1, "numbers1.txt", 3713.1622346939), (2, "numbers2.txt", ...
(3, (4, (5, ])

def test_calculate_variance(testcase, f_input, expected_output):
    assert abs(calculate_variance(f_input) - expected_output) < 10**-7 , "case 0".format(testcase)
```

Remember to keep in mind that comparing floats for equality has
rounding and precision problems. That is why we must compare that
the difference between what comes out of our function and what we
expect is less than, for example, $$10^{-7}$$.
