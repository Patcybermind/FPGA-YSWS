def convert_md_tags(line):
    
    # Convert headers (e.g., ## Header -> <h2>Header</h2> up to h6)
    line = re.sub(r'^(#{1,6})\s*(.+)$', lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", line)
    
    # Convert bold (e.g., **bold** or __bold__ -> <strong>bold</strong>)
    line = re.sub(r'(\*\*|__)(.*?)\1', r'<strong>\2</strong>', line)
    
    # Convert italic (e.g., *italic* or _italic_ -> <em>italic</em>)
    line = re.sub(r'(\*|_)(.*?)\1', r'<em>\2></em>', line)
    # Convert line to paragraph if it doesn't contain header tags
    if not re.match(r'^<h[1-6]>', line):
        if line != "":
            line = f"<p>{line}</p>"
        else:
            line = "<br>"

    return line
    
def convert_to_html(file):
    with open("html_boilerplate.html", "r") as f:
        boilerplate = f.read()
    with open(f"pub/{file}", "r") as f:
        content = f.read()
        content_list = content.splitlines()
        new_content = boilerplate + "\n"
        for line in content_list:
            new_content += convert_md_tags(line) + "\n"


    with open(f"pub/{file.replace('.md', '.html')}", "w") as f:
        f.write(new_content)


def generate_html():

    list_of_files = [file for file in os.listdir("pub") if file.endswith(".md") and file != "README.md"]
    print("\n", list_of_files) 
    for file in list_of_files:
        convert_to_html(file)