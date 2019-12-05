def main():
    op_code = get_data()
    #x(op_code, 1)
    x(op_code, 5)


def get_data():
    with open("input.txt", "r") as f:
        data = f.read()
        return [int(x) for x in data.split(",")]


def x(list, input_val):
    new_list = list.copy()

    i = 0
    stepper = 0

    while new_list[i] != 99:
        op = new_list[i] % 100
        m1 = (new_list[i] // 100) % 10
        m2 = (new_list[i] // 1000) % 10
        m3 = (new_list[i] // 10000) % 10

        p1 = i + 1 if m1 == 1 else new_list[i + 1]
        p2 = i + 2 if m2 == 1 else new_list[i + 2]
        p3 = i + 3 if m3 == 1 else new_list[i + 3]

        if op == 1:
            new_list[p3] = new_list[p1] + new_list[p2]
            stepper = 4
        elif op == 2:
            new_list[p3] = new_list[p1] * new_list[p2]
            stepper = 4
        elif op == 3:
            # This doesen't work as it should
            new_list[p1] = input_val
            stepper = 2
        elif op == 4:
            print(new_list[p1])
            stepper = 2
        elif op == 5:
            # Jump if true
            if new_list[p1] != 0:
                i = new_list[p2]
                stepper = 0
            else:
                stepper = 3
        elif op == 6:
            if new_list[p1] == 0:
                i = new_list[p2]
                stepper = 0
            else:
                stepper = 3
        elif op == 7:
            # less than
            if new_list[p1] < new_list[p2]:
                new_list[p3] = 1
            else:
                new_list[p3] = 0
            stepper = 4
        elif op == 8:
            # Equals?
            if new_list[p1] == new_list[p2]:
                new_list[p3] = 1
            else:
                new_list[p3] = 0
            stepper = 4
        else:
            print("I fcked up:" + str(op))

        i += stepper

    return new_list[0]


def y(list, target):
    for noun in range(100):
        for verb in range(100):
            if x(list, noun, verb) == target:
                return 100 * noun + verb


main()
