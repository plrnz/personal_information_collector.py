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