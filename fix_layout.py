import re
import glob

# 1. Fix detail pages: move back button to bottom
files = glob.glob('*-details.html') + ['Piping.html', 'Pumping.html', 'WaterStorage.html', 'AquathermGreen.html', 'AquathermBlue.html', 'AquathermRed.html']

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if the back button is in the top header we added
        back_btn_pattern = r'<a href="javascript:history\.back\(\)" style="padding: 8px 16px; background: #3a7bd5; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-family: [^"]+;">← Back</a>'
        
        if re.search(back_btn_pattern, content):
            # Remove it from top
            content = re.sub(back_btn_pattern, '', content)
            
            # Remove empty <div style="display: flex; align-items: center; gap: 20px;"> if needed
            content = re.sub(r'<div style="display: flex; align-items: center; gap: \d+px;">\s*<img src="images/logo2.png" alt="Tritech Logo" style="height: 50px;">\s*</div>',
                             r'<img src="images/logo2.png" alt="Tritech Logo" style="height: 50px;">', content)

            # Add it to the bottom, right before </body> or inside the container at the bottom
            back_btn_html = '\n    <div style="text-align: center; margin: 40px 0;"><a href="javascript:history.back()" style="display: inline-block; padding: 12px 25px; background-color: #3a7bd5; color: white; text-decoration: none; border-radius: 4px; font-size: 1.1rem; transition: background 0.3s ease;">← Back</a></div>\n'
            
            # Many pages have "</body>"
            if '</body>' in content:
                content = content.replace('</body>', back_btn_html + '</body>')
            else:
                content += back_btn_html

            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                
    except Exception as e:
        print(f"Error processing {file}: {e}")

# 2. Fix index.html pipe layout
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# We need to make sure the heights and layout exactly match the original structure.
# The original cards had ONE image container. Let's merge them into single container.
def fix_pipe(idx, pipe_name, img1, img2):
    pattern = rf'(<!-- {pipe_name}.*?<div class="product-card"[^>]*>)(.*?)(<div class="product-details")'
    match = re.search(pattern, idx, re.DOTALL)
    if match:
        new_img_container = f"""
            <div class="product-image-container" style="overflow: hidden; background: white; height: 220px; width: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 15px;">
                <img src="{img1}" alt="{pipe_name} Image" style="height: 120px; max-width: 100%; object-fit: contain; margin-bottom: 15px; transition: all 0.5s ease;">
                <img src="{img2}" alt="{pipe_name} Logo" style="height: 50px; max-width: 100%; object-fit: contain;">
            </div>
            """
        idx = idx[:match.start(2)] + new_img_container + idx[match.start(3):]
    return idx

idx = fix_pipe(idx, 'PP-R Pipes', 'images/100.jpg', 'images/2.jpg')
idx = fix_pipe(idx, 'HDPE Pipes', 'images/103.jpg', 'images/puhei.jpeg')

# Make sure the container row for pipes is closed properly in case python regex broke it
# I will just write changes to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("Done fixing layout")
