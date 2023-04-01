import socket
import json

HOST = '127.0.0.1'
PORT = 65432        


def ds_protocol(message, recipient):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Create the message packet
        packet = {
            'type': 'message',
            'message': message,
            'recipient': recipient
        }

        # Send the packet to the DSP server
        s.sendall(json.dumps(packet).encode('utf-8'))

        # Receive the response from the recipient
        data = s.recv(1024)

    return data.decode('utf-8')
