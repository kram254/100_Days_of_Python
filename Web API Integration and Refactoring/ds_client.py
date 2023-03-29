# ds_client.py

# Replace the following placeholders with your information.

# Carrie Liu
# carrihl1@uci.edu
# 64814057

import socket
import ds_protocol


def send(server, port, username, password, message):
    """Send a message to the specified server on the specified port."""
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    client_socket.connect((server, port))
    # create the message to send
    request = f"PUBLISH\n{username}\n{password}\n{message}\n"
    # send the message
    client_socket.send(request.encode())
    # receive the response
    response = client_socket.recv(1024).decode()
    # close the socket
    client_socket.close()
    # return the response
    return response.strip()


def send(server, port, username, password, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        credentials = ds_protocol.encode_credentials(username, password)
        s.sendall(credentials)
        response = s.recv(1024)
        if not ds_protocol.decode_response(response):
            raise Exception("Invalid username/password")
        post_data = ds_protocol.encode_post_data(username, message)
        s.sendall(post_data)
        response = s.recv(1024)
        if not ds_protocol.decode_reponse(response):
            raise Exception("Failed to post message to server")
