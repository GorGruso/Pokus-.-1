others = ["Odlišné", "O d l i š n é", "ODLIŠNÉ", "O D L I Š N É"]
better_others = ["Odlišné stanovisko",
                 "ODLIŠNÉ STANOVISKO",
                 "O d l i š n é   s t a n o v i s k o",
                 "O d l i š n é  s t a n o v i s k o",
                 "Odlišné  stanovisko",
                 "O d l i š n é s t a n o v i s k o",
                 "O D L I Š N É  S T A N O V I S K O",
                 "Odlišné doplňující stanovisko",
                 "Odlišné-doplňující stanovisko"]
# finds lines of "Odlišné stanovisko"
def other(text, lines):
    my_file = []
    for line in text:
        for word in others:
            if word in line and len(line) > 80:
                my_file.append(line)
                break
    if len(my_file) != 0:
        lines.append(my_file)


def more_trimmer(lines, other_lines):
    my_better_lines = []
    output = ""
    for file in lines:
        my_file = []
        for line in file:
            found = 0
            for other in better_others:
                if other in line[:100]:
                    my_file.append(line)
                    found = 1
                    break
            if found == 0:
                other_lines.append(line)
        if len(my_file) != 0:
            my_better_lines.append(my_file)
    return my_better_lines