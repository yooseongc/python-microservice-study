import unittest
import json
import sys
sys.path.append("./chapter02")
from flask_basic import app as _app


_404 = "The requested URL was not found on the server. "\
    "If you entered the URL manually please check your "\
    "spelling and try again."


class TestApp(unittest.TestCase):
    
    def setUp(self) -> None:
        from flask_error import app as _app
        self.app = _app.test_client()
    
    def test_raise(self):
        hello = self.app.get("/api")
        body = json.loads(str(hello.data, "utf8"))
        self.assertEqual(body["code"], 500)

    def test_proper_404(self):
        hello = self.app.get("/dwdwqqwdwqd")
        self.assertEqual(hello.status_code, 404)
        body = json.loads(str(hello.data, "utf8"))
        self.assertEqual(body["code"], 404)
        self.assertEqual(body["message"], "404 Not Found")
        self.assertEqual(body["description"], _404)


if __name__ == "__main__":
    unittest.main()
