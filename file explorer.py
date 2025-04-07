import os

def list_directory(path):
    """Lists files and directories in the specified path."""
    try:
        print(f"\nContents of {path}:")
        for index, item in enumerate(os.listdir(path), start=1):
            print(f"{index}. {item}")
    except FileNotFoundError:
        print("The specified path does not exist.")
    except PermissionError:
        print("Permission denied to access this path.")

def view_file(path):
    """Displays the content of a text file."""
    try:
        with open(path, 'r') as file:
            print("\nFile Content:\n")
            print(file.read())
    except FileNotFoundError:
        print("The specified file does not exist.")
    except IsADirectoryError:
        print("This is a directory, not a file.")
    except Exception as e:
        print(f"Error reading file: {e}")

def delete_file(path):
    """Deletes the specified file."""
    try:
        os.remove(path)
        print(f"{path} has been deleted.")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except IsADirectoryError:
        print("This is a directory, not a file.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def rename_file(old_path, new_name):
    """Renames the specified file."""
    try:
        directory = os.path.dirname(old_path)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed to {new_path}")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"Error renaming file: {e}")

def main():
    # Set the initial path to "D:\C++ program"
    current_path = r"D:\java progam - Copy"
    
    print(f"Starting File Explorer in: {current_path}")
    
    while True:
        print("\nOptions:")
        print("1. List Directory Contents")
        print("2. View File")
        print("3. Delete File")
        print("4. Rename File")
        print("5. Change Directory")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            list_directory(current_path)
        elif choice == "2":
            file_name = input("Enter the file name to view: ").strip()
            view_file(os.path.join(current_path, file_name))
        elif choice == "3":
            file_name = input("Enter the file name to delete: ").strip()
            delete_file(os.path.join(current_path, file_name))
        elif choice == "4":
            file_name = input("Enter the file name to rename: ").strip()
            new_name = input("Enter the new name: ").strip()
            rename_file(os.path.join(current_path, file_name), new_name)
        elif choice == "5":
            new_path = input("Enter the new directory path: ").strip()
            if os.path.isdir(new_path):
                current_path = new_path
                print(f"Changed directory to {current_path}")
            else:
                print("Invalid directory path.")
        elif choice == "6":
            print("Exiting File Explorer.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()