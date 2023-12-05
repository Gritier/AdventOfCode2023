import re
import time

start_time = time.time()

def read_file(file="input.txt"):
    with open(file,"r") as f:
        return f.read().splitlines()

#example = ['seeds: 79 14 55 13','','seed-to-soil map:','50 98 2','52 50 48','','soil-to-fertilizer map:','0 15 37','37 52 2','39 0 15','','fertilizer-to-water map:','49 53 8','0 11 42','42 0 7','57 7 4','','water-to-light map:','88 18 7','18 25 70','','light-to-temperature map:','45 77 23','81 45 19','68 64 13','','temperature-to-humidity map:','0 69 1','1 0 69','','humidity-to-location map:','60 56 37','56 93 4']

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
            if flag == 1:
                temp = []
                for match in re.finditer("\d+", line):
                    temp.append(int(match.group()))
                temp_data[key].append(temp)
            if key in line:
                flag = 1
            elif line == "" and flag==1:
               break
            
    
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
                    table[key][subkeys[0]].append(range(el[0],el[0]+el[2]))
                    table[key][subkeys[1]].append(range(el[1],el[1]+el[2]))
    return table

def starting_confront(value, key, table):
    subkeys = table[key].keys()
    good_idx = []
    
    for idx,el in enumerate(table[key][subkeys[0]]):
        if value in el:
            good_idx.append(idx)
    

    pass

puzzle = read_file()
map_data = extract_data(puzzle)
table = get_table(map_data)
print(table)
