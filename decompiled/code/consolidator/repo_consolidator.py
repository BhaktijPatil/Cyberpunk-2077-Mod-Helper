import os
from pathlib import Path

def write_to_file(output_file, files):
    """Writes the contents of the files to the output file."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in files:
            outfile.write(f"File Name: {Path(file).name}\n")
            outfile.write(f"File Location: {file}\n\n")
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n-------------------------\n\n")

def collect_files(directory, extensions):
    """Collects all files with the specified extensions in the given directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                yield os.path.join(root, file)

def main():
    directory = input("Enter Repository Directory: ")
    extensions = input("Enter the file extensions to include (comma-separated): ").split(',')
    output_file = "cyberpunk_repo.txt"

    files = collect_files(directory, extensions)
    write_to_file(output_file, files)

    print(f"All files have been written to {output_file}")

if __name__ == "__main__":
    main()