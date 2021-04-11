# PyNumeral v1.0
PyNumeral python library for formatting and manipulating numbers
## Create a simple program in pynumeral
Creating a simple program with the PyNumeral library is explained below with code and comments:
```python
import pynumeral # importing pynumeral

'''
  we store the functions in the pynumeral document to the num variable.
'''
num = pynumeral # this in num variable 

num.format( # use format function

  num = 10.4, # declare a number for formatting
  form = "0.!0" # format type
  # value: 10
)
```
## Docs
### Importing PyNumeral
In python file
```python
import pynumeral
```
### `format()` function
you can format any number from the `format()` function to percentages, integers, rounded numbers, currencies, odd-evens, and more. Syntax:
```python
num.format(

  num = 10.5,
  form = "<0.0>"

)
```
