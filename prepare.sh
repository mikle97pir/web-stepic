sudo apt update
sudo apt install python3.5
virtualenv -p python3.5 /home/box/web_study
source /home/box/web_study/bin/activate
pip install --upgrade pip
pip install gunicorn
pip install django~=2.0.1