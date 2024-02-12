from django import forms
from django.db.transaction import commit

from fruitipediaapp.common.mixins import ReadonlyFieldMixin
from fruitipediaapp.fruits.models import Fruit
from fruitipediaapp.profiles.models import Profile


class BaseFruitForm(forms.ModelForm, ReadonlyFieldMixin):
    class Meta:
        model = Fruit
        exclude = ['owner', ]

        labels = {
            'name': False,
            'image_url': False,
            'description': False,
            'nutrition': False,
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'})
        }


class CreateFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateFruitForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        fruit = super(CreateFruitForm, self).save(commit=False)

        if self.user is not None:
            fruit.owner = Profile.objects.get(first_name=self.user)
        if commit:
            fruit.save()

        return fruit


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    class Meta(BaseFruitForm.Meta):
        exclude = ['owner', 'nutrition', ]

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
        }

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
