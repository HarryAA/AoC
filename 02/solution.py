from functools import reduce

with open("input.txt", "r") as fp:
    data = fp.readlines()   

cube_totals = {"red": 12, "green": 13, "blue": 14}
def check_valid(game):
    for round in game.split(";"):
        for colour in round.split(","):
            if int(colour.strip().split(" ")[0]) > cube_totals[colour.strip().split(" ")[1]]:
                return False
    return True 

def get_power(line):
    colours = {"red": [], "green": [], "blue": []}
    for round in line.split(":")[1].split(";"):
        for colour in round.split(","):
            colours[colour.strip().split(" ")[1]].append(int(colour.strip().split(" ")[0]))
    return reduce(lambda x, y: x*y, [max(colours[colour]) for colour in colours])

print(sum([int(line.split(":")[0].split(" ")[1]) for line in data if check_valid(line.split(":")[1])]))
print(sum(map(get_power, data)))