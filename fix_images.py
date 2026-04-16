import re

# Mappa placeholder → immagine
replacements = {
    '📸 Foto: Imprenditore/titolare rilassato ma professionale, magari in un contesto dinamico (non per forza al computer)': ('img/hero-team.jpg', 'Team ALFED'),
    '📸 Foto: Team al lavoro, riunione informale, collaborazione': ('img/problema.jpg', 'Team al lavoro'),
    '📸 Foto: Schermo con grafici / dashboard': ('img/beneficio-dashboard.jpg', 'Dashboard'),
    '📸 Foto: Persone che collaborano / team': ('img/beneficio-team.jpg', 'Team'),
    '📸 Foto: Soldi / investimento / crescita': ('img/beneficio-roi.jpg', 'ROI'),
    '📸 Foto: Persona che usa telefono / semplicità': ('img/beneficio-semplice.jpg', 'Semplicità'),
    '📸 Auto': ('img/settore-auto.jpg', 'Auto e noleggio'),
    '📸 Solare': ('img/settore-solare.jpg', 'Fotovoltaico'),
    '📸 Viaggio': ('img/settore-viaggi.jpg', 'Viaggi e vacanze'),
    '📸 Soldi': ('img/settore-finanza.jpg', 'Finanziamenti'),
    '📸 Casa': ('img/settore-infissi.jpg', 'Infissi'),
    '📸 Scudo': ('img/settore-assicurazioni.jpg', 'Assicurazioni'),
    '📸 Studio': ('img/settore-formazione.jpg', 'Formazione'),
    '📸 Edificio': ('img/settore-immobiliare.jpg', 'Immobiliare'),
    '📸 Persona soddisfatta, stretta di mano, successo': ('img/cta.jpg', 'Successo'),
    '📸 Foto: Persona pensierosa/preoccupata mentre guarda numeri, oppure team in discussione': ('img/problema.jpg', 'Il problema'),
    '📸 Dashboard': ('img/beneficio-dashboard.jpg', 'Dashboard'),
    '📸 Team': ('img/beneficio-team.jpg', 'Team'),
    '📸 Grafici': ('img/beneficio-roi.jpg', 'ROI'),
    '📸 Semplice': ('img/beneficio-semplice.jpg', 'Semplicità'),
    '📸 Foto: Persona soddisfatta, stretta di mano, successo': ('img/cta.jpg', 'Successo'),
}

pages = ['index.html', 'funzionalita.html', 'prezzi.html', 'perche-sceglierci.html', 'contatti.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        for placeholder, (img_src, alt) in replacements.items():
            # Sostituisce il div img-placeholder che contiene il placeholder
            pattern = r'<div class="img-placeholder">[^<]*' + re.escape(placeholder) + r'[^<]*</div>'
            replacement = f'<img src="{img_src}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;">'
            content = re.sub(pattern, replacement, content)

        if content != original:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {page} aggiornato")
        else:
            print(f"⚠️  {page} nessuna modifica")

    except FileNotFoundError:
        print(f"❌ {page} non trovato")

print("Done!")