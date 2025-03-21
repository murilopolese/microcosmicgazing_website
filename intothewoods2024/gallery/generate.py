import os

def create_gallery(directory):
    # Create the HTML file structure for the gallery
    html = """<!DOCTYPE html>
               <html lang="en">
                 <head>
                   <meta charset="UTF-8" />
                   <title>Gallery</title>
                   <link rel="stylesheet" href="main.css">
                 </head>
                 <body>
                   <h1>Gallery</h1>
                   <div class="gallery">"""
    menu = """<ol class="menu">"""
    # Loop through all files in the directory and add them to the gallery
    for root, dirs, files in os.walk(directory):
        dirs.sort()
        files.sort()
        # print('-------')
        # print("root", root)
        # print("dirs", dirs)
        # print("files", files)
        section = root.split('_')[-1]
        if section != '.':
            html += f"""<h2 id="{section}">{section}</h2>"""
            menu += f"""<li><a href="#{section}">{section}</a></li>"""
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath):
                if '.jpg' in filepath or '.jpeg' in filepath or '.png' in filepath:
                    html += f"""<a href="{filepath}" target="_blank">
                        <img src="{filepath}" alt="{filename}" loading="lazy"/>
                    </a>"""
                if '.mp4' in filepath:
                    html += f"""<video controls alt="{filename}">
                        <source src="{filepath}" type="video/mp4">
                    </video>"""

    menu += """</ol>"""
    # Close the gallery div and end the HTML file
    html += f"""</div>
                {menu}
               </body>
             </html>"""

    # Write the HTML to a file
    with open("index.html", "w") as f:
        f.write(html)

# Example usage: create a gallery from the current directory and all subdirectories
create_gallery(".")
