import os
import chardet

def create_folder_structure(root_dir, output_file):
    """
    Generates a folder structure of the given directory and saves it to a txt file.
    """
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            level = dirpath.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write('{}{}/\n'.format(indent, os.path.basename(dirpath)))
            subindent = ' ' * 4 * (level + 1)
            for filename in filenames:
                f.write('{}{}\n'.format(subindent, filename))

def detect_encoding(file_path):
    """
    Detects the encoding of a file.
    """
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def read_file_contents(file_path):
    """
    Reads the contents of a file with the correct encoding.
    """
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

def generate_context_for_files(file_paths, output_file):
    """
    Generates a context file with contents of each file in the given list of file paths.
    """
    with open(output_file, 'w') as f:
        for file_path in file_paths:
            try:
                content = read_file_contents(file_path)
                f.write(f"{file_path}\n")
                f.write(content)
                f.write("\n\n")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

def generate_context_for_folders(root_dir, folder_paths, output_file):
    """
    Generates a context file with contents of each file in the given list of folder paths.
    """
    with open(output_file, 'w') as f:
        for folder_path in folder_paths:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(file_path, root_dir)
                    try:
                        content = read_file_contents(file_path)
                        f.write(f"```{relative_path}\n")
                        f.write(content)
                        f.write("```\n\n")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

def find_occurrences(root_dir, target_name, search_files=True):
    """
    Finds all occurrences of a file or folder name within the root directory.
    """
    occurrences = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if search_files and target_name in filenames:
            occurrences.append(os.path.join(dirpath, target_name))
        elif not search_files and target_name in dirnames:
            occurrences.append(os.path.join(dirpath, target_name))
    return occurrences

def get_user_selection(options, item_type):
    """
    Prompts the user to select one, many, or all items from the list of options.
    """
    print(f"Found the following {item_type}s:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    selection = input(f"Select {item_type}s (comma separated numbers or 'all'): ")
    if selection.lower() == 'all':
        return options
    else:
        indices = list(map(int, selection.split(',')))
        return [options[i-1] for i in indices]

def menu():
    while True:
        print("\nMenu:")
        print("1. Create folder structure")
        print("2. Generate context for a folder/file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            root_dir = input("Enter the root directory: ")
            output_file = input("Enter the output txt file name: ")
            create_folder_structure(root_dir, output_file)
            print(f"Folder structure saved to {output_file}")
        elif choice == '2':
            root_dir = input("Enter the root directory: ")
            target_type = input("Generate context for a file or folder? (file/folder): ").strip().lower()

            if target_type == 'file':
                target_name = input("Enter the file name: ")
                file_paths = find_occurrences(root_dir, target_name, search_files=True)
                if file_paths:
                    selected_files = get_user_selection(file_paths, 'file')
                    output_file = input("Enter the output txt file name: ")
                    generate_context_for_files(root_dir, selected_files, output_file)
                    print(f"Context saved to {output_file}")
                else:
                    print(f"No files named {target_name} found in {root_dir}")
            elif target_type == 'folder':
                target_name = input("Enter the folder name: ")
                folder_paths = find_occurrences(root_dir, target_name, search_files=False)
                if folder_paths:
                    selected_folders = get_user_selection(folder_paths, 'folder')
                    output_file = input("Enter the output txt file name: ")
                    generate_context_for_folders(root_dir, selected_folders, output_file)
                    print(f"Context saved to {output_file}")
                else:
                    print(f"No folders named {target_name} found in {root_dir}")
            else:
                print("Invalid type. Please enter 'file' or 'folder'.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
