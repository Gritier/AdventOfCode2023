value = 0

input = []

numbers = {
    'eight': 8,
    'seven': 7,
    'three': 3,
    'nine': 9,
    'one': 1,
    'five': 5,
    'four': 4,
    'two': 2,
    'six': 6,
}


calibration_values = []


def replace_textual(string):
    if len(string) == 3:
        for number in numbers.keys():
            string = string.replace(number, str(numbers[number]))
    elif len(string) == 4:
        for i in range(2):
            if string[i:i+3] in numbers.keys():
                string = + \
                    string[i:i+3].replace(string[i:i+3],
                                          str(numbers[string[i:i+3]]))+string[i+3:]
        if len(string) > 3:
            if string in numbers.keys():
                string = string.replace(string, str(numbers[string]))
    else:
        for i in range(len(string)-4):
            for number in numbers.keys():
                string = string[:i]+string[i:i +
                                           5].replace(number, str(numbers[number]))+string[i+5:]
    return string


def replace_residual(string):
    for c in string:
        if not c.isdigit():
            string = string.replace(c, "")
    return string


with open("input.txt", "r") as puzzle:
    input = puzzle.read().splitlines()


def main():
    for i in input:
        line = replace_residual(replace_textual(i))
        value = int(str(line[0])+str(line[-1]))
        calibration_values.append(value)

    total = 0

    for v in calibration_values:
        total += v

    print(total)


main()
