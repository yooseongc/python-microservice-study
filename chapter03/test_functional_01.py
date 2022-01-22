import unittest
import json
import sys
sys.path.append("./chapter02")
from flask_basic import app as _app


class TestApp(unittest.TestCase):
    
    def test_help(self):
        app = _app.test_client()
        hello = app.get("/api")
        body = json.loads(str(hello.data, "utf8"))
        self.assertEqual(body["Hello"], "World!")


if __name__ == "__main__":
    unittest.main()
