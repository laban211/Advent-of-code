def main():
    x = 147981
    y = 691423
    print(num_of_corr_passwords(x, y))


def num_of_corr_passwords(start, stop):
    num = 0
    for i in range(start, stop):
        if is_correct_password(i) and new_rules(i):
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


def new_rules(password):
    if not is_correct_password(password):
        return False

    password_str = str(password)
    has_duplet = False
    has_triplet = False
    my_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in password_str:
        my_dict[int(num)] = my_dict[int(num)] + 1

    for i in range(1, 10):
        if my_dict.get(i) == 3:
            has_triplet = True
        elif my_dict.get(i) == 2:
            has_duplet = True

    return True if has_duplet else False


main()
