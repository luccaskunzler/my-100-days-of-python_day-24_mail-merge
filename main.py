clear_lines = []
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    lines = letter.readlines()
    for line in lines:
        new_line = line.strip("\n")
        clear_lines.append(new_line)
    print(clear_lines)

clear_list_of_guests = []
with open("./Input/Names/invited_names.txt") as guests:
    list_of_guests = guests.readlines()
    for line in list_of_guests:
        new_line = line.strip("\n")
        clear_list_of_guests.append(new_line)
    print(clear_list_of_guests)
    print(len(list_of_guests))

for i in range(0,len(list_of_guests)):
    with open(f'./Output/ReadyToSend/{clear_list_of_guests[i]}.txt', 'w') as individual_letter:
        new_string = clear_lines[0].replace("[name]", clear_list_of_guests[i])
        individual_letter.write(new_string)
        for _ in range(1,len(clear_lines)):
            individual_letter.write("\n ")
            individual_letter.write(clear_lines[_])