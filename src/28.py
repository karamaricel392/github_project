import requests

def main():
    url = "https://api.example.com/data"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data received successfully")
    else:
        print(f"Failed to receive data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
