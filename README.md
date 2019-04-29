## clone
```bash
git clone https://github.com/lanieee/myblog.git
cd myblog 
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser 
python manage.py runserver
```


- ## step-1
```bash
# 创建文件夹
mkdir myblog
# 创建项目文件
django-admin startproject main myblog
# 创建.gitignore README.md文件（Linux命令）
# 创建git忽略文件（添加一些忽略规则）
touch .gitignore
# 创建REAMDE.md文件 
touch REAMDE.md
# 进入项目
cd myblog
# 创建迁移文件（创建，修改数据库）
python manage.py migrate 
# 运行项目 默认8000端口 可自定义
python manage.py runserver <127.0.0.1:8282>

```

# Step-2
```bash
# 创建应用
python manage.py startapp pages
# 创建模型迁移文件
python manage.py makemigrations
# 数据迁移
python manage.py migrate
```

# Step-3
```bash 
# 进入Django-Shell(便于执行数据库操作)
python manage.py shell
```