import csv

# Writes result of NxN array into the file where N = num.
def score_output(colab, num, period):
    row = []
    output = ""
    for i in range(num):
        out = []
        for j in range(num):
            output += str(colab[i][j])
            out.append(str(colab[i][j]))
            if j != (num - 1):
                output += ", "
        output += "\n"
        row.append(out)
        print(out)
    f = open("tabs/tab_result0" + str(period) + ".txt", "wt", encoding="cp852")
    f.write(output)
    f.close()
    f = open("tabs/tab0" + str(period) + ".csv", "w")
    writer = csv.writer(f)
    for i in range(num):
        writer.writerow(row[i])
    f.close()

# Output of not read lines into file.
def bad_lines_output(bad_lines, config):
    my_text = ""
    for line in bad_lines:
        if len(line) < 100:
            continue
        my_text += line
        my_text += "\n"
    f = open("wrongs/bad_result0" + str(config) + ".txt", "wt", encoding="utf-8")
    f.write(my_text)
    f.close()

# Output of not read lines into file.
def other_lines_output(bad_lines, config):
    my_text = ""
    for line in bad_lines:
        if len(line) < 100:
            continue
        my_text += line
        my_text += "\n"
    f = open("lines_with_other/other0" + str(config) + ".txt", "wt", encoding="utf-8")
    f.write(my_text)
    f.close()

# Output of not read files into file.
def bad_files_output(fail_files, config):
    output = ""
    for file in fail_files:
        output += "-------------------------------------------------------------\n"
        for line in file:
            output += line
            output += "\n"
    f = open("lines_with_other/bad_files0" + str(config) + ".txt", "wt", encoding="utf-8")
    f.write(output)
    f.close()

# Output of counts of collaborations of every human into file.
def collaborations_count_output(num_of_colabs, num, config):
    output = ""
    for i in range(num):
        output += str(num_of_colabs[i])
        output += "\n"
    f = open("lines_with_other/how_many_collabs0" + str(config) + ".txt", "wt", encoding="utf-8")
    f.write(output)
    f.close()
    f = open("lines_with_other/how_many_collabs0" + str(config) + ".csv", "w")
    writer = csv.writer(f)
    for i in range(num):
        writer.writerow(str(num_of_colabs[i]))
    f.close()