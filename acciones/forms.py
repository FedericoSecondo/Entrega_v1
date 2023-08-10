from django import forms
from .models import Accion
from .models import CEOEmpresa
from .models import ResultadoEconomico


#----------------------------------------------------------------------------------------------
#  AQUI SE DETALLAN LOS FORMULARIOS CREADOS QUE PERMITEN CREAR NUEVOS DATOS PARA CADA MODELO
#----------------------------------------------------------------------------------------------

class AgregarAccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = ['simbolo', 'descripcion', 'fecha_fundacion']


class CEOEmpresaForm(forms.ModelForm):
    class Meta:
        model = CEOEmpresa
        fields = ['accion', 'nombre_director', 'nacionalidad', 'sitio_web']

    def clean_sitio_web(self):
        sitio_web = self.cleaned_data['sitio_web']
        return sitio_web
    


class ResultadoEconomicoForm(forms.ModelForm):
    class Meta:
        model = ResultadoEconomico
        fields = ['accion_comprada', 'resultado_ultimo_anio', 'proyeccion_proximo_anio']








