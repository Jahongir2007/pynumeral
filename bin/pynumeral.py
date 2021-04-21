'''
    Author: Jahongir Sobirov
    PyNumeral library
    Version: 1.1.0
    License: MIT
'''
import math

def format(num, form):
    if form == "0.0":
        print(float(num))
    elif form == "|0|":
        print(abs(num))
    elif form == "0.!0":
        print(int(num))
    elif form == "0,0t":
        build = ",000"
        print(num,build)
    elif form == "0t":
        build = "000"
        print(num,build)
    elif form == "0,0m":
        build = ",000000"
        print(num,build)
    elif form == "0m":
        build = "000 000"
        print(num,build)
    elif form == "+0":
        build = "+"
        print(build,num)
    elif form == "<0.0>":
        print(math.ceil(num))
    elif form == "!0.00":
        print(math.modf(num))
    elif form == "1":
        on = "st"
        print(num,on)
    elif form == "2":
        on = "nd"
        print(num,on)
    elif form == "3":
        on = "rd"
        print(num,on)
    elif form == "on":
        on = "th"
        print(num,on)
    elif form == "k":
        on = "k"
        print(num,on)
    elif form == "m":
        on = "m"
        print(num,on)
    elif form == "(0.000)":
        fa = "("
        sa = ")"
        ta = ","
        build = ".000"
        print(fa,num,build,sa)
    elif form == "$0.0":
        build = "$"
        print(build,float(num))
    elif form == "$0k":
        build = "k"
        print(int(num),build)
    elif form == "$0m":
        build = "m"
        print(int(num),build)
        if num >= 1000:
            val = num / 1000
            build = "k"
            print(val,build)
        elif num >= 1000000:
            val = num / 1000000
            build = "m"
            print(num,build)
        else:
            print("Error!")
    elif form == "2b":
        print(bin(num)[2:].zfill(8))
    elif form == "3b":
        print(bin(num)[3:].zfill(8))
    elif form == "8b":
        print(oct(num))
    elif form == "b":
        print(bin(num))
    elif form == "h":
        print(hex(num))
    elif form == "res":
        print(reversed(num))
    elif form == "asc":
        print(ascii(num))
    elif form == "0b":
        if num <= 1024:
            val = num / 1024
            print(val,"KB")
        elif num <= 1048576:
            val = num / 1048576
            print(val,"MB")
        elif num <= 1048577:
            val = num / 1073741824
            print(val,"GB")
        elif num >= 1073741825:
            val = num / 1099511627776
            print(val,"TB")
    elif form == "00:00:00":
        if num <= 59:
            print("00",":",num)
        elif num >= 59:
            if num % 2 == 0:
                print(int(num/60),":","00")
            elif num >=3600:
                print(int(num/3600),":",num%60,':','00')
            else:
                val = num / 60
                sec = num % 60
                print(math.ceil(val),":",sec)
    elif form == "0%":
        if num == 1:
            num = 100
            print(num,"%")
        elif num < 1:
            val = num * 100
            print(int(val),"%")
    elif form == "0a":
        if num <= 999999:
            print(num / 1000,"k")
        elif num <= 999999999:
            print(num / 1000000,"m")
        elif num <= 999999999:
            print(num / 1000000,"m")
        elif num <= 999999999999:
            print(num / 1000000000,"b")
        elif num <= 999999999999999:
            print(num / 1000000000000,"t")
    elif form == "0%2":
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
    elif form == "0.[0]":
        def truncate(n, decimals=0):
            multiplier = 10 ** decimals
            return int(n * multiplier) / multiplier
        print(truncate(num, 1))
    elif form == "0.0[0]":
        def truncate(n, decimals=0):
            multiplier = 10 ** decimals
            return int(n * multiplier) / multiplier
        print(truncate(num, 2))
    elif form == "0.00[0]":
        def truncate(n, decimals=0):
            multiplier = 10 ** decimals
            return int(n * multiplier) / multiplier
        print(truncate(num, 3))
    elif form == "0C":
        print(num, "C")
    elif form == "0C[0F]":
        print((num*1.8)+32, "F")
    else:
        print("Error!")
def add(num, set):
    print(num + set)
def sub(num, set):
    print(num - set)
def div(num, set):
    print(num / set)
def mul(num, set):
    print(num * set)
def dif(num, set):
    print(num - set)
def clone(name, set):
    print("Name clone: ", name)
    print("Value clone: ", set)
def value(get):
    print(get)
def zeroform(code, num):
        print("number:",code)
def makelang(lang,abb_k,abb_m,abb_b,abb_t,curr,num):
        if num <= 999999:
            print(num / 1000,"k")
        elif num <= 999999999:
            print(num / 1000000,"m")
        elif num <= 999999999:
            print(num / 1000000,"m")
        elif num <= 999999999999:
            print(num / 1000000000,"b")
        elif num <= 999999999999999:
            print(num / 1000000000000,"t")
        print(num,curr)
def unform(num,type):
    if type == "0.0":
        print(int(num))
    elif type == "|0|":
        print(num)
    elif type == "0.!0":
        print(float(num))
    elif type == "0k":
        val = num * 1000
        print(val)
    elif type == "0m":
        val = num * 1000000
        print(val)
    elif type == "0%":
        val = num / 100
        print(val)
def cordinate(num):
    prev = num - 1
    nt = num + 1
    print(prev,num,nt)
def real(self, numf, nums):
        if self == "<":
            print(numf < nums) 
        elif self == ">":
            print(numf > nums)
        elif self == "=":
            print(numf ==  nums)
def calc(value):
    print(value)
def number(num):
    if num == "pi":
        print(math.pi)
    elif num == "inf":
        print(math.inf)
    elif num == "e":
        print(math.e)
    elif num == "nan":
        print(math.nan)
    elif num == "tau":
        print(math.tau)
def numlist(start,end):
    li = range(start, end)
    for n in li:
        print(n)
def numeral(value):
        print(value)
def value(val):
        print(val)
