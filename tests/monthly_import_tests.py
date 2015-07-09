import unittest
import os
import sys

sys.path.append(os.path.abspath('../bls_reader'))

from bls_report_classes import *
from bls_reader import *
from bls_api import *


class TestBlsReader(unittest.TestCase):
	""" Test the reading of the BLS monthly Employment Situation Report """

	def testFeb2015(self):
		answer = bls_reader(2, 2015)
		self.assertEqual(answer, 266000)




if __name__ == "__main__":
	unittest.main()