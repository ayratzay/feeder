import socket
from _thread import start_new_thread
from random import choice, randrange
from time import sleep


def generate_data():
    gender = choice(['male', 'female'])
    value1 = randrange(1, 10)
    value2 = randrange(18, 60)
    value3 = randrange(150, 180)
    data = (gender, value1, value2, value3)
    return data


host = '0.0.0.0'
post = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((host, post))
except socket.error as e:
    print(str(e))


s.listen(5)
print('waiting for connection')

def threaded_client(conn):
    conn.send(str.encode('Connected to server!\n'))
    while True:
        sleep(1)
        reply = 'New data: {output}\n'.format(output=generate_data())
        conn.sendall(str.encode(reply))
    conn.close()


while True:
    conn, addr = s.accept()
    print('connected to: {adr1} : {adr2}'.format(adr1=addr[0], adr2=addr[1]))
    start_new_thread(threaded_client, (conn,))