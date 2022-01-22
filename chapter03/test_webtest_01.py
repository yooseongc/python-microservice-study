import unittest
import sys
sys.path.append("./chapter02")
from flask_basic import app as _app


class TestMyApp(unittest.TestCase):
    
    def setUp(self) -> None:
        from webtest import TestApp
        self.app = TestApp(_app)
        
    def test_help(self):
        hello = self.app.get("/api")
        self.assertEqual(hello.json["Hello"], "World!")
        

if __name__ == "__main__":
    unittest.main()
