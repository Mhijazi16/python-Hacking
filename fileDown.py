import requests
import pyfiglet
import tqdm


banner = pyfiglet.figlet_format("File \n Downloader")
print(banner)
url = input("Enter URL for file you want to download \n")
r = requests.get(url, allow_redirects=True)
open("new.png",'wb').write(r.content)