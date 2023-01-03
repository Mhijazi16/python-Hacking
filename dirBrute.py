import requests
import sys 
from tqdm import tqdm

def interface():
    print("[*]staring DirBrute please wait...")
    print("[*]sesion started.")
    print("===================================")

def main():
    interface() 
    
    dir_list = open("wordlist2.txt").read()
    dirs = dir_list.splitlines()

    for dir in tqdm(dirs): 
        url = f"http://{sys.argv[1]}/{dir}.html" 
        r = requests.get(url)
        if r.status_code != 404:
            print(f"[Valid Directory]: {sys.argv[1]}/{dir}")
    print("===================================")


if __name__ == '__main__': 
    main()