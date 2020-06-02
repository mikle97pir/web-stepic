create database ask;
use ask;
create user 'django_app'@'localhost' identified by 'django_pass';
grant all on ask.* to 'django_app'@'localhost' identified by 'django_pass';