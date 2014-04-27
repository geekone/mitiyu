//
admin@admin.com
admin
admin

//登录代码
     {% if request.user.is_authenticated %}
		<div class="pull-right">
			<a href=#>欢迎您：{{request.user}}</a>&nbsp;&nbsp;
			<a class="btn danger small" href="#">注销</a>
		</div>
{% else %}
          <form action="{% url "mitiyu.views.login_view" %}" method='post' class="pull-right">
			{% csrf_token %}
            <input name='username' class="input-small" type="text" placeholder="用户名">
            <input name='password' class="input-small" type="password" placeholder="密码">
            <button class="btn" type="submit">登录</button>
          </form>
{% endif %}

http://www.cnblogs.com/BeginMan/p/3387997.html
http://blog.csdn.net/feng88724/article/details/7262514


//登录:
在验证登录的地方加上,默认url accounts/login
@login_required()
如果修改成登录url路径/backend/accounts/login 加上 @login_required(login_url='/backend/accounts/login/')

如果在mitiyu.urls 里面使用:url(r'^accounts/login/$', 'django.contrib.auth.views.login'),使用默认的templates 默认跳转到“templates\registration\login.html”这个模板
(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),