vowels = ["A", "E", "I", "O", "U"]

while True:
    line = input()
    if line == "#":
        break

    count = 0
    for ch in line.upper():
        if ch in vowels:
            count += 1
    print(count)
