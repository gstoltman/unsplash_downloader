import requests
import os
import webbrowser


firefox_path = "/mnt/c/'Program Files'/'Mozilla Firefox'/firefox.exe %s"
webbrowser.register('firefox', None, firefox_path)

tab_url = webbrowser.get('firefox').tab.url

print(tab_url)

# Set the directory where you want to save the image
#directory = '/home/gstoltman/pictures/wallpapers/'

# Send a GET request to the URL to download the image
#response = requests.get(url)

# Extract the filename from the URL
#filename = 'image.jpg'

# Join the directory and filename to create the full file path
#filepath = os.path.join(directory, filename)

# Write the image to the file
#with open(filepath, 'wb') as f:
#    f.write(response.content)

#print(f'Successfully downloaded and saved {filename} to {directory}.')