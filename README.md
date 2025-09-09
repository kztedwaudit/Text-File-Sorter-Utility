# Text File Sorter Utility

A simple Python utility to organize files in a directory by their file extension. Each extension will get its own subfolder, making it easier to manage and locate files.

## Features

- Automatically sorts all files in a specified directory into subfolders by extension.
- Handles files with no extension (`no_extension` folder).
- Cross-platform (Windows, macOS, Linux).

## Usage

1. **Clone or Download** this repository.

2. **Run the script** from the command line:

   ```bash
   python text_file_sorter.py /path/to/your/directory
   ```

   Replace `/path/to/your/directory` with the directory you want to organize.

3. **Result:**  
   - Files will be moved into subfolders named after their extension (e.g., `txt`, `pdf`).
   - Files without an extension will be placed in a folder called `no_extension`.

## Example

Suppose your directory contains:
```
document.txt
image.png
notes.pdf
README
```
After running:
```bash
python text_file_sorter.py .
```
Your directory will look like:
```
txt/document.txt
png/image.png
pdf/notes.pdf
no_extension/README
```

## Requirements

- Python 3.x

No external dependencies are required.

## License

MIT License
