from django.urls import path,include

from use_cases.infraccion.views import InfraccionAV,InfraccionDetailAV





urlpatterns=[
    path('api/infraccion/',InfraccionAV.as_view(),name='infraccion-list'),
    path('api/infraccion/<int:pk>',InfraccionDetailAV.as_view(),name='infraccion-detalle')
]