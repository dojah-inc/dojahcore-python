import unittest


class CoreTestCase(unittest.TestCase):
    def endpoint_url(self, path):
        if path[0] == '/':
            return 'https://sandbox.dojah.io{}'.format(path)
        return 'https://sandbox.dojah.io/{}'.format(path)