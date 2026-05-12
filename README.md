# File Compare
A command-line Python tool that checks whether two files are identical using SHA-256 hashing. Works with any file type - PDFs, Word docs, images, and more.
 
---
 
## How to Use
1. Run the script from the terminal with two file paths as arguments
2. The tool hashes both files and compares the results
3. A message is printed telling you whether the files are identical or not
---
 
## Features
- Reads files in chunks for efficient memory usage
- SHA-256 hashing for accurate and reliable comparison
- Graceful error handling for invalid file paths
---
 
## Tech Stack
| Technology | Purpose |
|---|---|
| Python | Core logic |
| `hashlib` | SHA-256 file hashing |
| `sys` | Command-line argument handling |
 
---
 
## Getting Started
 
### Prerequisites
- Python 3 installed
### Installation
```bash
# Clone the repository
git clone https://github.com/kevvvvvz/file-compare.git
 
# Navigate into the project
cd file-compare
 
# Run the tool with two files
python compare.py file1.pdf file2.pdf
```
 
---
 
## Example Output
```
These files are not identical
```
```
These files are identical
```
 
---
