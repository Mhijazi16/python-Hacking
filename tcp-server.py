import socket 
import threading 
import pyfiglet

#global variables
address = "0.0.0.0"
port = 5050 


def main():
    #printing banner
    banner = pyfiglet.figlet_format(f"HyperKrash \n Server \n")
    print(banner)

    #creating server
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    server.bind((address,port))
    #server start listening 
    server.listen(5)
    print(f"[*] Listening on {address} and port {port}")

    while True: 
        #accepting clients
        client,cli_addr = server.accept()
        print(f"Accepted connection from {cli_addr[0]}:{cli_addr[1]}")
        #managing client to threads
        cli_thread = threading.Thread(target=cli_handling,args=((client,)))
        cli_thread.start()
        #printing the number of threads
        print(f"[New Thread Just Started]")
        print(f"Thread Number {threading.active_count()}")
    

def cli_handling(client_sock):
    while True:
        #recieving message from client
        response = client_sock.recv(1024).decode()
        print(f"[*] recived: {response}")
        #checking if want to exit
        if response == "bye":
            print("[*] shuting down Thread...")
            client_sock.close()
            break



if __name__ == '__main__':
    main()
