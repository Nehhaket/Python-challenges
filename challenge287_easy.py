def desc_digits(string):
    return "Descended: " + "".join(sorted(string, reverse=True))


def largest_digit(string):
    return "Max: " + str(max(string))


def kaprekar(string):
    i = 0
    for j in range(len(string)-1):
        if string[j] != string[j+1]:
            break
        elif j == (len(string)-2):
            return "At least two different digits required"
    while string != "6174":
        i += 1
        string = str(int("".join(sorted(string, reverse=True))) - int("".join(sorted(string))))
        for x in range(4 - len(string)):
                string = "0" + string
    return i


def main(string):
    if string == "exit()":
        exit()
    else:
        if len(string) <= 4:
            for i in range(4 - len(string)):
                string = "0" + string
            print(largest_digit(string))
            print(desc_digits(string))
            print(kaprekar(string))
            return main(input("Moar? "))
        else:
            print("Up to 4 digits!")
            return main(input("Again! "))


main(input("Gimme dem digits! "))
