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

with open("input.txt", "r") as puzzle:
    input = puzzle.read().splitlines()


def check(string):
    if string in numbers.keys():
        return string.replace(string, str(numbers[string]))
    else:
        return string


def replace_residual(string):
    for c in string:
        if not c.isdigit():
            string = string.replace(c, "")
    return string


def loop_substring(line):
    for i in range(len(line)-3):
        for n in range(3, 6):
            if i+n <= len(line):
                temp_line = line[:i]+check(line[i:i+n])+line[i+n:]
                line = line.replace(line, temp_line)
            else:
                temp_line = line[0:-3]+check(line[-3:])
                line = line.replace(line, temp_line)

    return line


def analyze_string(string):
    l = 0
    r = 0
    temp = string.replace(string, string+("_"))
    for i, c in enumerate(temp):
        if c.isdigit() and l == 0:
            l = int(c)
        elif temp[i:i+3] in numbers.keys() and len(temp) > (i+3) and l == 0:
            l = numbers[temp[i:i+3]]
        elif temp[i:i+4] in numbers.keys() and len(temp) > (i+4) and l == 0:
            l = numbers[temp[i:i+4]]
        elif temp[i:i+5] in numbers.keys() and len(temp) > (i+5) and l == 0:
            l = numbers[temp[i:i+5]]
        if i == 0:
            j = -1
        else:
            j = (i*-1)-1
        if temp[j].isdigit() and r == 0:
            r = int(temp[j])
        elif temp[j-3:j] in numbers.keys() and len(temp) > (i+3) and r == 0:
            r = numbers[temp[j-3:j]]
        elif temp[j-4:j] in numbers.keys() and len(temp) > (i+4) and r == 0:
            r = numbers[temp[j-4:j]]
        elif temp[j-5:j] in numbers.keys() and len(temp) > (i+5) and r == 0:
            r = numbers[temp[j-5:j]]
        print(temp[j-5:j])
    if r == 0:
        r = l
    value = int(str(l)+str(r))
    return value


def main():
    for line in input:
        # new_line = replace_residual(loop_substring(line))
        # value = int(str(new_line[0])+str(new_line[-1]))
        value = analyze_string(line)
        calibration_values.append(value)
        print(f'{line} : {value}')

    print(sum(calibration_values))


main()
