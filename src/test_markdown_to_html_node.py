import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        html = markdown_to_html_node(md) 
#       self.assertEqual(
#           html,
#           [
#               "This is **bolded** paragraph",
#               "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#               "- This is a list\n- with items",
#           ],
#       )

if __name__ == "__main__":
    unittest.main()

