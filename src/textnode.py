from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD= "bold"
    ITALIC= "italic"
    CODE= "code"
    LINK= "link"
    IMAGE= "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
       if not isinstance(other, TextNode):
            return NotImplemented

       return (
                self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(node):
    match node.text_type:
        case TextType.IMAGE:
            return LeafNode("img", "", {"src" : node.url, "alt" : node.text})
        case TextType.LINK:
            return LeafNode("a", node.text, {"href" : node.url})
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.TEXT:
            return LeafNode(None, node.text)
        case _:
            raise Exception("Unknown TextType")
