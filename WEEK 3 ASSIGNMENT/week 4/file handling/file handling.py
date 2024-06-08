# file_handling_assignment.py

def main():
    try:
        # File Creation and Writing
        with open("my_file.txt", "w") as file:
            file.write("Exploring the cosmos, one code at a time.\n")
            file.write("42: The answer to life, the universe, and everything.\n")
            file.write("Today's date: 2024-06-08\n")

        # File Reading and Display
        with open("my_file.txt", "r") as file:
            print("File Contents:")
            print(file.read())

        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("Appending new insights.\n")
            file.write("2024, the year of Pythonic mastery!\n")
            file.write("EOF: The end of file, but not the end of discovery.\n")

        # Reading and displaying the appended file contents
        with open("my_file.txt", "r") as file:
            print("\nUpdated File Contents:")
            print(file.read())

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied for accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nOperation completed. Ensuring all resources are properly managed.")

if __name__ == "__main__":
    main()
