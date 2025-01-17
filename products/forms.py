from django import forms

from categories.models import Category
from .models import Product


class ProductModelForm(forms.ModelForm):
    name = forms.CharField(label="Nombre del producto",max_length=254, min_length=5)
    description = forms.CharField(label='Descripción', min_length=5, max_length=254, widget=forms.Textarea, required=False)
    discount = forms.IntegerField(min_value=0, max_value=100, label="Porcentaje de descuento")
    class Meta:
        model = Product
        fields = '__all__'

    categories = forms.ModelMultipleChoiceField(label="Categorias",queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['categorias'] = [c.pk for c in kwargs['instance'].categorias.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

        def save(self):
            instance = forms.ModelForm.save(self)
            instance.topping_set.clear()
            instance.topping_set.add(*self.cleaned_data['categorias'])
            return instance

