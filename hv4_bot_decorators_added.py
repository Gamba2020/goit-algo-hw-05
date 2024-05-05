def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(cmd, args):

        try:
            return func(cmd, args)
        except IndexError:
            return print("Enter the argument for the command")
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Wrong format of argument"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ")
        cmd, args = parse_input(user_input)
        if cmd == "hello":
            print("How can I help you?")
        elif cmd == "add" :
            print(add_contact(args, contacts))
        elif cmd == "change" :
            print(change_contact(args, contacts))
        elif cmd == "phone" :
            print(show_phone(args, contacts))
        elif cmd == "all" :
            print(show_all(contacts))
        elif cmd in ["close", 'exit']:
            print("Good bye!")
            break

if __name__ == "__main__":
    main()



