# cms_dj
django_cms


本项目是基于Django的一个cms内容管理系统

#安装：


首先安装虚拟环境，不想虚拟环境也可以正式环境，然后pip install -r requirements.txt安装依赖库


#配置：


项目使用的是mysql数据库，具体数据库设置到setting下的DATABASE中去修改，改为自己的数据库账号密码，然后进入项目根目录执行


python manage.py makemigrations


python manage.py migrate
进行数据库迁移

#启动：

进入根目录，python manage.py runserver启动，默认端口8000，如果被占用，可在启动时加上端口号，例如：python manage.py runserver 8888
