from copy_static import copy_static
from generate_page import generate_page
from os import path, getcwd, listdir
from config import *

def main():
    file_list = listdir(path.join(getcwd(),INITIAL_CONTENT_DIRECTORY))
    print(file_list)
    template_path = path.join(getcwd(), "template.html")
    print (template_path)
    dest_path = path.join(getcwd(), PUBLIC_DIRECTORY) 
#   copy_static()
#   generate_page(from_path, template_path, dest_path)
main()    
