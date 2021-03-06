![db2a7348b09e424b92aa94cb33c38fd9](https://user-images.githubusercontent.com/69193276/115833303-531fab00-a42d-11eb-8eee-700b7c144a4b.png)

# PyNumeral v1.1.7
PyNumeral python library for formatting and manipulating numbers
## Create a simple program in pynumeral
Creating even-odd program with the PyNumeral library is explained below with code and comments:
```python
import pynumeral # importing pynumeral

'''
  we store the functions in the pynumeral document to the num variable.
'''
num = pynumeral # this in num variable 

number_in = int(input("Enter number: ")) # Input number

num.format( # use format function

  num = number_in, # declare a number for formatting
  form = "0%2" # format type
  
)
```
## Docs
### Run this library
1. Install .zip file in github
2. Copy file: pynumeral-1.0.3/bin/pynumeral.py
3. Create new folder and paste pynumeral.py
4. Create new (for example test.py) .py file in this folder (the folder must contain a pynumeral file)
5. Write the code to your newly opened .py file and run it, following the PyNumeral syntax

### Importing PyNumeral
In python file
```python
import pynumeral # importing pynumeral
'''
  we store the functions in the pynumeral document to the num variable.
'''
num = pynumeral # this in num variable
```
### Create
```python
import pynumeral
num = pynumeral
num.numeral(12)
# 12
```
### `format()` function
you can format any number from the `format()` function to percentages, integers, rounded numbers, currencies, odd-evens, and more. Syntax:

```python
num.format(

  num = 10.5,
  form = "<0.0>"

)
```

#### Numbers

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
    <td>"|0|"</td>
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
    <td>"0m"</td>
    <td>100 000 000</td>
  </tr>
      <tr>
    <td>100</td>
    <td>"+0"</td>
    <td>+100</td>
  </tr>
      <tr>
    <td>100.8</td>
    <td>"&lt;0.0&gt;"</td>
    <td>101</td>
  </tr>
      <tr>
    <td>100.1</td>
    <td>"!0.0"</td>
    <td>0.09999999999999432</td>
  </tr>
        <tr>
    <td>12.14</td>
    <td>"0.[0]"</td>
    <td>12.1</td>
  </tr>
          <tr>
    <td>12.147</td>
    <td>"0.0[0]"</td>
    <td>12.14</td>
  </tr>
          <tr>
    <td>12.1479</td>
    <td>"0.00[0]"</td>
    <td>12.147</td>
  </tr>
  <tr>
    <td>12</td>
    <td>"0C"</td>
    <td>12 C</td>
  </tr>
    <tr>
    <td>24</td>
    <td>"0C[0F]"</td>
    <td>75.2 F</td>
  </tr>
      <tr>
    <td>51, 52</td>
    <td>"1", "2", "3", "on"</td>
    <td>51 st, 52 nd, 53 rd, 100 th</td>
  </tr>
      <tr>
    <td>1200</td>
    <td>"0a"</td>
    <td>1.2k</td>
  </tr>
    <tr>
    <td>100</td>
    <td>"(0.000)"</td>
    <td>( 100, 000)</td>
  </tr>
      <tr>
    <td>100</td>
    <td>"0.0"</td>
    <td>100.0</td>
  </tr>
      <tr>
    <td>100</td>
    <td>"0%2"</td>
    <td>even</td>
  </tr>
</table>

#### Units of length

<table>
  <tr>
    <td><b>Number</b></td>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
  <tr>
    <td>8</td>
    <td>"0_m"</td>
    <td>8 mm</td>
  </tr>
  <tr>
    <td>25</td>
    <td>"0_m"</td>
    <td>2.5 cm</td>
  </tr>
    <tr>
    <td>250</td>
    <td>"0_m"</td>
    <td>25 dm</td>
  </tr>
      <tr>
    <td>2500</td>
    <td>"0_m"</td>
    <td>25 m</td>
  </tr>
        <tr>
    <td>25000</td>
    <td>"0_m"</td>
    <td>25 km</td>
  </tr>
</table>

#### Bytes

<table>
  <tr>
    <td><b>Number</b></td>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
  <tr>
    <td>1048577</td>
    <td>"0b"</td>
    <td>0.0009765634313225746 GB</td>
  </tr>
    <tr>
    <td>1024</td>
    <td>"0b"</td>
    <td>1.0 KB</td>
  </tr>
      <tr>
    <td>234000</td>
    <td>"0b"</td>
    <td>0.2231597900390625 MB</td>
  </tr>
    <tr>
    <td>104857756</td>
    <td>"0b"</td>
    <td>9.536757352179848e-05 TB</td>
  </tr>
</table>

#### Currency

<table>
  <tr>
    <td><b>Number</b></td>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
  <tr>
    <td>100</td>
    <td>"$0.0"</td>
    <td>$ 100.0</td>
  </tr>
    <tr>
    <td>100</td>
    <td>"$0.0"</td>
    <td>$ 100.0</td>
  </tr>
      <tr>
    <td>100</td>
    <td>"$0k"</td>
    <td>$ 100 k</td>
  </tr>
        <tr>
    <td>100</td>
    <td>"$0m"</td>
    <td>$ 100 m</td>
  </tr>
</table>

#### Percentages

<table>
  <tr>
    <td><b>Number</b></td>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
  <tr>
    <td>1</td>
    <td>"0%"</td>
    <td>100 %</td>
  </tr>
  <tr>
    <td>0.25</td>
    <td>"0%"</td>
    <td>25 %</td>
  </tr>
    <tr>
    <td>-0.25</td>
    <td>"0%"</td>
    <td>-25 %</td>
  </tr>
</table>

#### Time

<table>
  <tr>
    <td><b>Number</b></td>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
  <tr>
    <td>49</td>
    <td>"00:00:00"</td>
    <td>00:49</td>
  </tr>
  <tr>
      <td>120</td>
    <td>"00:00:00"</td>
    <td>2:00</td>
  </tr>
    <tr>
      <td>3601</td>
    <td>"00:00:00"</td>
    <td>1:1:00</td>
  </tr>
</table>

### Unformatting
Got a formatted string? Use the unformat function to make it useful again.
```python
num.unform(
  
  num = 20,
  type = "0%"
  # value: 0.2
  
)
```

<table>
  <tr>
    <td><b>Value</b></td>
    <td><b>Type</b></td>
    <td><b>Number</b></td>
  </tr>
  <tr>
    <td>20.2</td>
    <td>"0.0"</td>
    <td>20</td>
  </tr>
    <tr>
    <td>20</td>
    <td>"0.!0"</td>
    <td>20.0</td>
  </tr>
    <tr>
    <td>35</td>
    <td>"|0|"</td>
    <td>35</td>
  </tr>
    <tr>
    <td>20</td>
    <td>"0k"</td>
    <td>20000</td>
  </tr>
    <tr>
    <td>15</td>
    <td>"0m"</td>
    <td>15000000</td>
  </tr>
    <tr>
    <td>20</td>
    <td>"0%"</td>
    <td>0.2</td>
  </tr>
</table>

### Number types
numbers accepted in mathematics. Syntax:
```python
num.number("pi")
# 3.141592653589793
```
<table>
  <tr>
    <td><b>Type</b></td>
    <td><b>Value</b></td>
  </tr>
  <tr>
    <td>"pi"</td>
    <td>3.141592653589793</td>
  </tr>
  <tr>
    <td>"inf"</td>
    <td>inf</td>
  </tr>
    <tr>
    <td>"e"</td>
    <td>2.718281828459045</td>
  </tr>
      <tr>
    <td>"nan"</td>
    <td>nan</td>
  </tr>
        <tr>
    <td>"tau"</td>
    <td>6.283185307179586</td>
  </tr>
</table>

### Manipulate
In PyNumeral, manipulation is generated mainly in variables.
```python
a = 12 # variable for manipulate
num.add(
  num = a, # get value
  set = 1
  # value: 13
)
```
### Actions on numbers
In the PyNumeral library, numbers can be added, subtracted, multiplied, and divided.
```python
# add numbers
num.add(
  num = 14, 
  set = 12
  # value: 26
)
```

```python
# subtract numbers
num.sub(
  num = 14, 
  set = 12
  # value: 2
)
```

```python
# multiply numbers
num.mul(
  num = 14, 
  set = 12
  # value: 168
)
```

```python
# division numbers
num.div(
  num = 14, 
  set = 12
  # value: 1.166666666666667
)
```
### Calculate the given example
Imagine you are given an example PyNumeral will help you work on it quickly.
```python
num.calc((24-12)/2)
# value: 6
```
### Difference
Find the difference between any two numbers in pynumeral.
```python
num.dif(
  num = 900,
  set = 100
  # value: difference 800
)
```
### Clone
A PyNumeral clone is a manipulation of this variable and consists of a clone name and contains a value.
```python
a = 12
num.clone(
  name = "myclone",
  set = a
  '''
  Output:
  Name clone: myclone
  Value clone: 12
  '''
)
```
### Number list
Use this method to display a list of numbers from any number to any number.
```python
num.numlist(
  start = 1,
  end = 6
  '''
  Output:
  1
  2
  3
  4
  5
  '''
)
```
### Value
The `value()` function stores the value
```python
num.val(100)
```
### Encryption of zeros
In PyNumeral, the encryption of zeros is done using the `zeroform()` function.
```python
num.zeroform(
  code = "Z/N",
  num = "0.0"
  '''
  Output:
  number: Z/N
  '''
)
```
### How to create language
Create your number formats:
```python
num.makelang(
    lang="uzb",
    abb_k="ming",
    abb_m="million",
    abb_b="milliard",
    abb_t="trillion",
    curr="so'm",
    num=1000
    '''
    Output:
    1.0 ming
    so'm 1000
    '''
)
```
### Opposite numbers
To find the opposite of the desired number
```python
num.opposite(12)
# -12
num.opposite(-45)
# 45
```
### The truth of numbers
To determine this, you need to use the `real()` function.
```python
num.real(
  self = "<",
  numf = 12,
  nums = 11
  # value: False
)
```
### `cordinate()` function
Determine between which numbers the desired number is located
```python
num.cordinate(12)
# value: 11 12 13
```
