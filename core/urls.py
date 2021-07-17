from django.urls import path
from .views import (
    home,
    lista_medicos,
    medico_novo,
    medico_update,
    #lista_postos,
    #posto_novo,
    #posto_update,
    lista_escalas,
    escala_novo,
    escala_update,
    escala_delete,
    lista_folgas,
    folga_novo,
    folga_update,
    folga_delete,
    PdfEscalas
    
)



urlpatterns = [
    path('', home, name='core_home'),
    path('medicos', lista_medicos, name='core_lista_medicos'),
    path('medico-novo', medico_novo, name='core_medico_novo'),
    path('medico-update/<int:id>/', medico_update, name='core_medico_update'),
    
    #path('postos', lista_postos, name='core_lista_postos'),
    #path('posto-novo', posto_novo, name='core_posto_novo'),
    #path('posto-update/<int:id>/', posto_update, name='core_posto_update'),

    path('escalas', lista_escalas, name='core_lista_escalas'), 
    path('escala-novo', escala_novo, name='core_escala_novo'),
    path('escala-update/<int:id>/', escala_update, name='core_escala_update'),
    path('escala-delete/<int:id>/', escala_delete, name='core_escala_delete'),
    path('relatorio-pdf/', PdfEscalas.as_view(),name='relatorio_pdf_escalas'),

    path('folgas', lista_folgas, name='core_lista_folgas'),
    path('folga-novo', folga_novo, name='core_folga_novo'),
    path('folga-update/<int:id>/', folga_update, name='core_folga_update'),
    path('folga-delete/<int:id>/', folga_delete, name='core_folga_delete'),
]
