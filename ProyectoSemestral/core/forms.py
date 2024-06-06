from django import forms
from .models import Orden, Producto

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        productos = Producto.objects.all()
        # Asegurarse de que las opciones del select incluyan los atributos data-precio y data-cantidad
        choices = []
        for producto in productos:
            choices.append((producto.pk, f"{producto.nombre_producto} - {producto.precio_unitario} - {producto.cantidad}"))
            self.fields['productos'].widget.attrs[f'data-precio-{producto.pk}'] = producto.precio_unitario
            self.fields['productos'].widget.attrs[f'data-cantidad-{producto.pk}'] = producto.cantidad
        self.fields['productos'].choices = choices

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
