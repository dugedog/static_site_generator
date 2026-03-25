import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
       md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
       node = markdown_to_html_node(md) 
       html = node.to_html()
       self.assertEqual(
       html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_tolkein_quote(self):
        md = """
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>I am in fact a Hobbit in all but size. -- J.R.R. Tolkien</blockquote></div>"
        )

 

    def test_unordered_list(self):
        md = """
- Item one
- Item two
- Item three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>",
    )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_heading1(self):
        md = """
## This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h2>This is a heading</h2></div>",
        )


    def test_heading2(self):
        md = """
# This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>",
        )


    def test_heading3(self):
        md = """
###### This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h6>This is a heading</h6></div>",
        )
    def test_heading_with_inline(self):
        md = """
# This is **bold** and _italic_ text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
        html,
        "<div><h1>This is <b>bold</b> and <i>italic</i> text</h1></div>",
    )

    def test_blockquote_1(self):
        md = """
> This is a quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
        html,
        "<div><blockquote>This is a quote</blockquote></div>",
    )

    def test_blockquote_with_inline(self):
        md = """
> This is **bold**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bold</b></blockquote></div>",
        )

    def test_blockquote_multiline(self):
        md = """
> First line
> Second line
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>First line Second line</blockquote></div>",
        )

    def test_blockquote_single_word(self):
        md = """
> Hello
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>Hello</blockquote></div>",
        )
    def test_blockquote_trailing_space(self):
        md = """
> Hello   
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>Hello</blockquote></div>",
        )

    def test_blockquote_extra_space(self):
        md = """
>   Spaced quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>Spaced quote</blockquote></div>",
        )
    def test_paragraph_and_blockquote(self):
        md = """
This is a paragraph

> This is a quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is a paragraph</p><blockquote>This is a quote</blockquote></div>",
        )

    def test_multiple_blocks(self):
        md = """
This is a paragraph

> This is a quote

This is another paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is a paragraph</p><blockquote>This is a quote</blockquote><p>This is another paragraph</p></div>",
        )

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()

