# Makes array of colabs from lines with "Odlišné stanovisko".
def process_lines(lines, bad_lines, arr_of_ppl, fail_files):
    output = []
    for file in lines:
        colaborations = []
        used_ppl = []
        ret = True
        for line in file:
            if len(arr_of_ppl) > 1 and ("J.M." in line or "J. M." in line or "J.  M." in line):
                bad_lines.append(line)
                continue
            colab = []
            for ppl in arr_of_ppl:
                ret = finding_humans(ppl, colab, line, used_ppl)
                if not ret:
                    break
            if not ret:
                break
            if len(colab) != 0 and ret:
                print(colab)
                colaborations.append(colab)
            if len(colab) == 0:
                bad_lines.append(line)
        if not ret:
            fail_files.append(file)
        else:
            for succ_colab in colaborations:
                output.append(succ_colab)
    return output

# Creates a collaboration from Humans in the line.
def finding_humans(ppl, colab, line, used_ppl):
    for human in list(ppl.keys()):
        if human in line[:500]:
            if human in used_ppl:
                print("-----------------------")
                print(human)
                print("-----------------------")
                return False
            used_ppl.append(human)
            colab.append(human)
        elif human in line[-300:]:
            if human in used_ppl:
                print("-----------------------")
                print(human)
                print("-----------------------")
                return False
            used_ppl.append(human)
            colab.append(human)
    return True


def process_good_files(good_files, arr_of_colab, my_ppl):
    print("HERE  ARE  BAD  FILES\n")
    for file in good_files:
        print("FILE")
        for line in file:
            colab = []
            for ppl in my_ppl:
                for human in ppl:
                    if human in line[:108]:
                        colab.append(human)
            print(colab)
            arr_of_colab.append(colab)




