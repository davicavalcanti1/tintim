# Página inicial (painel.tintim.online): serve site/public com nginx
FROM nginx:1.27-alpine
COPY site/nginx.conf /etc/nginx/conf.d/default.conf
COPY site/public/ /usr/share/nginx/html/
EXPOSE 80
