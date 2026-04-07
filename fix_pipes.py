import os

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

orig = """              <div style="display: flex; gap: 5px; justify-content: center; align-items: center; flex-grow: 1; min-height: 120px; position:relative;">
                <img src="images/101.jpg" alt="Blue PP-R" style="height: 80px; object-fit: contain; mix-blend-mode: multiply;">
                <img src="images/100.jpg" alt="Green PP-R" style="height: 110px; object-fit: contain; mix-blend-mode: multiply; z-index: 2;">
                <img src="images/102.jpg" alt="Red PP-R" style="height: 80px; object-fit: contain; mix-blend-mode: multiply;">
              </div>"""

new = """              <div style="display: flex; gap: 0px; justify-content: center; align-items: center; flex-grow: 1; min-height: 120px; position:relative;">
                <img src="images/101.jpg" alt="Blue PP-R" style="height: 110px; object-fit: contain; mix-blend-mode: darken; transform: scale(1.3) translateX(15px);">
                <img src="images/100.jpg" alt="Green PP-R" style="height: 150px; object-fit: contain; mix-blend-mode: darken; z-index: 3; transform: scale(1.3);">
                <img src="images/102.jpg" alt="Red PP-R" style="height: 110px; object-fit: contain; mix-blend-mode: darken; transform: scale(1.3) translateX(-15px);">
              </div>"""

if orig in text:
    text = text.replace(orig, new)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("SUCCESS")
else:
    print("FAIL to find ORIG")

