with open("./info_file.txt", "r") as stored_info:
    lines = stored_info.readlines()


data_info = []
one_person_info = [] 

for line in lines:
    if "-" * 40 in line:
        if one_person_info:
            data_info.append(one_person_info)
        one_person_info = []
    else:
        one_person_info.append(line.strip())

if one_person_info:
    data_info.append(one_person_info)

for entry in data_info:

    for info in entry:
        print(info)
    print("-•-" * 20)