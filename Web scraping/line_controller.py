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

# Finds lines with"Odlišné stanovisko"
# the word for other here is meant for "Odlišné stanovisko".
def other(text, lines):
    lines_with_others = []
    for line in text:
        for word in others:
            if word in line and len(line) > 80:
                lines_with_others.append(line)
                break
    if len(lines_with_others) != 0:
        lines.append(lines_with_others)

# Preciser trimmer that controls if there is
# really "Odlišné stanovisko" in the line.
# Collection of other_lines contains lines
# that are suspicious and must be manually
# controlled.
def preciser_trimmer(lines, other_lines):
    better_lines = []
    for file in lines:
        lines_with_others = []
        for line in file:
            found = 0
            for other in better_others:
                if other in line[:100]:
                    lines_with_others.append(line)
                    found = 1
                    break
            if found == 0:
                other_lines.append(line)
        if len(lines_with_others) != 0:
            better_lines.append(lines_with_others)
    return better_lines