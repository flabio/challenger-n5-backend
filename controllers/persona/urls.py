from django.urls import path,include

from use_cases.persona.views import PersonaAv,PersonaDetalleAv,PersonaInformeDetail

urlpatterns=[
    path('api/persona/',PersonaAv.as_view(),name='persona-list'),
    path('api/persona/<int:pk>',PersonaDetalleAv.as_view(),name='persona-detalle'),
    path('api/persona/generar_informe/<str:email>/',PersonaInformeDetail.as_view(),name='generar-informe'),
    
    
]