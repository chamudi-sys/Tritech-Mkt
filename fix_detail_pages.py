import glob
import re

for file in glob.glob('*.html'):
    if file in ('index.html', 'index_backup.html'):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Backgrounds & Core Colors
    replacements = {
        r'background-color:\s*#121212;': 'background-color: #FAFAFA;',
        r'background-color:\s*#1e1e1e;': 'background-color: #ffffff;\n      border: 1px solid rgba(0,0,0,0.05);',
        r'color:\s*#fff;': 'color: #0f172a;',
        r'color:\s*#ccc;': 'color: #475569;',
        r'color:\s*#bbb;': 'color: #64748b;',
        r'color:\s*#FFD700;': 'color: #d97706;',  # Bright gold/orange for titles instead of yellow
        r'box-shadow:\s*0\s+8px\s+20px\s+rgba\(0,0,0,0\.3\);': 'box-shadow: 0 10px 30px rgba(0,0,0,0.03);',
        r'box-shadow:\s*0\s+12px\s+30px\s+rgba\(0,0,0,0\.4\);': 'box-shadow: 0 20px 40px rgba(0,0,0,0.08);',
        r'background:\s*rgba\(255,255,255,0\.05\);': 'background: #ffffff;\n        box-shadow: 0 4px 15px rgba(0,0,0,0.02);',
    }

    for pattern, new_val in replacements.items():
        if re.search(pattern, content):
            content = re.sub(pattern, new_val, content)
            changed = True

    # 2. To ensure bodies are light if they didn't have the exact #121212
    if '<body class="sub_page">' not in content and '<body>' in content:
         # Apply a light class or just rely on the CSS
         if 'background-color: #121212;' not in content and 'background: #111;' in content:
             content = content.replace('background: #111;', 'background: #FAFAFA;')
             changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated theme for {file}")

print("Detail pages upgraded to Light Theme.")
