create database ask character set UTF8 collate utf8_bin;
use ask;
create user 'django_app'@'localhost' identified by 'django_pass';
grant all on ask.* to 'django_app'@'localhost' identified by 'django_pass';