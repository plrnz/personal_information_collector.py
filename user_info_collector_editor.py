def personal_info(data):
    user_info = [] # This will store the data for one person
    for info in data: # Loop through each info in the data list
        ask_user = input(f"{info}: ") # Ask user for input
        user_info.append(ask_user if ask_user else "N/A") # Append the input or "N/A" if blank
    return user_info

def write_info(people, data, filename="info_file.txt"):
    collected_info = open("./info_file.txt", "w") # Open a text file in write mode


    collected_info.close()