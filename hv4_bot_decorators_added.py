from typing import Callable, Dict

def input_error(func):
    def inner(cmd, *args):
        try:
            return func(cmd, *args)
        except IndexError:
            return print("Enter the argument for the command")
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Wrong format of argument"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def hello(args, contacts):
    return "How can I help you?"

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated"

def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all(args, contacts):
    for name, phone in contacts.items():
        return f"{name}: phone: {phone}"

operations: Dict[str, Callable] = {
    "hello": input_error(hello),
    "add": input_error(add_contact),
    "change": input_error(change_contact),
    "show": input_error(show_phone),
    "all": input_error(show_all)
}

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)
        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd in operations:
            result = operations[cmd](args, contacts)
            print(result)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()


