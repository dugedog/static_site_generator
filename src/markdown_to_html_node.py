from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            tag = "p"
        elif block_type == BlockType.ULIST:
            tag = "ul"
        else:
            tag = None
        print(tag)
        new_html_nodes.append(HTMLNode(tag, block))
    print(new_html_nodes)

        
    return new_html_nodes
