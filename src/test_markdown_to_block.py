import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_block_to_block_type_heading(self):
        block = "#### Heading"
        test = block_to_block_type(block)
        self.assertEqual(test, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\n code ```"
        test = block_to_block_type(block)
        self.assertEqual(test, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> Start\n> Hello bob\n> Hello bob\n> End"
        test = block_to_block_type(block)
        self.assertEqual(test, BlockType.QUOTE)

    def test_block_to_block_type_quote_fail(self):
        block = "> Hello bob\n> Hello bob\n< Hello bob\n> Hello bob"
        test = block_to_block_type(block)
        self.assertEqual(test, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()

