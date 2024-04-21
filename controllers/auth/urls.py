from django.urls import path



from use_cases.auth.views import login_view,logout_view
urlpatterns=[
    path('api/auth/login',login_view,name='login-app'),
    path('api/auth/logout',logout_view,name='logout-app'),
]