from django.urls import path,include

from use_cases.oficial.views import OficialAv



urlpatterns=[
    path('api/oficial/',OficialAv.as_view(),name='oficial-list'),
    
    
]