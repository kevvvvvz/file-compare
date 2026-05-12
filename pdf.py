import hashlib
import sys


def compare(file1, file2):
    BUF_SIZE = 65536
    h1 = hashlib.sha256()
    h2 = hashlib.sha256()
    
    with open(file1, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            
            h1.update(data)
            
    with open(file2, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            
            h2.update(data)
            
    return h1.hexdigest(), h2.hexdigest()


def main():
    try:
        file_hash, file_hash2 = compare(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        print("Please enter a valid file path")
        sys.exit()
    
    if file_hash == file_hash2:
        print("These files are identical")
    else:
        print("These files are not identical")
    #print(f"Hash:{file_hash}")
    
    
main()
