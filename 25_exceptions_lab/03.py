"""
Write code to make the following unit test pass
"""

import unittest
import re
import sys

class InvalidImageExt(Exception):

    def __init__(self, file):
        super(InvalidImageExt, self).__init__("File '{}' has an invalid image extension".format(file))


class ImageFile(object):

    def __init__(self, file):
        if not re.search(r'[.]gif|png|jpg|jpeg$', file):
            raise InvalidImageExt(file)
        self._file = file


class TestImageFile(unittest.TestCase):

    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()