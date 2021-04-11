import math

def format(num, form):
    if form == "0.0":
        print(float(num))
    elif form == "||":
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
    elif form == "m":
        build = "000 000"
        print(num,build)
    elif form == "+0":
        build = "+"
        print(build,num)
    elif form == "<0.0>":
        print(math.ceil(num))
    elif form == "!0.00":
        basic = float(num)
        intnum = int(num)
        val = basic - intnum
        print(val)
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
    elif form == "0a":
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
        elif num >= 1025:
            val = num / 1048576
            print(val,"MB")
        elif num >= 1048577:
            val = num / 1073741824
            print(val,"GB")
        elif num >= 1073741825:
            val = num / 1099511627776
            print(val,"TB")
    elif form == "hsm":
        if num < 60:
            print(num, "seconds")
        elif num > 60:
            val = num / 60
            print(val, "minutes")
        if num < 3600:
            val = num / 3600
            print(val, "hours")
    elif form == "00:00:00":
        seconds = "00"
        minutes = "00"
        hours = "00"
        if num < 59:
            seconds = num
            print(hours,":",math.ceil(seconds),":",seconds)
        elif num > 59:
            minutes = num
            val = minutes / 60
            print(hours,":",val,":",seconds)
    elif form == "0%":
        if num == 1:
            num = 100
            print(num,"%")
        elif num < 1:
            val = num * 100
            print(int(val),"%")
    elif form == "0a":
        if num <= 1000000:
            val = num / 1000
            print(val,abb_k)
        elif num <= 1000000000:
            val = num / 1000000
            print(num,abb_m)
        elif num <= 1000000000000:
            val = num / 1000000000 
            print(val,abb_b)
        elif num <= 1000000000000000:
            val = num / 1000000000000
            print(val,abb_t)
    elif form == "0%2":
        if num % 2 == 0:
            print("even")
        else:
            print("odd")
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
def val(value):
    print(value)
def clone(name, set):
    print("Name clone: ", name)
    print("Value clone: ", set)
def value(get):
    print(get)
def zeroform(code, num):
        print("number:",code)
def makelang(lang,abb_k,abb_m,abb_b,abb_t,curr,num):
    if num <= 1000000:
        val = num / 1000
        print(val,abb_k)
    elif num <= 1000000000:
        val = num / 1000000
        print(num,abb_m)
    elif num <= 1000000000000:
        val = num / 1000000000 
        print(val,abb_b)
    elif num <= 1000000000000000:
        val = num / 1000000000000
        print(val,abb_t)
    print(curr,num)
def unform(num,type):
    if type == "0.0":
        print(int(num))
    elif type == "||":
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
