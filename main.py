import requests
import shutil

url = input('Enter url: ')

folder_path = "home/gstoltman/pictures/wallpapers/image.jpg"

response = requests.get(url, stream=True)

with open(url, "wb") as f:
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, f)
    print("Image saved to:", folder_path)