import unittest
import os
import sys
sys.path.append("./chapter02")


class TestMyApp(unittest.TestCase):
    
    def setUp(self) -> None:
        http_app = os.environ.get("HTTP_SERVER")
        if http_app is not None:
            from webtest import TestApp
            self.app = TestApp(http_app)
        else:
            from flask_basic import app
            from flask_webtest import TestApp
            self.app = TestApp(app)
        
    def test_help(self):
        hello = self.app.get("/api")
        self.assertEqual(hello.json["Hello"], "World!")
        

if __name__ == "__main__":
    unittest.main()
