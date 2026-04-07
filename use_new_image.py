import os
import glob

# Copy the asset safely
os.system('cp /Users/liveroom/.gemini/antigravity/brain/fff605ab-07d6-42bd-bc7d-df3fdd3c681b/single_hdpe_pipe_*.png /Users/liveroom/Desktop/tritech/TRITECH/images/single_hdpe_pipe.png')

# Update all references safely
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'images/103.jpg' in content:
        content = content.replace('images/103.jpg', 'images/single_hdpe_pipe.png')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Asset deployment complete.")
