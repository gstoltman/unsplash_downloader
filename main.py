import requests
import os

url = input('Enter url: ')
folder_path = r"C:/Users/Grant/Desktop/backgrounds"

response = requests.get(url)

if response.status_code == 200:
    with open(os.path.join(folder_path, "image.jpg"), "wb") as f:
        f.write(response.content)
        print("Image saved to:", os.path.join(folder_path, "image.jpg"))
else:
    print("Failed to download image")