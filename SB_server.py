import socket       
import sys

host = "127.0.0.1"  
port = 5001

try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.bind((host, port))          
    my_sock.listen(1)                   
except Exception as err:
    print(err)
    sys.exit()

print("Server listening...")
conn, addr = my_sock.accept()
print ('Connection incoming from... ', addr)

word = conn.recv(256)
if word == "break":
    pass
else:
    print(f"\nThe number of letters of the word to guess is-> {word.decode()}")
    guess=input(f"Try to guess the word of {word.decode()} letters-> ")
    conn.send(guess.encode())
    while 1:
        word1 = conn.recv(256)
        if word1.decode() == "break":
            break
        else:
            print(word1.decode())
            guess = input(f"Try to guess the word of {word.decode()} letters-> ")
            conn.send(guess.encode())

    
conn.close()
my_sock.close()