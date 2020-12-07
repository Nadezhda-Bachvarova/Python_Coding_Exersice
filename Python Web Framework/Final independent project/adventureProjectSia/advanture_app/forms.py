from django import forms

from advanture_app.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'image': forms.FileInput(attrs={'class': 'img_input'}),
        }
        fields = '__all__'


class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(
        required=False,
    )
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )


class CommentForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control rounded-2', }
    ))