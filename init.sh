sudo rm -f /etc/nginx/sites-enabled/default
sudo ln /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo rm -f /etc/gunicorn.d/django.example
sudo rm -f /etc/gunicorn.d/wsgi.example
sudo ln /home/box/web/etc/hello.conf /etc/gunicorn.d/
