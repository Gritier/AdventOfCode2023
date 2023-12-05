import re
import time

start_time = time.time()

def read_file(file="input.txt"):
    with open(file,"r") as f:
        return f.read().splitlines()

example = ['seeds: 79 14 55 13','','seed-to-soil map:','50 98 2','52 50 48','','soil-to-fertilizer map:','0 15 37','37 52 2','39 0 15','','fertilizer-to-water map:','49 53 8','0 11 42','42 0 7','57 7 4','','water-to-light map:','88 18 7','18 25 70','','light-to-temperature map:','45 77 23','81 45 19','68 64 13','','temperature-to-humidity map:','0 69 1','1 0 69','','humidity-to-location map:','60 56 37','56 93 4']

def extract_data(puzzle):
    keys = []
    for line in puzzle:
        if ":" in line:
            keys.append(line.split(":")[0])

    temp_data = {}

    for key in keys:
        temp_data[key] = []
        flag = 0
        for line in puzzle:
            if flag == 1 or key==keys[0]:
                temp = []
                for match in re.finditer("\d+", line):
                    temp.append(int(match.group()))
                temp_data[key].append(temp)
            if line == "" and flag==1:
               break
            elif key in line:
                flag = 1
    return temp_data

def get_data(puzzle):
    keys = []
    temp_data = {}
    for line in puzzle:
        if ":" in line:
            keys.append(line.split(":")[0])
    i = 0
    key = keys[i]
    flag = 0
    for line in puzzle:
        temp = []
        if flag == 1 and line != '':
            for match in re.finditer(r"\d+",line):
                temp.append(int(match.group()))
            temp_data[key].append(temp)
        if key == keys[0] and key in line:
            temp_data[key] = []
            for match in re.finditer(r"\d+",line):
                temp_data[key].append(int(match.group()))
            continue
        elif key in line:
            flag = 1
        elif line == "" and i < len(keys)-1:
            i += 1
            key = keys[i]
            flag = 0
            temp_data[key] = []
            continue
    return temp_data

def get_table(data):
    table = {}
    for idx,key in enumerate(data.keys()):
        if idx != 0:
            table[key]= {}
            subkeys = [key.split("-")[0],key.split("-")[2].split(" ")[0]]
            table[key][subkeys[0]] = []
            table[key][subkeys[1]] = []
            for el in data[key]:
                if len(el)>0:
                    table[key][subkeys[0]] = table[key][subkeys[0]] + [val for val in range(el[1],el[1]+el[2])]
                    table[key][subkeys[1]] = table[key][subkeys[1]] + [val for val in range(el[0],el[0]+el[2])]
        else:
            table[key] = data[key]
    return table

def get_min_location(values, table, turn=-1):
    turn += 1
    key = [key for key in table.keys()][turn]
    subkeys = [key for key in table[key].keys()]
    good_idx = []
    good_values = []
    print(f'{key}: {time.time()-start_time}')
    print(values)
    for value in values:
        for jdx,group in enumerate(table[key][subkeys[0]]):
            for idx,el in enumerate(group):
                if value in el:
                    good_idx.append(idx)
            for i in good_idx:
                good_values.append(table[key][subkeys[1]][jdx][i])
    print(good_idx)
    print(good_values)
    if turn < len(table.keys())-1:
        get_min_location(good_values, table, turn)
    else:
        return good_values
    
def analyze_table(table):
    results = {
        'seed': [],
        'soil': [],
        'fertilizer': [],
        'water': [],
        'light': [],
        'temperature': [],
        'humidity': [],
        'location': []
    }
    keys = [key for key in table.keys()]
    for idx,key in enumerate(keys):
        good_idx = []
        if idx != 0:
            subkeys = [sub for sub in table[key].keys()]
            for value in values:
                if value in table[key][subkeys[0]]:
                    results[subkeys[0]].append(value)
                    good_idx.append(table[key][subkeys[0]].index(value))
            values = []
            for i in good_idx:
                try:
                    values.append(table[key][subkeys[1]][i])
                except:
                    print(table[key][subkeys[1]])
        else:
            values =  table[key]
    return results


puzzle = example #read_file()
map_data = get_data(puzzle)
table = get_table(map_data)
print(analyze_table(table))


#'seed': [98, 99, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97],
#'soil': [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#'soil':        [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
 #'fertilizer': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]