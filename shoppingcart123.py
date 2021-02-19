list = []

while True:
    command = input("Please add entries to the list,then type rearrange to remove duplicates: ").lower()
    if command != "rearrange":
        list.append(command)

    elif command == "rearrange":
        if not list:
            print("Please add entries to the list before rearranging.")

        else:
            break

for item in list:
    while list.count(item) > 1:
        list.remove(item)

print(list)