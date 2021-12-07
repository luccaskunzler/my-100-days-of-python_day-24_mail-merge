# opens the sample letter
with open("./Input/Letters/starting_letter.txt", "r") as sample_letter:
    letter = sample_letter.read()

# opens the guest list and creates a list with the individual names.
with open("./Input/Names/invited_names.txt") as guests:
    list_of_guests = guests.readlines()
    for guest in list_of_guests:
        # for every guest name, strip can be used to remove unwanted characters
        stripped_name = guest.strip()
        # individually creates the invitations
        with open(f'./Output/ReadyToSend/{stripped_name}.txt', 'w') as final_letter:
            new_string = letter.replace("[name]", stripped_name)
            final_letter.write(new_string)
