import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    current_text = ""
    for node in old_nodes:
        extracts = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(extracts) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for extract in extracts:
            link_text = extract[0]
            link_url = extract[1]
            delimiter = f"[{link_text}]({link_url})"
            split_text = current_text.split(delimiter,1)
            new_text_node = split_text[0]
            current_text = split_text[1]
            if len(new_text_node) > 0:
                new_nodes.append(TextNode(new_text_node, TextType.TEXT))
            new_nodes.append(TextNode(link_text,TextType.LINK,link_url))
    if len(current_text) > 0:
        new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

 
def split_nodes_image(old_nodes):
    new_nodes = []
    current_text = ""
    for node in old_nodes:
        extracts = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(extracts) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for extract in extracts:
            link_text = extract[0]
            link_url = extract[1]
            delimiter = f"![{link_text}]({link_url})"
            split_text = current_text.split(delimiter,1)
            new_text_node = split_text[0]
            current_text = split_text[1]
            if len(new_text_node) > 0:
                new_nodes.append(TextNode(new_text_node, TextType.TEXT))
            new_nodes.append(TextNode(link_text,TextType.IMAGE,link_url))
    if len(current_text) > 0:
        new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    current_textnode = TextNode(text,TextType.TEXT)
    current_textnode = split_nodes_delimiter([current_textnode],"_",TextType.ITALIC)
    current_textnode = split_nodes_delimiter(current_textnode,"**",TextType.BOLD)
    current_textnode = split_nodes_delimiter(current_textnode,"`",TextType.CODE)
    current_textnode = split_nodes_image(current_textnode) 
    current_textnode = split_nodes_link (current_textnode)
    return current_textnode


