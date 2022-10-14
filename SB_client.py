import socket       
import sys

host = "127.0.0.1"
port = 5001


try:
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((host, port))       
except Exception as err:
    print(err)
    sys.exit()
print("Connection established with success...")

print("\nSTRIKE & BALL")
word=input("\nInsert the word that server will have to guess-> ")
word1=str(len(word))
my_sock.send(word1.encode())
if word=="break":
    pass
else:
    while 1:
        guess = my_sock.recv(256)
        print(f"The word sent from server is-> {guess.decode()}")
        if guess.decode() == word:
            print("Server guessed the word!")
            my_sock.send("break".encode())
            break
        
        strike = input("\nHow many Strike do you want to send?-> ")
        ball = input("How many Ball do you want to send?")     
        my_sock.send(f"Number of Strike: {strike}\nNumber of Ball: {ball}".encode())
        
        
        
        
my_sock.close()