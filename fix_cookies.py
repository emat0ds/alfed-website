import os

ANALYTICS_OLD = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-BKZCW39Q1N"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag("js", new Date());
gtag("config", "G-BKZCW39Q1N");
</script>'''

ANALYTICS_NEW = '''<script>
function loadAnalytics(){
  if(document.getElementById('ga-script'))return;
  var s=document.createElement('script');
  s.id='ga-script';
  s.async=true;
  s.src='https://www.googletagmanager.com/gtag/js?id=G-BKZCW39Q1N';
  document.head.appendChild(s);
  window.dataLayer=window.dataLayer||[];
  function gtag(){dataLayer.push(arguments);}
  window.gtag=gtag;
  gtag('js',new Date());
  gtag('config','G-BKZCW39Q1N');
}
if(localStorage.getItem('cookie-consent')==='accepted'){loadAnalytics();}
</script>'''

COOKIE_BANNER = '''<!-- COOKIE BANNER -->
<div id="cookie-banner" style="display:none;position:fixed;bottom:0;left:0;width:100%;background:#1E293B;color:white;padding:1.2rem 2rem;z-index:9999;font-family:'Poppins',sans-serif;">
    <div style="max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
        <p style="margin:0;font-size:0.9rem;flex:1;min-width:280px;">
            Questo sito usa cookie tecnici e di analisi per migliorare la tua esperienza.
            <a href="privacy.html" style="color:#F97316;text-decoration:none;">Privacy Policy</a>
        </p>
        <div style="display:flex;gap:0.8rem;">
            <button onclick="acceptCookies()" style="background:linear-gradient(135deg,#F97316,#FB923C);color:white;border:none;padding:0.6rem 1.5rem;border-radius:50px;font-weight:600;cursor:pointer;font-family:'Poppins',sans-serif;font-size:0.85rem;">Accetta</button>
            <button onclick="rejectCookies()" style="background:transparent;color:#94A3B8;border:1px solid #94A3B8;padding:0.6rem 1.5rem;border-radius:50px;font-weight:600;cursor:pointer;font-family:'Poppins',sans-serif;font-size:0.85rem;">Rifiuta</button>
        </div>
    </div>
</div>
<script>
function acceptCookies(){
    localStorage.setItem('cookie-consent','accepted');
    document.getElementById('cookie-banner').style.display='none';
    loadAnalytics();
}
function rejectCookies(){
    localStorage.setItem('cookie-consent','rejected');
    document.getElementById('cookie-banner').style.display='none';
}
if(!localStorage.getItem('cookie-consent')){
    document.getElementById('cookie-banner').style.display='block';
}
</script>
</body>'''

pages = ['index.html', 'funzionalita.html', 'prezzi.html', 'perche-sceglierci.html', 'contatti.html']

for page in pages:
    if not os.path.exists(page):
        print(f"❌ {page} non trovato")
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(ANALYTICS_OLD, ANALYTICS_NEW)
    content = content.replace('</body>', COOKIE_BANNER)
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ {page} aggiornato")

print("Done!")