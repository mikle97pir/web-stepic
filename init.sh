sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
killall -q gunicorn
gunicorn -b 0.0.0.0:8080 -w 4 --chdir etc -D --error-logfile=/home/box/gunicorn.log --capture-output hello:app
sudo /etc/init.d/nginx restart
