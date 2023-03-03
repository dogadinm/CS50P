def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    withoutd = d.replace('$', '')
    return float(withoutd)


def percent_to_float(p):
    withoutp = p.replace('%', '')
    pconv = float(withoutp) / 100
    return pconv
main()