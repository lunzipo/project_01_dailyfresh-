from django.conf.urls import urls
from df_user import views

urlpatterns = [
	url(r'^register/$', views.register, name='register'),  # 显示注册页面
]