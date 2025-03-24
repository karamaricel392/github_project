import os
import hashlib
import requests

def generate_random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result = ''.join(random.choice(characters) for _ in range(length))
    return result

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)

def hash_download_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(1024 * 1024)  # read a chunk of 1MB
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def main():
    url = "https://example.com/upload"
    filename = "random_string.txt"
    
    while True:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        random_string = generate_random_string(10)  # Generate a random string of length 10
        download_file(url, filename + "_" + random_string)
        
        hash_value = hash_download_file(filename + "_" + random_string)
        if hash_value == "YOUR_HASH_VALUE":
            print(f"File saved as {filename}")
            break

if __name__ == "__main__":
    main()
