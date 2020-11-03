from django import forms
from .models import Pizza, Size


# class PizzaForm(forms.Form):
    ## topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.PasswordInput)
    # topping1 = forms.CharField(label='Topping 1', max_length=100)
    # topping2 = forms.CharField(label='Topping 2', max_length=100)
    ## toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olive', 'Olive')], widget=forms.CheckboxSelectMultiple)
    # size = forms.ChoiceField(label='Size', choices=[ ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large') ])

class PizzaForm(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
    # image = forms.ImageField()
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}
        # widgets = {'topping1':forms.CheckboxSelectMultiple}


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)