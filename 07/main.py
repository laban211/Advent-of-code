def main():
    data = get_data()
    test_1(data)


def get_data():
    with open("input.txt", "r") as f:
        data = f.read()
        return [int(x) for x in data.split(",")]


def test_1(data):
    print("Answer: " + str(run_amplifier([0, 1, 2, 3, 4], data)))


def run_amplifier(settings, data):
    in_val = 0
    for s in settings:
        output = intcode_compute(data, in_val, s)
        in_val = output
    return output


def intcode_compute(list, input_val, phase_setting):
    new_list = list.copy()

    i = 0
    stepper = 0
    phase_setting_used = False

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
            # New
            new_list[p1] = input_val if phase_setting_used else phase_setting
            phase_setting_used = True
            stepper = 2
        elif op == 4:
            # print(new_list[p1])
            new_list[0] = new_list[p1]
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


main()
