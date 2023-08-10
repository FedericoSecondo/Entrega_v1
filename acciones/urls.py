from django.urls import path, include
from .views import *
from .views import lista_resultados_economicos

urlpatterns = [
    path('', index, name='inicio'),
    path('acciones/', lista_acciones, name='lista_acciones'),
    path('compras/', lista_compras, name='lista_compras'),
    path('resultados/', lista_resultados_economicos, name='lista_resultados'),
    path('ceos/', lista_ceos, name='lista_ceos'),

    #---------------------------------------------------------------------------
    #URLS para FORMULARIOS
    #---------------------------------------------------------------------------

    path('agregar/', agregar_accion, name='agregar_accion'),#formulario para agregar acciones
    
    path('agregar-ceo/', agregar_ceo, name='agregar_ceo'), #formulario para agregar ceos

    path('agregar-resultado/', agregar_resultado, name='agregar_resultado'), #formulario para agregar resultados economicos

#------------------------------------------------------------------------------
#URLS Para CRUDS
#-------------------------------------------------------------------------------

    path('acciones/updateAccion/<int:id_accion>/',updateAccion, name='update_accion'), #url para hacer un update de las acciones a monitorear, permite editar cualquier campo, simbolo, descripcion, fecha de fundacion

    path('acciones/deleteAccion/<int:id_accion>/', deleteAccion, name='deleteAccion'), #url para hacer un borrar las acciones a monitorear
 
    path('editar-ceo/<int:ceo_id>/',editar_ceo, name='editar_ceo'), #url para editar informacion financiera de empresas

    path('eliminar-ceo/<int:id_ceo>/',eliminar_ceo, name='eliminar_ceo'), #url para borrar informacion financiera de empresas

  

]




    

    