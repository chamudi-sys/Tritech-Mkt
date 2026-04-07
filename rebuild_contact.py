import os

with open("contact.html", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = '<div class="row align-items-center">'
end_marker = '      </div>\n    </div>\n  </section>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    before = text[:start_idx]
    after = text[end_idx:]
    
    new_html = """<div class="row mb-5">
        <!-- Contact Info & WhatsApp -->
        <div class="col-lg-5 col-md-12 mb-4 mb-lg-0">
          <div class="contact_info animate-on-scroll" style="background: #ffffff; border-radius: 15px; padding: 40px; box-shadow: 0 15px 35px rgba(0,0,0,0.05); border: 1px solid rgba(0, 0, 0, 0.05); height: 100%;">
            <div class="info_box" style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
              <i class="fas fa-map-marker-alt" style="font-size: 30px; color: #0f172a;"></i>
              <div>
                <h4 style="font-size: 22px; font-weight: 600; color: #0f172a; margin-bottom: 5px;">TRITECH Marketing Int (Pvt) Ltd</h4>
                <p style="font-size: 16px; color: #0f172a; margin: 0;">Colombo, Sri Lanka</p>
              </div>
            </div>
            <div class="info_box" style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
              <i class="fas fa-phone" style="font-size: 30px; color: #0f172a;"></i>
              <div>
                <p style="font-size: 16px; color: #0f172a; margin: 0;">
                  <strong style="color: #0f172a;">Call:</strong> 
                  <a href="tel:+94112345678" style="color: #0f172a; text-decoration: none; transition: all 0.3s ease;">+94 770109746</a>
                </p>
              </div>
            </div>
            <div class="info_box" style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
              <i class="fab fa-whatsapp" style="font-size: 30px; color: #25D366;"></i>
              <div>
                <p style="font-size: 16px; color: #0f172a; margin: 0;">
                  <strong style="color: #0f172a;">WhatsApp:</strong> 
                  <a href="https://wa.me/94770109746" target="_blank" style="color: #0f172a; text-decoration: none; transition: all 0.3s ease;">+94 770109746</a>
                </p>
              </div>
            </div>
            <div class="info_box" style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
              <i class="fas fa-envelope" style="font-size: 30px; color: #0f172a;"></i>
              <div>
                <p style="font-size: 16px; color: #0f172a; margin: 0;">
                  <strong style="color: #0f172a;">Email:</strong> 
                  <a href="mailto:sales.mkt@tritech.lk" style="color: #0f172a; text-decoration: none; transition: all 0.3s ease;">sales.mkt@tritech.lk</a>
                </p>
              </div>
            </div>
            <div class="info_box" style="display: flex; align-items: center; gap: 20px;">
              <i class="fas fa-clock" style="font-size: 30px; color: #0f172a;"></i>
              <div>
                <p style="font-size: 16px; color: #0f172a; margin: 0;">
                  <strong style="color: #0f172a;">Business Hours:</strong> <br>
                  <span>Mon - Fri: 8:30 AM - 5:30 PM</span> <br>
                  <span>Saturday: 8:30 AM - 1:30 PM</span>
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="col-lg-7 col-md-12 mb-4 mb-lg-0">
          <div class="contact_form animate-on-scroll" style="background: #ffffff; border-radius: 15px; padding: 40px; box-shadow: 0 15px 35px rgba(0,0,0,0.05); border: 1px solid rgba(0, 0, 0, 0.05); height: 100%;">
            <h3 style="font-size: 28px; font-weight: 700; color: #0f172a; margin-bottom: 25px;">Send a Message</h3>
            <form action="#">
              <div style="margin-bottom: 20px;">
                <input type="text" placeholder="Your Name" style="width: 100%; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; background: #f8fafc; font-family: 'Inter';" required />
              </div>
              <div style="margin-bottom: 20px;">
                <input type="email" placeholder="Email Address" style="width: 100%; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; background: #f8fafc; font-family: 'Inter';" required />
              </div>
              <div style="margin-bottom: 30px;">
                <textarea placeholder="Note / Message" rows="6" style="width: 100%; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; background: #f8fafc; font-family: 'Inter';" required></textarea>
              </div>
              <button type="submit" style="background: #d97706; color: white; border: none; padding: 15px 35px; border-radius: 8px; font-weight: 600; font-size: 16px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(217, 119, 6, 0.2); cursor: pointer;">Send Message <i class="fas fa-paper-plane" style="margin-left: 8px;"></i></button>
            </form>
          </div>
        </div>
      </div>

      <!-- Google Map Horizontal Ribbon -->
      <div class="row">
        <div class="col-12">
          <div class="map_container animate-on-scroll" style="height: 350px; border-radius: 15px; overflow: hidden; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05); border: 1px solid rgba(0, 0, 0, 0.05);">
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15841.115127949264!2d79.9451374!3d6.9763978!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ae257dcfbb2f773%3A0x63e77eb18ffa3ad6!2sTritech%20Engineers%20(Pvt)%20Ltd!5e0!3m2!1sen!2slk!4v1743288248373!5m2!1sen!2slk" 
              width="100%" 
              height="100%" 
              style="border:0;" 
              allowfullscreen="" 
              loading="lazy" 
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
          </div>
        </div>
"""
    
    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(before + new_html + after)
    print("SUCCESS")
else:
    print("FAILURE")
