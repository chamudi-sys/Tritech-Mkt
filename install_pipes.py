import os

# Copy the asset safely
os.system('cp /Users/liveroom/.gemini/antigravity/brain/fff605ab-07d6-42bd-bc7d-df3fdd3c681b/unified_ppr_pipes_*.png /Users/liveroom/Desktop/tritech/TRITECH/images/unified_ppr_pipes.png')

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

orig = """              <div
                style="display: flex; gap: 0px; justify-content: center; align-items: center; flex-grow: 1; min-height: 120px; position:relative;">
                <img src="images/101.jpg" alt="Blue PP-R"
                  style="height: 110px; object-fit: contain; mix-blend-mode: darken; transform: scale(1.3) translateX(15px);">
                <img src="images/100.jpg" alt="Green PP-R"
                  style="height: 150px; object-fit: contain; mix-blend-mode: darken; z-index: 2; transform: scale(1.3);">
                <img src="images/102.jpg" alt="Red PP-R"
                  style="height: 110px; object-fit: contain; mix-blend-mode: darken; transform: scale(1.3) translateX(-15px);">
              </div>"""

new = """              <div style="display: flex; justify-content: center; align-items: flex-end; flex-grow: 1; min-height: 120px; padding-bottom: 5px;">
                <img src="images/unified_ppr_pipes.png" alt="Aquatherm PP-R Pipes" style="height: 160px; max-width: 100%; object-fit: contain; mix-blend-mode: multiply; transform: scale(1.3);">
              </div>"""

if orig in text:
    text = text.replace(orig, new)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("HTML safely updated and deployed.")
else:
    print("FAILED TO FIND ORIG")

