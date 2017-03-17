inpt1 = [(10, 16), (10, 32), (10, 9024720), ("F", 10), ("F", 1), ("F", 111111), ("F", 100000), ("F", 10110110100111001)]
inpt2 = [(10, 8), (10, 16), (10, 32), (10, 9024720)]
inpt_test = [("F", 111111011111110101101011101101110)]

def defib(string):
    i = 0
    string = list(string)
    for x in range(len(string)-2):
        if string[-(x+1)] == "0" and string[-(x+2)] == "0" and string[-(x+3)] == "1":
            i += 1
            string[-(x+1)] = "1"
            string[-(x+2)] = "1"
            if (x+3) == len(string):
                del string[0:1]
            else:
                string[-(x+3)] = "0"
        else:
            continue
    new_string = ""
    for y in string:
        new_string += y
    if i == 0:
        return new_string
    else:
        return defib(new_string)        
    
def encode(inpt):
    if inpt == "2":
        inpt = inpt2
    elif inpt == "test":
        inpt = inpt_test
    else:
        inpt = inpt1
    for i in inpt:
        if i[0] == "F":
            a, b, s = 1, 1, 0
            for x in range(len(str(i[1]))):
                s += int(str(i[1])[-(x+1)])*a
                a, b = b, a+b
            print(s)
        else:
            a, b, c = 1, 1, i[1]
            s = ""
            while b <= c:
                a, b = b, a+b
            while a >= 1:
                if c >= a:
                    c -= a
                    s += "1"
                else:
                    s += "0"
                a, b = b-a, a
            print(defib(s))
            
if __name__ == "__main__":
    import sys
    try:
        if len(sys.argv) > 1:
            encode(int(sys.argv[1]))
        else:
            encode(1)
    except ValueError:
        encode(sys.argv[1])



