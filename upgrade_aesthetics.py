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

/* Navbar Enhancement */
header {
  background: rgba(15, 23, 42, 0.3) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border-bottom: 1px solid rgba(255,255,255,0.05) !important;
}

/* Nav links hover */
.custom_nav-container .nav-link {
  transition: all 0.3s ease !important;
  color: #fff !important;
}
.custom_nav-container .nav-link:hover {
  color: #F59E0B !important;
  transform: translateY(-2px) !important;
}

/* Hero Section */
.hero_area .bg-box img {
  filter: brightness(0.7) contrast(1.1) saturate(1.2) !important;
}
.detail-box {
  padding: 40px 50px !important;
  background: rgba(15, 23, 42, 0.4) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
  border-left: 6px solid #F59E0B !important;
  border-radius: 24px !important;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5) !important;
}

.detail-box h1 {
  font-size: 56px !important;
  background: linear-gradient(135deg, #FCD34D, #F59E0B, #D97706) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  text-shadow: none !important;
}

.detail-box p {
  color: #F8FAFC !important;
  font-weight: 300 !important;
  text-shadow: none !important;
}

/* Services section */
.services-section {
  background: #0F172A !important;
}
.elegant-heading {
  background: linear-gradient(135deg, #FCD34D, #F59E0B) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}

.service-item {
  background: rgba(30, 41, 59, 0.5) !important;
  backdrop-filter: blur(8px) !important;
  padding: 20px !important;
  border-radius: 16px !important;
  border: 1px solid rgba(255,255,255,0.05) !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
.service-item:hover {
  transform: translateY(-8px) !important;
  background: rgba(51, 65, 85, 0.6) !important;
  box-shadow: 0 15px 30px rgba(0,0,0,0.3) !important;
  border-color: rgba(245, 158, 11, 0.3) !important;
}
.service-item i {
  color: #F59E0B !important;
}

/* Products Section General Headers */
.section-title {
  color: #0F172A !important;
  font-weight: 800 !important;
}
.category-header h3 {
  border-bottom: none !important;
  position: relative !important;
  color: #1E293B !important;
}
.category-header h3::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 30%;
  right: 30%;
  height: 4px;
  border-radius: 4px;
  background: linear-gradient(90deg, #3B82F6, #8B5CF6) !important;
}

/* Product Cards */
.product-card {
  border-radius: 20px !important;
  border: 1px solid rgba(0,0,0,0.05) !important;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
  background: #ffffff !important;
}
.product-card:hover {
  transform: translateY(-8px) scale(1.02) !important;
  box-shadow: 0 25px 50px rgba(0,0,0,0.15) !important;
}

/* Force light background on all parts of the card */
.product-image-container, .product-image-container + div {
  background: #ffffff !important;
  border-bottom: 0px !important; /* hide default borders */
}

/* Details area styling */
.product-details {
  background: #ffffff !important;
  border-top: 1px solid #F1F5F9 !important;
}
.product-details h4 {
  color: #0F172A !important;
  font-weight: 700 !important;
}
.product-details p {
  color: #475569 !important;
}

/* Interactive explore buttons */
.product-link {
  color: #3B82F6 !important;
  background: rgba(59, 130, 246, 0.1) !important;
  padding: 8px 18px !important;
  border-radius: 9999px !important;
  font-weight: 600 !important;
  border: none !important;
}
.product-link:hover {
  background: rgba(59, 130, 246, 0.2) !important;
  color: #1D4ED8 !important;
  text-decoration: none !important;
}
.product-link span {
  display: none !important; /* Hide old underline line */
}

/* Bottom "Find more" or explore cards if any */
</style>
<!-- END PREMIUM AESTHETIC OVERRIDE -->
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove old premium block if exists
text = re.sub(r'<!-- PREMIUM MODERN AESTHETIC OVERRIDE -->.*?<!-- END PREMIUM AESTHETIC OVERRIDE -->\n?', '', text, flags=re.DOTALL)

# Insert before closing head
if '</head>' in text:
    text = text.replace('</head>', css_block + '</head>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected UI Override")
else:
    print("Could not find </head>")
