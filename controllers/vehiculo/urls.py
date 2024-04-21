from django.urls import path,include

from use_cases.vehiculo.views import VehiculoAv,VehiculoDetailAv



urlpatterns=[
    path('api/vehiculo/',VehiculoAv.as_view(),name='vehiculo-list'),
    path('api/vehiculo/<int:pk>',VehiculoDetailAv.as_view(),name='vehiculo-detalle')
]