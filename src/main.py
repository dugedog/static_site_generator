from copy_static import copy_static
from generate_page import generate_page_recursively
from os import path, getcwd, listdir
from config import *
import sys

def main():
    basepath = "/" if len(sys.argv) == 1 else sys.argv[1]
    from_path = path.join(getcwd(),INITIAL_CONTENT_DIRECTORY)
    file_list = listdir(from_path)
    template_path = path.join(getcwd(), "template.html")
    dest_path = path.join(getcwd(), PUBLIC_DIRECTORY) 
    generate_page_recursively(file_list, template_path, from_path, dest_path, basepath)
main()    
