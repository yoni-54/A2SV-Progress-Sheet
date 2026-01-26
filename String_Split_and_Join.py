def split_and_join(line):
    split = line.split(" ")
    join = "-".join(split)
    return join

line = input()
result = split_and_join(line)
print(result)