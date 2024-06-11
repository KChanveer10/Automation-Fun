import os
import fnmatch
import re
import argparse

def find_files_with_keywords(root_dir, keywords, file_extension):
    matches = []
    # Compile the regex pattern once
    pattern = re.compile(r".*(" + "|".join(re.escape(keyword) for keyword in keywords) + r").*\." + re.escape(file_extension) + r"$")
    
    for root, dirnames, filenames in os.walk(root_dir):
        for name in filenames:
            if fnmatch.fnmatch(name, f"*.{file_extension}") and pattern.match(name):
                matches.append(os.path.join(root, name))
                
    return matches

def main():
    parser = argparse.ArgumentParser(description="Find files with specific keywords in filenames.")
    parser.add_argument('folder_path', type=str, help='The folder path to search within')
    parser.add_argument('keywords', type=str, nargs='+', help='Keywords to look for in filenames')
    parser.add_argument('--extension', type=str, required=True, help='File extension to look for (e.g., docx, txt, pdf)')

    args = parser.parse_args()
    root_directory = args.folder_path
    keywords = args.keywords
    file_extension = args.extension

    found_files = find_files_with_keywords(root_directory, keywords, file_extension)

    if found_files:
        for file_path in found_files:
            print(f"Found file: {file_path}")
    else:
        print("No matching files found")

if __name__ == "__main__":
    main()
