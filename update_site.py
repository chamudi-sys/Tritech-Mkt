import re
import glob

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Replace Aquatherm Pipes -> PP-R Pipes with dual images
pipe_match = re.search(r'(<!-- Aquatherm Pipes -->.*?</div>\s*</div>\s*</div>)', index_content, re.DOTALL)
if pipe_match:
    new_ppr = """<!-- PP-R Pipes -->
        <div class="col-12 col-sm-6 col-md-5 col-lg-4 mb-5 animate-on-scroll"
          style="opacity: 0; transition: all 0.6s ease 0.2s;">
          <div class="product-card"
            style="height: 100%; background: white; border-radius: 8px; overflow: hidden; 
                                                   box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: all 0.4s ease;">
            <div class="product-image-container"
              style="overflow: hidden; background: white; height: 160px; width: 100%; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #f0f0f0;">
              <img src="images/100.jpg" alt="PP-R Pipes"
                style="max-height: 90%; max-width: 90%; object-fit: contain; transition: all 0.5s ease;">
            </div>
            <div style="background: white; height: 80px; width: 100%; display: flex; align-items: center; justify-content: center;">
              <img src="images/2.jpg" alt="Aquatherm Logo" 
                 style="max-height: 80%; max-width: 80%; object-fit: contain;">
            </div>
            <div class="product-details"
              style="padding: 25px; background: #3a3a3a; height: 200px; display: flex; flex-direction: column;">
              <h4 style="font-size: 20px; font-weight: 600; margin-bottom: 15px; color: #ecf0f1; text-align: center; font-family: 'Outfit', sans-serif;">
                PP-R Pipes
              </h4>
              <p style="color: #bdc3c7; margin-bottom: 20px; text-align: center; line-height: 1.6; flex-grow: 1; font-family: 'Inter', sans-serif;">
                Quality you can trust. <br>
                Performance you can feel.
              </p>
              <div style="text-align: center;">
                <a href="aquatherm-details.html" class="product-link" style="color: #ecf0f1; font-weight: 500; font-size: 16px; position: relative; 
                                          display: inline-block; transition: all 0.3s ease; text-decoration: none;">
                  Explore Product
                  <span style="position: absolute; width: 0; height: 1px; bottom: -2px; left: 0; background: #ecf0f1; transition: width 0.3s ease;"></span>
                </a>
              </div>
            </div>
          </div>
        </div>"""
    index_content = index_content.replace(pipe_match.group(1), new_ppr)

hdpe_match = re.search(r'(<!-- HDPE Pipes -->.*?</div>\s*</div>\s*</div>)', index_content, re.DOTALL)
if hdpe_match:
    new_hdpe = """<!-- HDPE Pipes -->
        <div class="col-12 col-sm-6 col-md-5 col-lg-4 mb-5 animate-on-scroll"
          style="opacity: 0; transition: all 0.6s ease 0.3s;">
          <div class="product-card"
            style="height: 100%; background: white; border-radius: 8px; overflow: hidden; 
                                                   box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: all 0.4s ease;">
            <div class="product-image-container"
              style="overflow: hidden; background: white; height: 160px; width: 100%; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid #f0f0f0;">
              <img src="images/th.jpg" alt="HDPE Pipes"
                style="max-height: 90%; max-width: 90%; object-fit: contain; transition: all 0.5s ease;">
            </div>
            <div style="background: white; height: 80px; width: 100%; display: flex; align-items: center; justify-content: center;">
              <img src="images/puhei.jpeg" alt="Puhei Logo" 
                 style="max-height: 80%; max-width: 80%; object-fit: contain;">
            </div>
            <div class="product-details"
              style="padding: 25px; background: #3a3a3a; height: 200px; display: flex; flex-direction: column;">
              <h4 style="font-size: 20px; font-weight: 600; margin-bottom: 15px; color: #ecf0f1; text-align: center; font-family: 'Outfit', sans-serif;">
                HDPE Pipes
              </h4>
              <p style="color: #bdc3c7; margin-bottom: 20px; text-align: center; line-height: 1.6; flex-grow: 1; font-family: 'Inter', sans-serif;">
                Advance pipeing for a Demanding world.
              </p>
              <div style="text-align: center;">
                <a href="HDPE-details.html" class="product-link" style="color: #ecf0f1; font-weight: 500; font-size: 16px; position: relative; 
                                          display: inline-block; transition: all 0.3s ease; text-decoration: none;">
                  Explore Product
                  <span style="position: absolute; width: 0; height: 1px; bottom: -2px; left: 0; background: #ecf0f1; transition: width 0.3s ease;"></span>
                </a>
              </div>
            </div>
          </div>
        </div>"""
    index_content = index_content.replace(hdpe_match.group(1), new_hdpe)

