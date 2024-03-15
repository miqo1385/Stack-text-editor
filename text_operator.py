class TextOperation:
    def __init__(self, operation_type, character=None):
        self.operation_type = operation_type
        self.character = character


class TextEditor:
    def __init__(self):
        self.text = ""
        self.operation_stack = []

    def add_character(self, char):
        self.text += char
        self.operation_stack.append(TextOperation("add", char))
        self.display()

    def delete_character(self):
        if self.text:
            deleted_char = self.text[-1]
            self.text = self.text[:-1]
            self.operation_stack.append(TextOperation("delete", deleted_char))
            self.display()
        else:
            print("Text is already empty")

    def undo(self):
        if self.operation_stack:
            last_operation = self.operation_stack.pop()
            if last_operation.operation_type == "add":
                self.text = self.text[:-1]
            elif last_operation.operation_type == "delete":
                self.text += last_operation.character
            self.display()
        else:
            print("No more operations to undo")

    def display(self):
        print("Current text:", self.text)


def main():
    editor = TextEditor()
    while True:
        print("\nOptions:")
        print("1. Add character")
        print("2. Delete last character")
        print("3. Undo")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            char = input("Enter character to add: ")
            editor.add_character(char)
        elif choice == "2":
            editor.delete_character()
        elif choice == "3":
            editor.undo()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
