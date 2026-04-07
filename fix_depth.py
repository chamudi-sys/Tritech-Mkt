import glob

for file in glob.glob('*.html'):
    if file in ('index.html', 'index_backup.html'):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if 'background-color: #FAFAFA;' in content:
        content = content.replace('background-color: #FAFAFA;', 'background-color: #f1f5f9;')
        changed = True
        
    if '#FAFAFA !important' in content:
        content = content.replace('#FAFAFA !important', '#f1f5f9 !important')
        changed = True

    if 'box-shadow: 0 10px 30px rgba(0,0,0,0.03);' in content:
        content = content.replace('box-shadow: 0 10px 30px rgba(0,0,0,0.03);', 'box-shadow: 0 15px 35px rgba(0,0,0,0.08);')
        changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added depth to {file}")

print("Added depth and proper contrast to detail pages.")
