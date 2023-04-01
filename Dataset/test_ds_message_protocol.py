import unittest
from unittest.mock import patch
from ds_messenger import Profile, Message, ds_protocol
from ds_exceptions import ConnectionError, DSProtocolError


class TestDSMessenger(unittest.TestCase):
    def setUp(self):
        self.user1 = Profile('Mark')
        self.user2 = Profile('Karios')

    def test_add_friend(self):
        self.user1.add_friend('Karios')
        self.assertIn('Karios', self.user1.get_friends())

    def test_remove_friend(self):
        self.user1.add_friend('Karios')
        self.user1.remove_friend('Karios')
        self.assertNotIn('Karios', self.user1.get_friends())

    def test_send_message(self):
        with patch('ds_messenger.ds_protocol') as mock_protocol:
            mock_protocol.return_value = 'OK'
            message = Message('Hello, Karios!', 'Karios')
            self.assertEqual(message.send(), 'OK')

    def test_receive_message(self):
        with patch('ds_messenger.ds_protocol') as mock_protocol:
            mock_protocol.return_value = 'Hello, Mark!'
            message = Message('Hi, Karios!', 'Karios')
            self.assertEqual(message.receive(), 'Hello, Mark!')

    def test_ds_protocol_connection_error(self):
        with patch('socket.socket') as mock_socket:
            mock_socket.return_value.connect.side_effect = ConnectionError
            with self.assertRaises(ConnectionError):
                ds_protocol('Hello, Karios!', 'Karios')

    def test_ds_protocol_protocol_error(self):
        with patch('socket.socket') as mock_socket:
            mock_socket.return_value.recv.return_value = b'{"type": "error", "message": "Invalid recipient"}'
            with self.assertRaises(DSProtocolError):
                ds_protocol('Hello, Karios!', 'Karios')


if __name__ == '__main__':
    unittest.main()
