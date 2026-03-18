from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextType, TextNode

def _helper_blocktext_to_children(plain_text):
    children_nodes = []
    text_nodes = text_to_textnodes(plain_text)
    for node in text_nodes:
        children_nodes.append(text_node_to_html_node(node))
    return children_nodes

def _helper_quote(block):
    cleaned_block_list = []
    split_block = block.split("\n")
    for split in split_block:
        cleaned_block_list.append(split.lstrip('>').lstrip(' '))
    cleaned_block = " ".join(cleaned_block_list)
    return ParentNode("blockquote", _helper_blocktext_to_children(cleaned_block))

def _helper_heading(block):
    header_level = block.split(" ",1)[0].count("#")
    cleaned_header = block.lstrip("#").strip()
    children_nodes = []
    header_text_nodes = text_to_textnodes(cleaned_header)
    for node in header_text_nodes:
        children_nodes.append(text_node_to_html_node(node))
    return ParentNode(f"h{header_level}", children_nodes)

def _helper_olist(block):
    dot_points = block.split("\n") 
    text_nodes = []
    children = []
    for dot_point in dot_points:
       dot_point = f"<li>{dot_point[3:]}</li>"
       text_nodes.extend(text_to_textnodes(dot_point))
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    parent = ParentNode("ol",children) 
    return parent

def _helper_ulist(block):
    dot_points = block.split("\n") 
    text_nodes = []
    children = []
    for dot_point in dot_points:
       dot_point = f"<li>{dot_point[2:]}</li>"
       text_nodes.extend(text_to_textnodes(dot_point))
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    parent = ParentNode("ul",children) 
    return parent 

def _helper_paragraph(block):
    block = block.replace("\n"," ")
    children_list = []
    text_nodes = text_to_textnodes(block)
    for text_node in text_nodes:
        children_list.append(text_node_to_html_node(text_node))
    return ParentNode("p", children_list) 

def _helper_code(block):
    split_blocks = block.strip("```").strip().split("\n")
    cleaned_blocks = []
    for split_block in split_blocks:
        cleaned_blocks.append(split_block.strip())
    joined_cleaned_block = "\n".join(cleaned_blocks)
    child_node = LeafNode("code", joined_cleaned_block)
    parent_node = ParentNode("pre", [child_node])
    return parent_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    page_list = []

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                page_list.append(_helper_paragraph(block))
            case BlockType.CODE:
                page_list.append(_helper_code(block))
            case BlockType.ULIST:
                page_list.append(_helper_ulist(block))
            case BlockType.OLIST:
                page_list.append(_helper_olist(block))
            case BlockType.HEADING:
                page_list.append(_helper_heading(block))
            case BlockType.QUOTE:
                page_list.append(_helper_quote(block))

    html_page = ParentNode("div",page_list)            
    return html_page 
