# tintim

Dados públicos, tim-tim por tim-tim. Página inicial de **painel.tintim.online**.

- `logo/`: logomarca (positiva, negativa e ícone), em SVG.
- `site/_modelo.html`: modelo da página; `site/montar.py` monta `site/public/index.html` com a logo e o mapa embutidos.
- `Dockerfile`: serve `site/public/` com nginx (usado pelo Easypanel).
