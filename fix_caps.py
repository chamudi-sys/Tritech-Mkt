import glob

replacements = {
    'AQUATHERM POLYPROPYLENE PIPE SYSTEMS': 'Aquatherm polypropylene pipe systems',
    'EVERGUSH PUMP SYSTEMS': 'Evergush pump systems',
    'HENG LONG PUMP SYSTEMS': 'Heng Long pump systems',
    'SPERONI WATER PUMPS': 'Speroni water pumps',
    'HDPE (Pnhai) PIPE SYSTEMS': 'HDPE (Puhei) pipe systems', 
    'CALPEDA PUMP SYSTEMS': 'Calpeda pump systems',
    'TSURUMI PUMP TECHNOLOGY': 'Tsurumi pump technology',
    'GRP WATER TANKS & HDPE PIPING SYSTEMS': 'GRP water tanks & HDPE piping systems'
}

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for old, new in replacements.items():
        if f'>{old}<' in content or f'>{old} <' in content or old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated title case in {file}")

print("Title capitalization properly formatted.")
