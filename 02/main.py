import csv


def main():
    op_code = get_data()

    # Part one
    print(x(op_code, 12, 2))

    # Part two
    print(y(op_code, 19690720))


def get_data():
    with open("input.txt", "r") as f:
        data = f.read()
        return [int(x) for x in data.split(",")]


def x(list, replace1, replace2):
    new_list = list.copy()
    new_list[1] = replace1
    new_list[2] = replace2

    index = 0
    while True:
        if new_list[index] == 99:
            break
        elif new_list[index + 4] == None:
            break
        elif new_list[index] == 1:
            new_list[new_list[index + 3]] = new_list[new_list[index+1]] + \
                new_list[new_list[index+2]]
        elif new_list[index] == 2:
            new_list[new_list[index + 3]] = new_list[new_list[index+1]] * \
                new_list[new_list[index+2]]
        index += 4

    return new_list[0]


def y(list, target):
    for noun in range(100):
        for verb in range(100):
            if x(list, noun, verb) == target:
                return 100 * noun + verb


main()
