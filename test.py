import unittest
import server

class Test_server (unittest.TestCase):

    def test_server1(self):
        """
        Testar servern
        """
        result = server.for_test_only()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()