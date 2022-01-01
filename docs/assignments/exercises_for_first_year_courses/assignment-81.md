---
title: "Automating testing of functions that use files"
author: TILEd by Tanja E.J. Vos
...

# Automating testing of functions that use files

To test a function like `calculate_VAT` from the [Process prices from a file and calculate the VAT](exercises_for_first_year_courses/assignment-80.md) exercise, which generates a file,
you have to open the file it has generated to check that it has the
content you expected. For example, if you used the file `data1.txt`
as input, you would expect a file with name `data1_VAT.txt` that has
the content as shown in the example above.

Doing that manually is tedious. Imagine doing it for 10 data files,
from `data1.txt` to `data10.txt`. We would have to manually generate the
10 files from `data1_VAT.txt` to `data10_VAT.txt`, with
`calculate_VAT`, and then open them one by one to check their
content to see if it is what we expect.

We can automate it with pytest. However, the output of the function
is not just a value as we have seen so far. The output of the
`calculate_VAT` function is a file. So the expected output can also
be a file, and the test simply compares that what comes out is equal
to what we expect!

For that, we must create 10 files only once where we define the
expected outputs of our tests: from to. Then we create a pytest
like the one below:

```python
@pytest.mark.parametrize("testcase, f_input, f_expected_output",[ (1, "data1.txt", "expected_output_data1_VAT.txt"), (2, "data2.txt", "expected_output_data2_VAT.txt"), (3, "data3.txt", "expected_output_data3_VAT.txt"), (4, "data4.txt", "expected_output_data4_VAT.txt"), (5, "data5.txt", "expected_output_data5_VAT.txt"), (6, "data6.txt", "expected_output_data6_VAT.txt"), (7, "data7.txt", "expected_output_data7_VAT.txt"), (8, "data8.txt", "expected_output_data8_VAT.txt"), (9, "data9.txt", "expected_output_data9_VAT.txt"), (10, "data10.txt", "expected_output_data10_VAT.txt"), ])

def test_calculate_VAT(testcase, f_input, f_expected_output):
    f_output = calculate_VAT(f_input)
    assert (open(f_output).read() == open(f_expected_output).read()), "case 0".format(testcase)
```

NOTE: To compare the files we have used `read` because the size of
the files that we are handling here is very small.


# Metadata

| *Summary*                     |  Automating testing of functions that use files |
| *TILE aspects*                | Test domain, test cases and test run TILE-ing is applied. |
| *Topics*                      |  |
| *Technology used*             | Python |
| *Audience*                    | CS1 |
| *Programming learning goals*  |  |
| *Testing learning goals*      |  |
| *Prerequisites*               | Basic programming constructs. |
| *Variants*                    | Many options are possible, including porting to other programming languages. | 
| *Added by*                    | Tanja E.J. Vos |   

