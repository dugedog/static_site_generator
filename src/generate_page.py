from markdown_to_html_node import markdown_to_html_node
from os import mkdir, path, getcwd, listdir

def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.startswith("# "):
            block = block.strip("#")
            block = block.strip()
            return block
    raise Exception("Header not found in markdown")

def read_from_file (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return (file_contents)

def read_from_template (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return (file_contents)

def write_html_file(file_path, contents):
    with open(file_path,'w',encoding="utf-8") as f:
        f.write(contents)

def update_template(template, html_string, page_title, basepath):
    html_list = []
    for html in template.split("\n"):
        if html=="    <title>{{ Title }}</title>":
            html_list.append(f"    <title>{page_title}</title>")
        elif html == "    <article>{{ Content }}</article>":
            html_list.append(f"    <article>{html_string}</article>")
        else:
            html_list.append(f"{html}") 
    html_content = "\n".join(html_list) 
    html_content = html_content.replace('href="/',f'href="{basepath}')
    html_content = html_content.replace('src="/',f'src="{basepath}')
    return html_content

def generate_page_recursively(file_list, template_path, from_path, dest_path, basepath):
    
    for file in file_list:    
        from_object = path.join(from_path, file)
        to_object = path.join(dest_path, file) 
        if path.isfile(from_object):
            markdown = read_from_file(from_object)
            template = read_from_template(template_path)
            html_string = markdown_to_html_node(markdown).to_html()
            page_title = extract_title((markdown))
            full_html_page = update_template(template, html_string, page_title, basepath)
            write_html_file(to_object[:-2]+"html", full_html_page)
        else:
            new_file_list = listdir(from_object)
            if len(new_file_list) > 0:
                if not path.exists(to_object):
                    mkdir(to_object)
                generate_page_recursively(new_file_list, template_path, from_object, to_object, basepath)

    return "Website Generation Complete" 
