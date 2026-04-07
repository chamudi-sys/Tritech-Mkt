import re
import os

os.system('git restore index.html')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Aquatherm Image Box
old_aq = re.search(r'<img[^>]*alt="Aquatherm Pipes"[^>]*>', text)
if old_aq:
    new_aq = '<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; width:100%; height:100%;"><img src="images/100.jpg" alt="PP-R Pipes" style="max-height: 60%; max-width: 100%; object-fit: contain; margin-bottom: 5px;"><img src="images/2.jpg" alt="Aquatherm Logo" style="max-height: 35%; max-width: 100%; object-fit: contain;"></div>'
    text = text[:old_aq.start()] + new_aq + text[old_aq.end():]

# Replace HDPE Image Box
old_hd = re.search(r'<img[^>]*alt="HDPE Pipes"[^>]*>', text)
if old_hd:
    new_hd = '<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; width:100%; height:100%;"><img src="images/103.jpg" alt="HDPE Pipes" style="max-height: 60%; max-width: 100%; object-fit: contain; margin-bottom: 5px;"><img src="images/puhei.jpeg" alt="Puhei Logo" style="max-height: 35%; max-width: 100%; object-fit: contain;"></div>'
    text = text[:old_hd.start()] + new_hd + text[old_hd.end():]

text = text.replace('Aquatherm Pipes', 'PP-R Pipes')

def get_block(name):
    # original code exactly repeats '</div>\s*</div>\s*</div>\s*</div>' for each item card
    pattern = rf'(<!-- {name} Pumps -->.*?</div>\s*</div>\s*</div>\s*</div>)'
    m = re.search(pattern, text, re.DOTALL)
    if not m: raise Exception(f"Missing {name}")
    return m

try:
    b_hl = get_block("Heng Long")
    b_eg = get_block("EVERGUSH")
    b_cp = get_block("Calpeda")
    b_ts = get_block("TSURUMI")
    b_sp = get_block("SPERONI")

    start_idx = min(b_hl.start(), b_eg.start(), b_cp.start(), b_ts.start(), b_sp.start())
    end_idx = max(b_hl.end(), b_eg.end(), b_cp.end(), b_ts.end(), b_sp.end())

    # Order: Speroni, Heng Long, Evergush, Tsurumi, Calpeda
    reordered = f"{b_sp.group(1)}\n\n                {b_hl.group(1)}\n\n                {b_eg.group(1)}\n\n                {b_ts.group(1)}\n\n                {b_cp.group(1)}"

    text = text[:start_idx] + reordered + text[end_idx:]
except Exception as e:
    print(f"Extraction error: {e}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored layout and updated content beautifully")
