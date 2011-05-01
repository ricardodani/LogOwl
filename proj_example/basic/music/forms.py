# -*- encoding: utf-8 -*-

from django.forms import ModelForm
from basic.music.models import *

class GenreForm(ModelForm):
    class Meta:
        model = Genre

class LabelForm(ModelForm):
    class Meta:
        model = Label

class BandForm(ModelForm):
    class Meta:
        model = Band

class AlbumForm(ModelForm):
    class Meta:
        model = Album

class TrackForm(ModelForm):
    class Meta:
        model = Track
