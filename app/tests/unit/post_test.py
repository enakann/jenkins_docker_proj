import unittest
from post import Post
class PostTest(unittest.TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_json(self):
        p = Post('Test', 'Test content')

        self.assertDictEqual({'title': p.title, 'content': p.content}, p.json())


if __name__ == '__main__':
    unittest.main()