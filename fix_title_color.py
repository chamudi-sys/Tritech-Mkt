import glob

for file in glob.glob('*.html'):
    if file in ('index.html', 'index_backup.html'):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if 'color: #d97706;' in content:
        content = content.replace('color: #d97706;', 'color: #0f172a;')
        changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated title color to slate black in {file}")

print("Title color update completed.")
