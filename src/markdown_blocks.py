from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    def test_quote_block(block):
        symbol_count = 0
        block_as_lines = block.split("\n")
        for line in block_as_lines:
            if line[0] == ">" and len(line)>1:
                symbol_count += 1
        if symbol_count == len(block_as_lines):
            return True
        else:
            return False
    
    def test_ulist_block(block):
        symbol_count = 0
        block_as_lines = block.split("\n")
        for line in block_as_lines:
            if line.startswith("- "):
                symbol_count += 1
        if symbol_count == len(block_as_lines):
            return True
        else:
            return False 

    def test_olist_block(block):
        block_as_lines = block.split("\n")
        for i in range(len(block_as_lines)):
            if block_as_lines[i].startswith(f"{i+1}."):
                continue 
            else:
                return False 
        return True

    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return BlockType.HEADING
    if block[0:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE
    if test_quote_block(block) == True:
        return BlockType.QUOTE
    if test_ulist_block(block) == True:
        return BlockType.ULIST
    if test_olist_block(block) == True:
        return BlockType.OLIST
    return BlockType.PARAGRAPH
