sudo ln -sf /home/box/web/etc/conf.nginx /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
killall -q gunicorn
gunicorn -b 0.0.0.0:8080 -w 2 --chdir /home/box/web/etc -D --error-logfile=/home/box/gunicorn_hello.log --capture-output hello:app
gunicorn -b 0.0.0.0:8000 -w 2 --chdir /home/box/web/ask -D --error-logfile=/home/box/gunicorn_ask.log --capture-output ask.wsgi
sudo /etc/init.d/nginx restart