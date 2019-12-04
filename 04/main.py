def main():
    x = 147981
    y = 691423
    print(num_of_corr_passwords(x, y))


def num_of_corr_passwords(start, stop):
    num = 0
    for i in range(start, stop):
        if is_correct_password(i):
            num += 1

    return num


def is_correct_password(password):
    password_str = str(password)
    has_duplet = False

    if len(password_str) != 6:
        return False
    for i in range(1, len(password_str)):
        if int(password_str[i]) < int(password_str[i-1]):
            return False
        elif int(password_str[i]) == int(password_str[i-1]):
            has_duplet = True

    return True if has_duplet else False


main()
