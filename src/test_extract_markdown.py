import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links




class TestInlineMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_markdown_images(self):
        node = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual([("rick roll","https://i.imgur.com/aKaOqIh.gif"),("obi wan","https://i.imgur.com/fJRm4Vk.jpeg")], node)

    def test_markdown_links(self):
        node = extract_markdown_links("This is text with a link [boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual([("boot dev","https://www.boot.dev"),("to youtube","https://www.youtube.com/@bootdotdev")], node)

    def test_markdown_links_error(self):
        with self.assertRaises(Exception):
           extract_markdown_links("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")