# 2. Reorder Pumps block.
# Extract all pump blocks
pumps = {}
names = ["Heng Long", "EVERGUSH", "Calpeda", "TSURUMI", "SPERONI"]
for name in names:
    pattern = rf'(<!-- {name} Pumps -->.*?</div>\s*</div>\s*</div>)'
    match = re.search(pattern, index_content, re.DOTALL)
    if match:
        pumps[name] = match.group(1)

# Remove old pump blocks
row_start = index_content.find('<div class="row justify-content-center gx-3 gy-4">', index_content.find('<!-- Pumps Section -->'))
row_end = index_content.find('</div>', index_content.find('</div>\n          </div>\n        </div>', row_start) + 30) # Roughly find end of row
# A safer way to replace pumps: just replace the contents of the row.
pump_row_match = re.search(r'(<!-- Pumps Section -->.*?<div class="row justify-content-center gx-3 gy-4">)(.*?)(      </div>\n    </div>\n\n    <!-- Water Tanks Section -->)', index_content, re.DOTALL)

if pump_row_match and len(pumps) == 5:
    # New order: Speroni, Heng Long, Evergush, Tsurumi, Calpeda
    new_pump_html = "\n".join([pumps["SPERONI"], pumps["Heng Long"], pumps["EVERGUSH"], pumps["TSURUMI"], pumps["Calpeda"]])
    index_content = index_content[:pump_row_match.start(2)] + "\n" + new_pump_html + "\n" + index_content[pump_row_match.end(2):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

# 3. Add Back logic to detail pages
mapping = {
    'aquatherm-details.html': 'images/2.jpg',
    'AquathermGreen.html': 'images/2.jpg',
    'AquathermBlue.html': 'images/2.jpg',
    'AquathermRed.html': 'images/2.jpg',
    'HDPE-details.html': 'images/puhei.jpeg',
    'Heng-Long-details.html': 'images/3.jpg',
    'EVERGUSH-details.html': 'images/4.jpg',
    'Calpeda-details.html': 'images/1.png',
    'TSURUMI-details.html': 'images/5.png',
    'SPERONI-details.html': 'images/6.png',
    'GRP-details.html': 'images/1.png', # Same as water tanks maybe? Actually GRP Water tanks has 1.png in index
    'Piping.html': 'images/logo2.png',
    'Pumping.html': 'images/logo2.png',
    'WaterStorage.html': 'images/logo2.png',
}

def get_header(logo_url):
    return f"""\n    <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px; background: rgba(255,255,255,0.05); margin-bottom: 20px; border-bottom: 1px solid rgba(0,0,0,0.1);">
        <div style="display: flex; align-items: center; gap: 20px;">
            <a href="javascript:history.back()" style="padding: 8px 16px; background: #3a7bd5; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-family: sans-serif;">← Back</a>
            <img src="images/logo2.png" alt="Tritech Logo" style="height: 50px;">
        </div>
        <img src="{logo_url}" alt="Brand Logo" style="height: 50px; max-width: 150px; object-fit: contain; background: white; padding: 5px; border-radius: 5px;">
    </div>\n"""

# Note, in aquatherm and hdpe, there is an existing back button sometimes. If there is, we should remove the old back button.
for file, logo in mapping.items():
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old back buttons if any
        content = re.sub(r'<a[^>]*href="[^"]*products\.html"[^>]*>← Back to Products<\/a>', '', content)
        
        # Insert new custom top bar after opening body
        if '<div class="container">' in content and "Tritech Logo" not in content:
            content = content.replace('<div class="container">', '<div class="container">' + get_header(logo), 1)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except FileNotFoundError:
        pass

print("Update complete")
