import os
import glob
import re

css_block = """
<!-- PREMIUM MODERN AESTHETIC OVERRIDE -->
<style id="premium-modern-aesthetic">
/* Import Modern Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;800&display=swap');

body, p, a, div, span, li, button {
  font-family: 'Inter', sans-serif !important;
}

h1, h2, h3, h4, h5, h6, .navbar-brand, .nav-link, .elegant-heading, .service-title {
  font-family: 'Outfit', sans-serif !important;
  letter-spacing: -0.5px !important;
}

/* Fixed Glass Navbar */
.glass-nav {
  position: fixed;
  top: 0; width: 100%; z-index: 1000;
  background: rgba(255, 255, 255, 0.85) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border-bottom: 1px solid rgba(0,0,0,0.05) !important;
  transition: all 0.3s ease !important;
  padding: 15px 0 !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.02) !important;
}
.glass-nav .nav-link {
  color: #0f172a !important;
  font-weight: 500 !important;
  margin: 0 15px !important;
  position: relative !important;
  transition: 0.3s ease !important;
}
.glass-nav .nav-link:hover {
  color: #d97706 !important;
  transform: translateY(-2px) !important;
}

/* Standardize backgrounds if page feels too legacy */
.sub_page {
    background-color: #FAFAFA !important;
}
</style>
"""

new_nav = """
  <!-- Floating Nav -->
  <nav class="glass-nav">
    <div class="container" style="display: flex; justify-content: space-between; align-items: center;">
      <a href="index.html">
        <img src="images/logo2.png" alt="Tritech" style="height: 45px;">
      </a>
      <div class="d-none d-lg-flex" style="display: flex;">
        <a href="index.html" class="nav-link">Home</a>
        <a href="about.html" class="nav-link">About Us</a>
        <a href="products.html" class="nav-link">Products</a>
        <a href="contact.html" class="nav-link">Contact Us</a>
      </div>
      <button class="btn d-lg-none" style="color:#0f172a;"><i class="fa fa-bars" style="font-size: 1.5rem;"></i></button>
    </div>
  </nav>
"""

for file in glob.glob('*.html'):
    if file in ('index.html', 'index_backup.html'):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Inject CSS before </head>
    if 'id="premium-modern-aesthetic"' not in content and '</head>' in content:
        content = content.replace('</head>', css_block + '\n</head>')
        changed = True
    
    # 2. Replace old navbar
    old_nav_pattern = r'<!-- header section starts -->.*?<!-- end header section -->'
    if re.search(old_nav_pattern, content, re.DOTALL):
        content = re.sub(old_nav_pattern, '', content, flags=re.DOTALL)
        
        body_match = re.search(r'<body[^>]*>', content)
        if body_match and 'class="glass-nav"' not in content:
            content = content[:body_match.end()] + "\n" + new_nav + content[body_match.end():]
        changed = True
        
    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')

print('Script finished')
