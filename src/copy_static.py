from os import path, getcwd, listdir, mkdir
from shutil import rmtree, copy
from config import SOURCE_DIRECTORY, PUBLIC_DIRECTORY 


def copy_static():

    def list_and_copy(listing, src, dst):
        print(listing)
        for file in listing:
            source_path = path.join(src, file)
            print(f"Actioning {source_path}")
            if path.isfile(source_path):
                print(f"Coping = {file} to {dst}")
                copy(source_path, dst)
                print(f"{file} copied!") 
            else:
                print(f"{file} is a directory")
                new_src = path.join(src, file)
                new_listing = listdir(new_src) 
                if len(new_listing)>0:
                    print(f"Directory contains: {new_listing}")
                    new_dst = path.join(dst, file)
                    print(f"Making new directory {new_dst}")
                    mkdir(new_dst)
                    print("Made new directory")
                    list_and_copy(new_listing, new_src, new_dst)
                else:
                    print("New directory is empty")
                
    
    source = path.join(getcwd(), SOURCE_DIRECTORY)
    destination = path.join(getcwd(), PUBLIC_DIRECTORY)

    if not path.exists(source) or not(path.isdir(source)):
        raise Exception("source directory not found or is not a directory")

    if path.exists(destination):
        print(path.exists(destination))
        rmtree(destination)
        mkdir(destination)
    else:
        mkdir(destination)

    if not path.isdir(destination):
        raise Exception("Destination is not a folder")

    listing = listdir(source) 

    if len(listing) == 0:
        raise Exception (f"Source directory: {source} contains no files or directories")
    else:
        list_and_copy(listing, source, destination)

    return f"# Source content: {source}\n# Destination: {destination}"
        
