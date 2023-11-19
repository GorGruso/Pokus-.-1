# Goes through collaborations and fullfils a score array, which tells who collaborated with who.
def process_colaborations(arr_of_colab, score, arr_of_ppl):
    for one_colab in arr_of_colab:
        if len(one_colab) == 1:
            for ppl in arr_of_ppl:
                if one_colab[0] in list(ppl.keys()):
                    my_id = ppl.get(one_colab[0])
                    break
            score[my_id][my_id] += 1
        else:
            for human in one_colab:
                compute_colab(human, one_colab, score, arr_of_ppl)
    return score

# Goes through one collab array.
def compute_colab(human, one_colab, score, arr_of_ppl):
    for ppl in arr_of_ppl:
        if human in list(ppl.keys()):
            id1 = ppl.get(human)
            break
    for i in range(len(one_colab)):
        if one_colab[i] == human:
            continue
        for ppl in arr_of_ppl:
            if one_colab[i] in list(ppl.keys()):
                id2 = ppl.get(one_colab[i])
                break
        score[id1][id2] += 1

# Creates NxN array with zeros where N = num.
def init_colab(num):
    my_list = list()
    for i in range(num):
        a = list()
        for j in range(num):
            a.append(0)
        my_list.append(a)
    return my_list

# Tells how many each human had collaborations.
def compute_number_of_collaborations(arr_of_colab, arr_of_ppl, num_of_colab):
    for colab in arr_of_colab:
        for human in colab:
            id = len(num_of_colab)
            for ppl in arr_of_ppl:
                if human in list(ppl.keys()):
                    id = ppl.get(human)
                    break
            num_of_colab[id] += 1
