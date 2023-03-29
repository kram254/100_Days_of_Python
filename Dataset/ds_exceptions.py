import socket
import json


class DSPConnectionError(Exception):
    """
    Raised when there is a connection error with the DSP server.
    """


class DSProtocolError(Exception):
    """
    Raised when there is an error in the DS protocol.
    """


class DSRecipientError(Exception):
    """
    Raised when the recipient is not valid.
    """


def ds_protocol(message, recipient):
    """
    This function implements the DS Protocol. Given a message and a recipient, it will connect to the DSP server,
    send the message to the recipient, and receive any response from the recipient.

    Args:
        message (str): The message to be sent.
        recipient (str): The username of the recipient.

    Returns:
        str: The response from the recipient.

    Raises:
        DSPConnectionError: If there is a connection error with the DSP server.
        DSProtocolError: If there is an error in the DS protocol.
        DSRecipientError: If the recipient is not valid.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 65432))

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

        response = data.decode('utf-8')

        if response == 'INVALID_RECIPIENT':
            raise DSRecipientError('Invalid recipient')

        return response

    except ConnectionError:
        raise DSPConnectionError('Connection error with the DSP server')

    except json.JSONDecodeError:
        raise DSProtocolError('Error in the DS protocol')
