from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    type = forms.ChoiceField(choices=[("dog", "dog"), ("cat", "cat"), ("parrot",
                                                                       "parrot")], required=True, widget=forms.Select(
        attrs={
            'class': 'form-control'
        },
    ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    age = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'type': 'number'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control rounded-2'
        }
    ))

    class Meta:
        model = Pet
        fields = ('type', 'name', 'age', 'description', 'image_url')


# class PetForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         for (_, field) in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#     class Meta:
#         model = Pet
#         fields = '__all__'
#         widgets = {
#             'image_url': forms.TextInput(
#                 attrs={
#                     'id': 'img_input',
#                 }
#             )
#         }