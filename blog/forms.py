
from django import forms
from cloudinary.forms import CloudinaryFileField

from blog.models import Post


class ModelnameCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image')
    image = CloudinaryFileField(
            options={'folder': 'media/Model_image', 'tags': 'Model_name'})
    movie = CloudinaryFileField(
            options={'folder': 'media/Model_movie', 'tags': 'Model_name',
                     'resource_type': 'video'})