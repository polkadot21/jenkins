import unittest
from model import model

#class TestHello(unittest.TestCase):

 #   def setUp(self):
  #      app.app.testing = True
   #     self.app = app.app.test_client()

   # def test_hello(self):
    #    rv = self.app.get('/test')
     #   self.assertEqual(rv.status, '200 OK')
      #  self.assertEqual(rv.data, b'Hello, world!\n')

class TestRSquared(unittest.TestCase):

    def setUp(self):
        model.testing = True
        self.model = model

    def testrsquared(self):
        """checks if the R-squared is larger than 90%"""
        rsquared = self.model.rsquared
        self.assertTrue(rsquared > 0.9)


if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
