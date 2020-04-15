import socket
from socket import AF_INET, SOCK_STREAM
from subprocess import Popen, PIPE, STDOUT

def receive_and_send_success(connectionSocket):
    try:
        command = connectionSocket.recv(2048)
        command = command.decode()

        popen = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = popen.stdout.read()
        output = output.decode()
        popen.wait()

        # Store data in local file
        if command[-1] == '>' or '>' not in command:
            if command[-1] == '>':
                command = command[:-1]
            filename = command.split()[0] + '_cmd.txt'
        else:
            filename = command.split('>')[-1].strip(' ')
        
        with open(filename, 'w') as f:
            f.write(output)

        # Send data back to the client
        with open(filename, 'rb') as f:
            message = f.read()
            connectionSocket.send(message)
    except:
        return False
    return True


def main():
    serverPort = 12345
    serverSocket = socket.socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(2)
    while True:
        connectionSocket, address = serverSocket.accept()
        print(connectionSocket)
        if receive_and_send_success(connectionSocket):
            print('Successful file transmission.')
        connectionSocket.close()



if __name__ == '__main__':
    main()