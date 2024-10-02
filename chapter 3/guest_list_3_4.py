guest_list = ["Chase Utley", "Andy Reid", "Mike Schmidt", "Donald Trump"]
print(f"Dear {guest_list[0].title()} I would like to invite you to lunch on")


print(guest_list[1] + " will not be making the party")

guest_list[1] = "Pete Rose"

for item in guest_list:
    print(item + " we have found a bigger table")

guest_list.insert(0, "Aiden")
guest_list.insert(3, "Amanda")
guest_list.append("Bob")

