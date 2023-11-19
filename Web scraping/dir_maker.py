import os
from line_trimmer import *
from process_line import *
from output import *
from make_colab import *

ppl31 = {"Fenyk": 0,
       "Rychetsk": 1,
       "Filip": 2,
       "Tomkov": 3,
       "Musil": 4,
       "Sládeč": 5,
       "Ludvík": 6,
       "Šimáčkov": 7,
       "Suchán": 8,
       "Zemán": 9,
       "Šimíč": 10,
       "Lichovník": 11,
       "Uhlíř": 12,
       "Jirs": 13,
       "Fial": 14,
       "Šámal": 15}

ppl21 = {"Výborn": 0,
       "Rychetsk": 1,
       "Lastoveck": 2,
       "Güttler": 3,
       "Musil": 4,
       "Holländ": 5,
       "Nykodým": 6,
       "Balík": 7,
       "Židlick": 8,
       "Formánkov": 9,
       "Kůrk": 10,
       "Janů": 11,
       "Zarembov": 12,
       "Varvařovsk": 13,
       "Wagnerov": 14,
       "Ducho": 15,
       "Much": 16,
       "Malenovsk": 17}

ppl1 = {"Brož": 0,
       "Cepl": 1,
       "Čermák": 2,
       "Güttler": 3,
       "Holeč": 4,
       "Holländ": 5,
       "Jurk": 6,
       "Kessler": 7,
       "Klokočk": 8,
       "Paul": 9,
       "Procházk": 10,
       "Ševčík": 11,
       "Zarembov": 12,
       "Janů": 13,
       "Varvařovsk": 14,
       "Wagnerov": 15,
       "Ducho": 16,
       "Much": 17,
       "Malenovsk": 18,
        "Výborn": 19,
         "Rychetsk": 20,
         "Lastoveck": 21,
         "Musil": 22,
         "Nykodým": 23,
         "Balík": 24,
         "Židlick": 25,
         "Formánkov": 26,
         "Kůrk": 27,
         "Fenyk": 28,
         "Filip": 29,
         "Sládečk": 30,
         "Ludvík": 31,
         "Šimáčkov": 32,
         "Suchán": 33,
         "Zemán": 34,
         "Šimíč": 35,
         "Lichovník": 36,
         "Uhlíř": 37,
         "Jirs": 38,
         "Fial": 39,
         "Šámal": 40,
         "Tomkov": 41}

ppl12 = {"I.B.": 0,
       "V.C.": 1,
       "V.Č.": 2,
       "V.G.": 3,
       "M.H.": 4,
       "P.H.": 5,
       "V.J.": 6,
       "Z.K.": 7,
       "V.K.": 8,
       "V.P.": 9,
       "A.P.": 10,
       "V.Š.": 11,
       "E.Z.": 12,
       "I.J.": 13,
       "P.V.": 14,
       "E.W.": 15,
       "F.D.": 16,
       "J.M.": 17,
       "J.M.": 18}

ppl13 = {"I. B.": 0,
       "V. C.": 1,
       "V. Č.": 2,
       "V. G.": 3,
       "M. H.": 4,
       "P. H.": 5,
       "V. J.": 6,
       "Z. K.": 7,
       "V. K.": 8,
       "V. P.": 9,
       "A. P.": 10,
       "V. Š.": 11,
       "E. Z.": 12,
       "I. J.": 13,
       "P. V.": 14,
       "E. W.": 15,
       "F. D.": 16,
       "J. M.": 17,
       "J. M.": 18}

ppl14 = {"I.  B.": 0,
       "V.  C.": 1,
       "V.  Č.": 2,
       "V.  G.": 3,
       "M.  H.": 4,
       "P.  H.": 5,
       "V.  J.": 6,
       "Z.  K.": 7,
       "V.  K.": 8,
       "V.  P.": 9,
       "A.  P.": 10,
       "V.  Š.": 11,
       "E.  Z.": 12,
       "I.  J.": 13,
       "P.  V.": 14,
       "E.  W.": 15,
       "F.  D.": 16,
       "J.  M.": 17,
       "J.  M.": 18}

my_dirs = ["period01",
            "period02",
            "period03"]

# Goes through all files in one dir
def make_dir(conf):
    if conf == 0:
        dirs = my_dirs
    else:
        dirs = list(choose_dir(conf))
    my_lines = []
    for dir in dirs:
        scan_files(dir, my_lines)
    other_lines = []
    lines = more_trimmer(my_lines, other_lines)
    arr_of_ppl = choose_ppl(conf)
    bad_lines = []
    num = len(list(arr_of_ppl[0].keys()))
    fail_files = []
    arr_of_colab = process_lines(lines, bad_lines, arr_of_ppl, fail_files)
    num_of_colabs = []
    for i in range(num):
        num_of_colabs.append(0)
    if conf == 0:
        my_good_files = fail_files[2:]
        fail_files = fail_files[0:2]
    elif conf == 1:
        my_good_files = []
    else:
        my_good_files = fail_files
        fail_files = []
    process_good_files(my_good_files, arr_of_colab, arr_of_ppl)
    print("Config " + str(conf) + " - len: " + str(len(arr_of_colab)))
    score = go_through_all_colab(arr_of_colab, init_colab(num), arr_of_ppl)

    how_many_collabs(arr_of_colab, arr_of_ppl, num_of_colabs)
    tab_output(score, num, conf)
    my_bad_lines(bad_lines, conf)
    my_other_lines(other_lines, conf)
    my_bad_file(fail_files, conf)
    my_how_many_collabs(num_of_colabs, num, conf)


# Finds words "Odlišné" in all files and fulfill array lines with the lines with this word
def scan_files(dir, lines):
    for filename in os.listdir("data/" + dir):
        if filename[-4:] != "html":
            continue
        f = open("data/" + dir + "/" + filename, "rt", encoding="utf-8")
        text = f.read().split('\n')
        other(text, lines)
        f.close()

def choose_ppl(conf):
    arr = []
    if conf == 1:
        arr.append(ppl1)
        arr.append(ppl12)
        arr.append(ppl13)
        arr.append(ppl14)
    elif conf == 2:
        arr.append(ppl1)
    elif conf == 3:
        arr.append(ppl1)
    else:
        arr.append(ppl1)
        arr.append(ppl12)
        arr.append(ppl13)
        arr.append(ppl14)
    return arr


def choose_dir(conf):
    return [my_dirs[conf - 1]]