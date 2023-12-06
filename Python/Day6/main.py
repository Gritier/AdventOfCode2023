import re

FILE = "input.txt"

class Race:
    def __init__(self, time, record):
        self.time = time
        self.record = record
    
    def __str__(self) -> str:
        return f'Time: {self.time}ms | Record: {self.record}mm'
    
def read_file(file=FILE):
    with open(file, "r") as f: 
        return f.read()

def parse_input(my_input=read_file()):
    races = []
    time_values = [int(match.group()) for match in re.finditer(r"\d+",my_input.split('\n')[0])]
    record_values = [int(match.group()) for match in re.finditer(r"\d+",my_input.split('\n')[1])]
    for i in range(len(time_values)):
        races.append(Race(time_values[i],record_values[i]))
    return races

def get_real_input(races):
    real_time = ''
    real_record = ''

    for race in races:
        real_time += str(race.time)
        real_record += str(race.record)

    return Race(int(real_time),int(real_record))

def race_results(race):
    result = {
        'hold': [],
        'distance': [],
        'status': []
    }
    for i in range(race.time+1):
        result['hold'].append(i)
        result['distance'].append(i*(race.time-i))
        result['status'].append(result['distance'][-1]>race.record)
    
    return result

def solve_part_1(all_results):
    solution = 1
    for result in all_results:
        real_wins = 0
        for win in result['status']:
            if win:
                real_wins += 1
        solution *= real_wins
    return solution

def solve_part_2(real_race):
    solution = 0
    for i in range(real_race.time+1):
        if i*(real_race.time-i) > real_race.record:
            solution += 1
    return solution

races = parse_input()
all_results = [race_results(race) for race in races]
real_race = get_real_input(races)

print(solve_part_1(all_results))
print(solve_part_2(real_race))



