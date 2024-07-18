
# Context Generator Script

## Overview

This Python script provides a menu-driven interface to perform two main tasks:
1. **Create a folder structure**: Generate a text file containing the folder structure of a specified directory.
2. **Generate context for a folder/file**: Create a text file containing the contents of specified files or folders within a given root directory, formatted to provide useful context for further processing or analysis.

## Features

1. **Create Folder Structure**: 
    - Scans a specified directory and generates a text file that outlines the folder structure.
    - Excludes common library folders like `__pycache__`, `node_modules`, `bin`, `obj`, and `lib`.

2. **Generate Context for a Folder/File**:
    - Allows you to specify a file or folder name and generates a context file containing the contents.
    - Handles multiple occurrences of the specified file or folder, allowing you to select one, many, or all.
    - Automatically detects and handles file encodings to avoid reading errors.
    - Excludes contents from common library folders.
    - Outputs file contents with relative paths based on the root directory.

## Usage

### Prerequisites

- Python 3.x
- `chardet` library for encoding detection. Install it using:
  \`\`\`sh
  pip install chardet
  \`\`\`

### Running the Script

1. **Clone or download the script to your local machine.**
2. **Navigate to the directory containing the script.**
3. **Run the script:**
   \`\`\`sh
   python script.py
   \`\`\`

### Menu Options

1. **Create Folder Structure**:
   - Prompts for a root directory.
   - Prompts for an output text file name.
   - Generates the folder structure and saves it to the specified text file.

2. **Generate Context for a Folder/File**:
   - Prompts for a root directory.
   - Asks if the target is a file or folder.
   - Prompts for the target file or folder name.
   - Searches for all occurrences of the specified file or folder within the root directory.
   - Allows selection of one, many, or all occurrences.
   - Prompts for an output text file name.
   - Generates the context and saves it to the specified text file.

3. **Exit**:
   - Exits the script.

## Example

\`\`\`plaintext
Menu:
1. Create folder structure
2. Generate context for a folder/file
3. Exit

Enter your choice: 2
Enter the root directory: /Users/user1/project/accounts-service
Is it a file or folder? (file/folder): file
Enter the target name: enums.py
Found the following files:
1. /Users/user1/project/accounts-service/module1/enums.py
2. /Users/user1/project/accounts-service/module2/enums.py
Select files (comma separated numbers or 'all'): all
Enter the output txt file name: context.txt
Context saved to context.txt
\`\`\`

## Notes

- Ensure that the root directory path is correctly specified.
- The script automatically excludes common library folders to avoid unnecessary content.
- Relative paths in the output context file are based on the provided root directory.
