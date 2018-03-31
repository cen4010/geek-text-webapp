from django.forms import *

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['anonymous', 'rating', 'comment']
        widgets = {
            'anonymous': CheckboxInput(attrs={'class': 'form-check-input'}),
            'rating': Select(attrs={'class': 'form-control'}, choices=(
                (None, 'None'),
                (1, '★☆☆☆☆'),
                (2, '★★☆☆☆'),
                (3, '★★★☆☆'),
                (4, '★★★★☆'),
                (5, '★★★★★')
            )),
            'comment': Textarea(attrs={'class': 'form-control'})
        }
