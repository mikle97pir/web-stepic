sudo apt update
echo "updated"
sudo apt install python3.5
echo "installed python 3.5"
sudo apt install python3.5-dev
echo "installed python 3.5 dev"
virtualenv -p python3.5 /home/box/web_study
echo "created venv"
source /home/box/web_study/bin/activate
echo "activated venv"
pip install --upgrade pip
echo "upgraded pip"
pip install gunicorn
echo "installed gunicorn"
pip install django~=2.0.1
echo "installed django"
pip install mysqlclient
echo "installed mysqlclient"
sudo /etc/init.d/mysql start
echo "started mysql"
sudo mysql -uroot < create_database.sql
echo "created database"
python /home/box/web/ask/manage.py makemigrations
echo "created migrations"
python /home/box/web/ask/manage.py migrate
echo "migrated"
