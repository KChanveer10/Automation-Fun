# GitHub File Downloader & File Finder Utility

## GitHub File Downloader

### Overview

The GitHub File Downloader is a Python script that allows users to download selected files from a GitHub repository and save them into a Word document. The script utilizes the GitHub API to fetch the contents of the repository and the requests library to download the files. It then uses the python-docx library to create a Word document and populate it with the contents of the selected files.

### Features

- Fetches the contents of a GitHub repository using the GitHub API.
- Allows users to select specific files from the repository to include in the Word document.
- Downloads the selected files and saves them into a Word document.
- Provides an easy-to-use interface for inputting GitHub username, repository name, and selecting files.

### Usage

1. Run the script (`wordfilegen.py`).
2. Enter your GitHub username when prompted.
3. Enter the name of the repository you want to download files from.
4. Select the files you want to include in the Word document by entering their indices separated by commas.
5. The script will download the selected files and save them into a Word document named `<repository_name>_files.docx`.

### Dependencies

- requests: For making HTTP requests to the GitHub API.
- python-docx: For creating and manipulating Word documents.
- tkinter: For creating a simple GUI for user input (only when running as an executable).

### Limitations

- Requires an active internet connection to fetch files from the GitHub repository.
- Only supports downloading files from public GitHub repositories.
- Does not handle authentication for private repositories.

### Future Improvements

- Add support for downloading files from private repositories by handling authentication.
- Enhance error handling and provide more informative error messages.
- Allow users to specify the output directory for the Word document.
- Implement progress indicators for file download and document creation processes.

---

## File Finder Utility

### Overview

The File Finder Utility is a command-line tool designed to search for files with specific keywords in their filenames within a specified directory and its subdirectories. The tool supports searching for any file type by specifying the file extension.

### Features

- Search for files containing specified keywords in their filenames.
- Supports any file type by specifying the file extension.
- Recursively searches through all subdirectories.
- Optimized for performance with efficient file filtering and concurrent processing.

### Requirements

- Python 3.6 or higher
- `argparse` module (included with Python standard library)
- `concurrent.futures` module (included with Python standard library)
- `PyInstaller` for creating the executable

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/KChanveer10/Automation-Fun.git
    ```

2. **Install dependencies**:
    ```sh
    pip install pyinstaller
    ```

### Usage

#### Running the Script

You can run the script directly using Python:

```sh
python fun.py <folder_path> <keywords> --extension <file_extension>
```

### Creating an Executable

1. **Navigate to the script's directory**:
    ```sh
    cd path_to_your_script
    ```

2. **Run PyInstaller**:
    ```sh
    pyinstaller --onefile <python file>
    ```

    This command generates a single executable file for your script. PyInstaller will create several directories and files, but the most important output will be located in the `dist` directory.

3. **Locate the Executable**:
   
    After PyInstaller completes, the executable will be created in the `dist` directory within your current working directory.

### Running the Executable

Run the executable from the command line, passing the folder path, keywords, and file extension as arguments:
1. **For File Finder Utility**
```sh
dist/<exe file> <folder_path> <filename> --extension <file_extension>
```
2. **For  GitHub File Downloader**
```sh
dist/<exe file>
```

