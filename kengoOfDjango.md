记录下django使用中的坑，利人利己。

django：1.10.6

1. 在模板中使用{{STATIC_URL}} 值为空
	检查setting文件中
	1） STATIC_URL = '/static/' 设置（默认有）
	2） INSTALLED_APPS[] 是否包含 'django.contrib.staticfiles',(默认有)
	3） 在TEMPLATES=[
			{
				...

				'OPTIONS': {
					'context_processors': [
						...

						#在此添加
						'django.template.context_processors.static',
					]
				}
			}
		]

2. form表单中使用 {% csrf_token %}出现csrf验证失败
	1）setting文件MIDDLEWARE下 'django.middleware.csrf.CsrfViewMiddleware',（默认有）
	2）view中使用render()跳转。（from django.shortcuts import render）

3. 使用mysql数据库连接出现"Access denied for user '**'@'localhost' (using password: YES)")
	1）setting中修改DATABASES下 'USERNAME': 为 'USER':

4.（windows下）使用model_to_dict()出现'charmap' codec can't encode characters....
	1）cmd编码设置为936（命令：chcp 936）,无效使用管理员打开cmd，右击选择属性切换。

