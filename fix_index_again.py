with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace Epic Hero section
hero_orig = """  <!-- Epic Hero -->
  <section class="hero">
    <img src="images/10.png" class="hero-bg" alt="Industrial Background">
    <div class="hero-bg-accent"></div>
    <div class="hero-content" data-aos="zoom-in" data-aos-duration="1200">"""

hero_new = """  <!-- Epic Hero -->
  <section class="hero">
    <div id="heroCarousel" class="carousel slide carousel-fade position-absolute w-100 h-100" data-ride="carousel" data-interval="4000" style="top:0; left:0; z-index:0;">
      <div class="carousel-inner h-100">
        <div class="carousel-item active h-100">
          <img src="images/10.png" class="d-block w-100 h-100" style="object-fit: cover; opacity: 0.25;" alt="Slide 1">
        </div>
        <div class="carousel-item h-100">
          <img src="images/hero-bg.jpg" class="d-block w-100 h-100" style="object-fit: cover; opacity: 0.25; filter: saturate(1.2);" alt="Slide 2">
        </div>
        <div class="carousel-item h-100">
          <img src="images/o2.jpg" class="d-block w-100 h-100" style="object-fit: cover; opacity: 0.25; filter: saturate(1.2);" alt="Slide 3">
        </div>
      </div>
    </div>
    <div class="hero-bg-accent"></div>
    <div class="hero-content" data-aos="zoom-in" data-aos-duration="1200">"""

text = text.replace(hero_orig, hero_new)

# Replace Pipes Grid
pipes_orig = """      <!-- Pipes Grid -->
      <div class="section-header" data-aos="fade-up">
        <h2>Piping Solutions</h2>
        <div class="accent-line"></div>
      </div>
      <div class="row justify-content-center mb-5 pb-5">
        
        <!-- PP-R Pipes -->
        <div class="col-lg-5 col-md-6 mb-4" data-aos="fade-up" data-aos-delay="100">
          <div class="premium-card">
            <div class="premium-img-box">
              <img src="images/100.jpg" alt="PP-R" style="height: 110px; max-width: 100%; object-fit: contain; margin-bottom: 20px;">
              <img src="images/2.jpg" alt="Aquatherm" style="height: 50px; max-width: 100%; object-fit: contain;">
            </div>
            <div class="premium-details">
              <h4>PP-R Pipes</h4>
              <p>Top-tier polypropylene engineering. Quality you can trust, performance you can truly feel.</p>
              <a href="aquatherm-details.html" class="explore-btn">Discover Product <i class="fa fa-arrow-right"></i></a>
            </div>
          </div>
        </div>

        <!-- HDPE Pipes -->
        <div class="col-lg-5 col-md-6 mb-4" data-aos="fade-up" data-aos-delay="200">
          <div class="premium-card">
            <div class="premium-img-box">
              <img src="images/103.jpg" alt="HDPE" style="height: 110px; max-width: 100%; object-fit: contain; margin-bottom: 20px;">
              <img src="images/puhei.jpeg" alt="Puhei" style="height: 50px; max-width: 100%; object-fit: contain;">
            </div>
            <div class="premium-details">
              <h4>HDPE Pipes</h4>
              <p>Advanced high-density piping architected flawlessly for a consistently demanding world.</p>
              <a href="HDPE-details.html" class="explore-btn">Discover Product <i class="fa fa-arrow-right"></i></a>
            </div>
          </div>
        </div>

      </div>"""

pipes_new = """      <!-- Pipes Grid -->
      <div class="section-header" data-aos="fade-up">
        <h2>Piping Solutions</h2>
        <div class="accent-line"></div>
      </div>
      <div class="row justify-content-center mb-5 pb-5">
        
        <!-- PP-R Pipes -->
        <div class="col-lg-5 col-md-6 mb-4" data-aos="fade-up" data-aos-delay="100">
          <div class="premium-card">
            <div class="premium-img-box" style="height: 280px; padding: 30px 20px; display: flex; flex-direction: column;">
              <div style="display: flex; gap: 15px; justify-content: center; align-items: center; flex-grow: 1; min-height: 120px; position:relative;">
                <img src="images/101.jpg" alt="Blue PP-R" style="height: 90px; object-fit: contain; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));">
                <img src="images/100.jpg" alt="Green PP-R" style="height: 120px; object-fit: contain; transform: scale(1.1); z-index: 2; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.15)); border-radius: 10px;">
                <img src="images/102.jpg" alt="Red PP-R" style="height: 90px; object-fit: contain; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));">
              </div>
              <div style="height: 50px; display: flex; align-items: center; justify-content: center; margin-top: auto;">
                <img src="images/2.jpg" alt="Aquatherm" style="max-height: 100%; max-width: 100%; object-fit: contain; mix-blend-mode: multiply;">
              </div>
            </div>
            <div class="premium-details">
              <h4>PP-R Pipes</h4>
              <p>Top-tier polypropylene engineering. Quality you can trust, performance you can truly feel.</p>
              <a href="aquatherm-details.html" class="explore-btn">Discover Product <i class="fa fa-arrow-right"></i></a>
            </div>
          </div>
        </div>

        <!-- HDPE Pipes -->
        <div class="col-lg-5 col-md-6 mb-4" data-aos="fade-up" data-aos-delay="200">
          <div class="premium-card">
            <div class="premium-img-box" style="height: 280px; padding: 30px 20px; display: flex; flex-direction: column;">
              <div style="display: flex; justify-content: center; align-items: center; flex-grow: 1; min-height: 120px;">
                <img src="images/103.jpg" alt="HDPE" style="height: 110px; max-width: 100%; object-fit: contain; filter: drop-shadow(0 10px 20px rgba(0,0,0,0.1));">
              </div>
              <div style="height: 50px; display: flex; align-items: center; justify-content: center; margin-top: auto;">
                <img src="images/puhei.jpeg" alt="Puhei" style="max-height: 100%; max-width: 100%; object-fit: contain; mix-blend-mode: multiply;">
              </div>
            </div>
            <div class="premium-details">
              <h4>HDPE Pipes</h4>
              <p>Advanced high-density piping architected flawlessly for a consistently demanding world.</p>
              <a href="HDPE-details.html" class="explore-btn">Discover Product <i class="fa fa-arrow-right"></i></a>
            </div>
          </div>
        </div>

      </div>"""

text = text.replace(pipes_orig, pipes_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Modifications successful!")
