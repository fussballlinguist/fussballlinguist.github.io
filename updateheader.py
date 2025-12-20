import os

# Pfad zum Projektordner
project_dir = "."  # aktueller Ordner
header_file = os.path.join(project_dir, "header.html")

# HTML-Dateien finden
html_files = []
for root, dirs, files in os.walk(project_dir):
    for f in files:
        if f.endswith(".html") and f != "header.html":
            html_files.append(os.path.join(root, f))

# Header-Inhalt lesen
with open(header_file, "r", encoding="utf-8") as f:
    header_content = f.read()

# Platzhalter für Header in HTML-Dateien
placeholder = "<!-- HEADER_PLACEHOLDER -->"

# Header einfügen
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if placeholder in content:
        new_content = content.replace(placeholder, header_content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Header aktualisiert in: {file_path}")
    else:
        print(f"Kein Placeholder in: {file_path}")
