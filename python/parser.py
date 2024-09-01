output = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        new_line = line[0] + line[3] + line[1] + line[4] + line[2] + line[5]
        output.append(new_line)

with open('output.txt', 'w') as f:
    counter = 97
    for line in output:
        f.write(f"{str(int(line, 2))}: '{chr(counter)}',\n")
        counter += 1