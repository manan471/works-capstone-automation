import unittest

from test_clientjourney import WorksApp as A
from test_lead_section import WorksApp as B

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(B))
suite.addTest(loader.loadTestsFromTestCase(A))
