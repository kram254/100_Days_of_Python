import socket
import threading
import json
import os

from NaClProfile import NaClProfile

# Constants
HOST = 'localhost'
PORT = 8888
BUFFER_SIZE = 1024
DATA_DIR = './data'
USERS_FILE = f'{DATA_DIR}/users.json'

# Data storage
USERS = {}
POSTS = []

# Load existing users from file
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'r') as f:
        USERS = json.load(f)

# NaClProfile object for public key encryption
np = NaClProfile()

def handle_client(conn, addr):
    """
    Thread to handle individual client connections.
    """
    print(f'New connection from {addr}')

    # Client public key is sent during the join process
    client_public_key = None

    while True:
        try:
            data = conn.recv(BUFFER_SIZE).decode()
            if not data:
                break

            # Parse incoming message
            try:
                msg = json.loads(data)
            except json.JSONDecodeError:
                print(f'Invalid JSON from {addr}: {data}')
                continue

            if 'join' in msg:
                # Handle join request
                username = msg['join']['username']
                password = msg['join']['password']
                client_public_key = msg['join']['token']

                if username not in USERS:
                    USERS[username] = {'password': password, 'public_key': client_public_key}
                    response = {'type': 'ok', 'message': f'Welcome {username}!'}
                    print(f'New user joined: {username}')
                elif USERS[username]['password'] == password:
                    USERS[username]['public_key'] = client_public_key
                    response = {'type': 'ok', 'message': f'Welcome back {username}!'}
                    print(f'Existing user joined: {username}')
                else:
                    response = {'type': 'error', 'message': 'Incorrect password'}
            elif 'post' in msg:
                # Handle post request
                username = msg['post']['username']
                password = msg['post']['password']
                post_text = msg['post']['text']

                if username not in USERS or USERS[username]['password'] != password:
                    response = {'type': 'error', 'message': 'Invalid username or password'}
                else:
                    # Encrypt post using client's public key
                    if client_public_key is None:
                        response = {'type': 'error', 'message': 'Client public key not found'}
                    else:
                        post_entry = np.encrypt_entry(post_text, client_public_key)
                        POSTS.append({'username': username, 'entry': post_entry})
                        response = {'type': 'ok', 'message': 'Post added successfully'}

            else:
                response = {'type': 'error', 'message': 'Invalid message type'}

            # Send response
            conn.sendall(json.dumps(response).encode())

        except ConnectionResetError:
            break

    print(f'Connection closed from {addr}')
    conn.close()

def start_server():
    """
    Start the main server loop.
    """
    print(f'Server started on {HOST}:{PORT}')

    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Start server loop
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

    # Save user data to file on exit
    def exit_handler():
        print("Saving user data...")
        with open(USER_DATA_FILE, 'wb') as f:
            pickle.dump(users, f)

    atexit.register(exit_handler)

if __name__ == '__main__':
    start_server()

