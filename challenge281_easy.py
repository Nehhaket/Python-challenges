#Base

letters = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "A": 10, "b": 11, "B": 11, "c": 12, "C": 12, "d": 13, "D": 13, "e": 14, "E": 14, "f": 15, "F": 15, "g": 16, "G": 16, "h": 17, "H": 17, "i": 18, "I": 18, "j": 19, "J": 19, "k": 20, "K": 20, "l": 21, "L": 21, "m": 22, "M": 22, "n": 23, "N": 23, "o": 24, "O": 24, "p": 25, "P": 25, "q": 26, "Q": 26, "r": 27, "R": 27, "s": 28, "S": 28, "t": 29, "T": 29, "u": 30, "U": 30, "v": 31, "V": 31}

print("Returning minimal base possible to wich given number can belong (up to base 32) and it's equivalent in base 10. (To exit type \"exit()\")")

def tens(string, a):
    t = 0
    for x in range(len(string)):
        t += letters[string[-(x+1)]]*(a**x)
    return t

def minimal():
    string = input("> ")
    if string == "exit()":
        exit()
    else:
        a = 0
        for x in string:
            if x in letters:
                if letters[x] > a:
                    a = letters[x]
                else:
                    continue
            else:
                print("Unsupported character found!")
                return minimal()
        out = tens(string, a+1)
        print("{0} : base {1} => {2} (base 10)".format(string, a+1, out))
    return minimal()
    
minimal()
