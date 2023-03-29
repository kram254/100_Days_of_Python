import unittest
from unittest.mock import patch
from ds_messenger import DS_Messenger, Message


class TestDSMessenger(unittest.TestCase):
    def setUp(self):
        self.messenger = DS_Messenger("user1")

    def test_add_friend(self):
        self.messenger.add_friend("user2")
        self.assertIn("user2", self.messenger.get_friends())

    def test_remove_friend(self):
        self.messenger.add_friend("user2")
        self.messenger.remove_friend("user2")
        self.assertNotIn("user2", self.messenger.get_friends())

    def test_send_message_success(self):
        with patch("ds_protocol.ds_protocol") as mock_ds_protocol:
            mock_ds_protocol.return_value = "success"
            message = Message("test message", "user2")
            result = self.messenger.send_message(message)
            self.assertEqual(result, "success")

    def test_send_message_failure(self):
        with patch("ds_protocol.ds_protocol") as mock_ds_protocol:
            mock_ds_protocol.return_value = "failure"
            message = Message("test message", "user2")
            result = self.messenger.send_message(message)
            self.assertEqual(result, "failure")

    def test_send_message_raises_exception(self):
        with patch("ds_protocol.ds_protocol") as mock_ds_protocol:
            mock_ds_protocol.side_effect = Exception("Test Exception")
            message = Message("test message", "user2")
            with self.assertRaises(Exception):
                self.messenger.send_message(message)


if __name__ == '__main__':
    unittest.main()
