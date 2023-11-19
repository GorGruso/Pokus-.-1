import os
from line_controller import *
from line_processor import *
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

directory_names = ["period01",
                   "period02",
                   "period03"]


# Goes through all files in one directory
def process_directories(configuration):

    # Getting Directories
    if configuration == 0:
        directories = directory_names
    else:
        directories = list(choose_directory(configuration))

    # Lines operations
    found_lines = []
    for directory in directories:
        scan_files(directory, found_lines)
    manually_controlled_lines = []
    lines = preciser_trimmer(found_lines, manually_controlled_lines)

    # People preparations
    array_of_ppl = choose_ppl(configuration)
    bad_lines = []
    count_of_ppl = len(list(array_of_ppl[0].keys()))

    # Building collaborations
    failed_files = []
    array_of_colab = process_lines(lines, bad_lines, array_of_ppl, failed_files)
    num_of_colaborations = []
    for i in range(count_of_ppl):
        num_of_colaborations.append(0)
    if configuration == 0:
        good_files = failed_files[2:]
        failed_files = failed_files[0:2]
    elif configuration == 1:
        good_files = []
    else:
        good_files = failed_files
        failed_files = []
    process_good_files(good_files, array_of_colab, array_of_ppl)

    # Score and number of collaborations creation
    print("Configuration " + str(configuration) + " - len: " + str(len(array_of_colab)))
    score = process_colaborations(array_of_colab, init_colab(count_of_ppl), array_of_ppl)
    compute_number_of_collaborations(array_of_colab, array_of_ppl, num_of_colaborations)

    # Results output managing
    score_output(score, count_of_ppl, configuration)
    bad_lines_output(bad_lines, configuration)
    other_lines_output(manually_controlled_lines, configuration)
    bad_files_output(failed_files, configuration)
    collaborations_count_output(num_of_colaborations, count_of_ppl, configuration)


# Finds words "Odlišné" in all files and fulfill array lines with the lines with this word.
def scan_files(directory, lines):
    for filename in os.listdir("data/" + directory):
        if filename[-4:] != "html":
            continue
        f = open("data/" + directory + "/" + filename, "rt", encoding="utf-8")
        text = f.read().split('\n')
        other(text, lines)
        f.close()

# Picks only the right arrays of people that are occuring in the period due to the configuration.
def choose_ppl(configuration):
    arr = []
    if configuration == 1:
        arr.append(ppl1)
        arr.append(ppl12)
        arr.append(ppl13)
        arr.append(ppl14)
    elif configuration == 2:
        arr.append(ppl1)
    elif configuration == 3:
        arr.append(ppl1)
    else:
        arr.append(ppl1)
        arr.append(ppl12)
        arr.append(ppl13)
        arr.append(ppl14)
    return arr


def choose_directory(configuration):
    return [directory_names[configuration - 1]]
