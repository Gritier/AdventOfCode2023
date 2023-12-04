first = 0
last = 0
value = 0

calibration_values= []

with open("input.txt", "r") as puzzle:
    for line in puzzle.readlines():
        flag_1 = 0
        flag_2 = 0
        for c in line:
            if c.isdigit():
                if flag_1==0:
                    flag_1 = 1
                    first = c
                else:
                    flag_2 = 1
                    last = c
        if (flag_1 == 1) and (flag_2 != 1):
            last = first
        value = int(str(first)+str(last))
        calibration_values.append(value)

        print(f'String: {line}First: {first}\nLast: {last}\nValue: {value}\n')

print(calibration_values)

total = 0

for v in calibration_values:
    total += v

print(total)
