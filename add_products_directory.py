with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

injection = """      <!-- Our Products Directory -->
      <div class="section-header" data-aos="fade-up" id="our-products">
        <h2>Our Products</h2>
        <div class="accent-line"></div>
      </div>
      <div class="row justify-content-center mb-5 pb-5 bento-grid" style="grid-template-columns: repeat(3, 1fr);">
        
        <a href="#piping-section" class="bento-card text-center" style="text-decoration:none;" data-aos="fade-up" data-aos-delay="100">
          <img src="images/unified_ppr_pipes.png" alt="Pipes" style="height: 120px; object-fit: contain; mix-blend-mode: multiply; margin-bottom: 20px;">
          <h3 style="color: #0f172a; font-weight: 700; margin-bottom: 10px;">Piping & Plumbing</h3>
          <p style="color: #475569;">Advanced engineering plastic piping networks.</p>
        </a>

        <a href="#pumping-section" class="bento-card text-center" style="text-decoration:none;" data-aos="fade-up" data-aos-delay="200">
          <img src="images/speroni.png" alt="Pumps" style="height: 120px; object-fit: contain; mix-blend-mode: multiply; margin-bottom: 20px;">
          <h3 style="color: #0f172a; font-weight: 700; margin-bottom: 10px;">Pumping Systems</h3>
          <p style="color: #475569;">Unmatched fluid dynamic motor systems.</p>
        </a>

        <a href="WaterStorage.html" class="bento-card text-center" style="text-decoration:none;" data-aos="fade-up" data-aos-delay="300">
          <img src="images/1.png" alt="Water Tanks" style="height: 120px; max-width: 100%; object-fit: contain; mix-blend-mode: multiply; margin-bottom: 20px;">
          <h3 style="color: #0f172a; font-weight: 700; margin-bottom: 10px;">Water Storage Tanks</h3>
          <p style="color: #475569;">Heavy-duty GRP and modular water storage.</p>
        </a>
      </div>

      <div id="piping-section" style="padding-top: 100px; margin-top: -100px;"></div>
      <!-- Pipes Grid -->"""

# Inject before <!-- Pipes Grid -->
if "<!-- Pipes Grid -->" in text:
    text = text.replace("<!-- Pipes Grid -->", injection)
    
# Inject anchor for Pumping Section
if "<!-- Pumping Section -->" in text:
    pumping_anchor = '<div id="pumping-section" style="padding-top: 100px; margin-top: -100px;"></div>\n      <!-- Pumping Section -->'
    text = text.replace("<!-- Pumping Section -->", pumping_anchor)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Product Directory injected successfully.")

