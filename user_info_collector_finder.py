with open("./info_file.txt", "r") as stored_data:
    data_info = stored_data.read().split("-" * 20)

find_name = input("\nPlease enter the name you want to find: ").strip()

for entry in data_info:
    if find_name in entry:
        print("\nInformation found.\n")
        print("\nUploading the informations: \n")
        print(entry.strip())
        break
else:
        print("\nThe person's information can't be found.")