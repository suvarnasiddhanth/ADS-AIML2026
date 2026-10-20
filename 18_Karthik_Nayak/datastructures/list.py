people = []

def display_people():
    if not people:
        print("List is empty.")
        return
    for i, person in enumerate(people):
        print(f"Index {i}: {person}")

def add_person():
    value = input("Enter value to add: ")
    people.append(value)
    print(f"{value} added.")

def update_person():
    display_people()
    if not people:
        return
    try:
        index = int(input("Enter index to update: "))
    except ValueError:
        print("Index must be a number.")
        return
    if 0 <= index < len(people):
        new_value = input("Enter new value: ")
        people[index] = new_value
        print(f"Index {index} updated to {new_value}.")
    else:
        print("Invalid index!")

def delete_person():
    display_people()
    if not people:
        return
    try:
        index = int(input("Enter index to delete: "))
    except ValueError:
        print("Index must be a number.")
        return
    if 0 <= index < len(people):
        removed = people.pop(index)
        print(f"Removed {removed} from index {index}.")
    else:
        print("Invalid index!")


def main():
    while True:
        print("PEOPLE LIST MENU ")
        print("1. Add person")
        print("2. Display all people")
        print("3. Update a person")
        print("4. Delete a person")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_person()
        elif choice == "2":
            print("Current list:")
            display_people()
        elif choice == "3":
            update_person()
        elif choice == "4":
            delete_person()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()