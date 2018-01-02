import socket
from time import sleep

host = 'localhost'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
while True:
    print('\nListening for a client at', host ,port)
    conn, addr = s.accept()
    print('\nConnected by', addr)
    try:
        print('\nSending data...\n')
        for i in range(10):
            print('Sending data')
            conn.send(b'hello world')
            sleep(10)
        print('End Of Stream.')
    except socket.error:
        print ('Error Occured.\n\nClient disconnected.\n')
conn.close()