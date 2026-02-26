import re

def extract_markdown_images(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    if not matches:
        raise Exception("No matches found")
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    if not matches:
        raise Exception("No matches found")
    return matches
