with open("./info_file.txt", "r") as stored_info:
    lines = stored_info.readlines()


data_info = []
one_person_info = [] 

for line in lines:
    if "-•-" * 20 in line:
        if one_person_info:
            data_info.append(one_person_info)
        one_person_info = []
    else:
        one_person_info.append(line.strip())

if one_person_info:
    data_info.append(one_person_info)

entry_counter = 1
for entry in data_info:
    print(f"Entry #{entry_counter}")
    for info in entry:
        print(info)
    print("-•-" * 20)
    entry_counter += 1
    