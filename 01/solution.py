with open("input.txt", "r") as fp:
    data = fp.readlines()    

def convert(line):
    conversions = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
        "zero": "z0o"
    }
    for k, v in conversions.items():
        line = line.replace(k, v)
    return line  

print(f"Part 1 = {sum(map(lambda x: int(x[0])*10 + int(x[-1]), [[n for n in line if n.isnumeric()] for line in data]))}")
print(f"Part 2 = {sum(map(lambda x: int(x[0])*10 + int(x[-1]), [[n for n in convert(line) if n.isnumeric()] for line in data]))}")