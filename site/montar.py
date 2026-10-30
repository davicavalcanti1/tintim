"""Monta index.html (para a Hostinger) e preview.html (prévia) a partir de _modelo.html, da logo e do mapa."""
import re
import urllib.parse
from pathlib import Path

AQUI = Path(__file__).resolve().parent
m = (AQUI / "_modelo.html").read_text(encoding="utf-8")
logo = (AQUI.parent / "logo" / "tintim-logo.svg").read_text(encoding="utf-8")
logo = re.sub(r"<title>.*?</title>\s*", "", logo)
logo = re.sub(r"<!--.*?-->\s*", "", logo)
logo = logo.replace('stroke="#0e4a55"', 'class="traco"').replace('fill="#e4684f"', 'class="pingo"')
logo = logo.replace('role="img" aria-label="tintim"', 'aria-hidden="true"')
icone = re.sub(r"<!--.*?-->\s*", "", (AQUI.parent / "logo" / "tintim-icone.svg").read_text(encoding="utf-8"))
mapa = (AQUI / "img" / "mapa-locais.svg").read_text(encoding="utf-8")
html = (m.replace("@@LOGO@@", logo.strip())
         .replace("@@ICONE_URI@@", urllib.parse.quote(" ".join(icone.split())))
         .replace("@@MAPA@@", mapa))
(AQUI / "preview.html").write_text(html, encoding="utf-8")
corte = html.index("<header")
(AQUI / "public").mkdir(exist_ok=True)
(AQUI / "public" / "index.html").write_text("<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n" + html[:corte]
                                 + "</head>\n<body>\n" + html[corte:] + "\n</body>\n</html>\n", encoding="utf-8")
print("ok", len(html))
