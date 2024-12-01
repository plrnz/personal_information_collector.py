with open("./info_file.txt", "r") as stored_data:
    data_info = stored_data.read().split("-" * 20)

find_name = input("Please enter the name of the person that you want to have the information: ").strip()

for entry in data_info:
    if find_name in entry:
        print("Information found.\n")
        print(entry.strip())
        break
else:
        print("\nThe person's information can't be found.")