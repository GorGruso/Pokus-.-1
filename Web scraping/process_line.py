# makes array of colabs from lines with "Odlišné stanovisko"
def process_lines(lines, bad_lines, arr_of_ppl, fail_files):
    my_tab = []
    for file in lines:
        my_colabs = []
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
                my_colabs.append(colab)
            if len(colab) == 0:
                bad_lines.append(line)
        if not ret:
            fail_files.append(file)
        else:
            for my_colab in my_colabs:
                my_tab.append(my_colab)
    return my_tab


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
    print("HERE\nARE\nBAD\nFILES")
    for file in good_files:
        print("FILEEEEEEE")
        for line in file:
            colab = []
            for ppl in my_ppl:
                for human in ppl:
                    if human in line[:108]:
                        colab.append(human)
            print(colab)
            arr_of_colab.append(colab)




