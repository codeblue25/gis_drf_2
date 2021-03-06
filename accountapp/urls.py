from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken import views

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView, \
    AccountLoginView, AccountRetrieveTemplateView, \
    AccountUpdateTemplateView, AccountDestroyTemplateView, AccountRUDAPIView, AccountTokenRetrieveAPIView

app_name = 'accountapp'

urlpatterns = [
    # UI를 보기 위한
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    # 로직 처리를 위한
    path('hello_world/', hello_world, name='hello_world'),

    path('login_template/', AccountLoginView, name='login_template'),
    path('login/', views.obtain_auth_token, name='login'),

    path('logout_template/', TemplateView.as_view(template_name='accountapp/logout.html'), name='logout_template'),

    path('create_template/', AccountCreateTemplate, name='create_template'),
    path('', AccountCreateAPIView.as_view(), name='create'),

    path('retrieve_template/<int:pk>', AccountRetrieveTemplateView.as_view(), name='retrieve_template'),
    path('update_template/<int:pk>', AccountUpdateTemplateView.as_view(), name='update_template'),
    path('delete_template/<int:pk>', AccountDestroyTemplateView.as_view(), name='delete_template'),
    path('<int:pk>', AccountRUDAPIView.as_view(), name='RUD'),

    path('token/', AccountTokenRetrieveAPIView.as_view(), name='token'),
]