from xml.dom.minidom import DOMImplementation
import requests
import sys 
from tqdm import tqdm


def interface():
    print("[*] Initializing BruteBat.... ")
    print("please wait while proccessing.")
    print("starting session.")
    print("=================================")
    return 

def main():
    sub_list = open("/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-20000.txt").read()
    subdomains = sub_list.splitlines()

    interface()

    for domain in tqdm(subdomains): 
        try:
            requests.get(f"http://{domain}.{sys.argv[1]}")
        except requests.ConnectionError:
            pass 
        else:
            print(f"[Valid Domain]:{domain}.{sys.argv[1]}")
    

        print("=================================")



if __name__ == '__main__':
    main()