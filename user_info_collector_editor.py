def personal_info(data):
    user_info = [] # This will store the data for one person
    
    for info in data: # Loop through each info in the data list
        ask_user = input(f"{info}: ") # Ask user for input
        if ask_user:
            user_info.append(ask_user)
        else:
            user_info.append("N/A") # Append the input or "N/A" if blank
    return user_info

def write_info(people, data, filename="info_file.txt"):
    collected_info = open("./info_file.txt", "w") # Open a text file in write mode

    for person in people: 
        for info_index in range(len(data)):
            collected_info.write(f"{data[info_index]}: {person[info_index]}\n")

    collected_info.close()

def main():

    # Main function to collect and save personal information

    print("\nPersonal Information Collector\n")

    data = ["Full Name", "Age", "Address", "Contact Number", "Email", "Occupation", "Marital Status", "Nationality", "Gender", "Hobbies", "Source of Income"]
    people = []

    while True:
        print("\nProvide the details for one person: \n")
        user_info = personal_info(data)
        people.append(user_info)
        
        another_entry = input("Add another person as an entry? (yes/no): ")
        if another_entry != "yes":
            break
    
    write_info(people, data)
    print("\nAll data have been saved. Rest asured that you informations will be kept hidden. Thank you!")

