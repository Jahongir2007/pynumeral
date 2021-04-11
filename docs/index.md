# PyNumeral v1.0
PyNumeral python library for formatting and manipulating numbers
## Create a simple program in pynumeral (construction)
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
import pynumeral # importing pynumeral 
```
### `format()` function
you can format any number from the `format()` function to percentages, integers, rounded numbers, currencies, odd-evens, and more. Syntax:
```python
num.format(

  num = 10.5,
  form = "<0.0>"

)
```

<table>
  <tr>
    <td><b>Number</b></td>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
    <tr>
    <td>100</td>
    <td>"0.0"</td>
    <td>100.0</td>
  </tr>
      <tr>
    <td>-100</td>
    <td>"||"</td>
    <td>100</td>
  </tr>
      <tr>
    <td>100.3</td>
    <td>"0.!0"</td>
    <td>100</td>
  </tr>
      <tr>
    <td>2</td>
    <td>"0,0t"</td>
    <td>2 ,000</td>
  </tr>
      <tr>
    <td>3</td>
    <td>"0t"</td>
    <td>3 000</td>
  </tr>
      <tr>
    <td>15</td>
    <td>"0,0m"</td>
    <td>15 ,000000</td>
  </tr>
      <tr>
    <td>100</td>
    <td>"m"</td>
    <td>100 000 000</td>
  </tr>
      <tr>
    <td>100</td>
    <td>"+0"</td>
    <td>+100</td>
  </tr>
</table>