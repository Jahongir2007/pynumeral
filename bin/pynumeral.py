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
            build = "k"
            print(num,build)
        elif num >= 1000000:
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
    elif form == "kb":
        if num == 1024:
            val = num / 1024
            build = "KB"
        elif num > 1024:
            val = num / 1024
            build = "KB"
            print(val,build)
    elif form == "mb":
        if num == 1048576:
            val = num / 1048576
            build = "MB"
            print(val,build)
        elif num > 1024:
            val = num / 1024
            build = "MB"
            print(val,build)
    elif form == "gb":
        if num == 1024:
            val = num / 1024
            build = "GB"
            print(val,build)
        elif num > 1024:
            val = num / 1024
            build = "GB"
            print(val,build)
    elif form == "tb":
        if num == 1024:
            val = num / 1024
            build = "TB"
            print(val,build)
        elif num > 1024:
            val = num / 1024
            build = "TB"
            print(val,build)
    elif form == "0k":
        if num == 1000:
            val = num / 1000
            build = "k"
            print(int(val),build)
        elif num > 1000:
            val =  num / 1000
            build = "k"
            print(val,build)
    elif form == "0m":
        if num == 1000000:
            val = num / 1000000
            build = "m"
            print(int(val),build)
        elif num > 1000000:
            val =  num / 1000000
            build = "m"
            print(val,build)
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
