def new_lines(line1, line2):
    if not isinstance(line1, str) or not isinstance(line2, str):
        return 0
    elif line1 == line2:
        return 1
    elif len(line1) > len(line2):
        return 2
    elif line2 == "learn" and line1 != "learn":
        return 3

print(new_lines(2, "3"))
print(new_lines("2", "2"))
print(new_lines("oeirfk", "oeir"))
print(new_lines('poe', "learn"))