import os
import shutil

def sort_files_by_extension(directory):
    """
    Organizes files in the specified directory into subfolders by file extension.
    Args:
        directory (str): The path to the directory to sort.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} is not a valid directory.")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Get file extension (without dot, lowercased)
            ext = os.path.splitext(filename)[1][1:].lower()
            if not ext:
                ext = "no_extension"
            folder_path = os.path.join(directory, ext)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, filename))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sort files in a directory by extension.")
    parser.add_argument("directory", help="Directory to sort")
    args = parser.parse_args()

    try:
        sort_files_by_extension(args.directory)
        print(f"Files in '{args.directory}' sorted by extension.")
    except Exception as e:
        print(f"Error: {e}")
