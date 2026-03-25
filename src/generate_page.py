from markdown_to_html_node import markdown_to_html_node

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

def update_template(template, html_string, page_title):
    html_list = []
    for html in template.split("\n"):
        if html=="    <title>{{ Title }}</title>":
            html_list.append(f"    <title>{page_title}</title>")
        elif html == "    <article>{{ Content }}</article>":
            html_list.append(f"    <article>{html_string}</article>")
        else:
            html_list.append(f"{html}") 
    html_content = "\n".join(html_list) 
    return html_content

def generate_page(from_path, template_path, dest_path):
    print(f"Generating pagk from {from_path} to {dest_path} using {template_path}\n")

    markdown = read_from_file(from_path)
    template = read_from_template(template_path)
    html_string = markdown_to_html_node(markdown).to_html()
    page_title = extract_title((markdown))
    full_html_page = update_template(template, html_string, page_title)
    write_html_file(dest_path, full_html_page)

    return "Website Generation Complete" 
