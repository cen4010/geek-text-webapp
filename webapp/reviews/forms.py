from django.forms import ModelForm, HiddenInput, ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from reviews.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['anonymous', 'rating', 'comment']

    # Seems like a hack, look for a cleaner way to check unique constraints.
    def clean(self):
        super().clean()
        self.instance.validate_unique()
