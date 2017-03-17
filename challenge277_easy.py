def simp_frac(a, b):
    if a == 0:
        print("\n0\n")
        return
    elif b == 0:
        print("\nDenominator cannot equal 0!\n")
        return
    x, y = abs(a), abs(b)
    while x != y:
        if x > y: x -= y
        else: y -= x
    a //= x
    b //= x
    if a < 0 and b < 0: 
        a, b = -a, -b
    print("\n{0} / {1}\n".format(a, b))
    return

def main():
    print("- - -- --- ----- Fraction simplifier ----- --- -- - -", end="\n\n\n")
    print("..to close program use ctrl+c...\n")
    while True:
        simp_frac(int(input("Numerator: ")), int(input("Denominator: ")))
    return

main()
