create database ask character set utf8mb4 collate utf8mb4_unicode_ci;
use ask;
create user 'django_app'@'localhost' identified by 'django_pass';
grant all on ask.* to 'django_app'@'localhost' identified by 'django_pass';