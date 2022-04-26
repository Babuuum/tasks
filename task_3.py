

def synthesis(file_name_1, file_name_2, file_name_3, result_file_name):

    crutch = []
    crutch_2 = {}
    crutch_3 = {}

    with open(file_name_1, mode="r", encoding="utf-8") as file_1:
        for line in file_1:
            crutch.append(line.strip())
    crutch_2[file_name_1] = crutch
    crutch_3[file_name_1] = len(crutch)
    crutch = []

    with open(file_name_2, mode="r", encoding="utf-8") as file_2:
        for line in file_2:
            crutch.append(line.strip())
    crutch_2[file_name_2] = crutch
    crutch_3[file_name_2] = len(crutch)
    crutch = []

    with open(file_name_3, mode="r", encoding="utf-8") as file_3:
        for line in file_3:
            crutch.append(line.strip())
    crutch_2[file_name_3] = crutch
    crutch_3[file_name_3] = len(crutch)
    crutch_4 = list(crutch_3.items())
    crutch_4.sort(key=lambda  sort: sort[1])

    with open(result_file_name, mode="w+", encoding="utf-8") as new_file:

        for search in crutch_4:
            new_file.write(f"{search[0]}\n{search[1]}\n")
            for search_2 in crutch_2[search[0]]:
                new_file.write(f"{search_2}\n")


synthesis("1.txt", "2.txt", "3.txt", "4.txt")
