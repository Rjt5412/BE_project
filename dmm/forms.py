'''
from django import forms


category = []
sub_category = []




class Search_form(forms.Form):
    search = forms.CharField(label="search", max_length=100)
    twitter =  forms.CharField(required=False, label="checkbox1",max_length=100)
    gplus = forms.CharField(required=False, label="checkbox2",max_length=100)
    tumblr = forms.CharField(required=False, label="checkbox3",max_length=100)
    category = forms.CharField(required=False, name="Main_Category",max_length=100)
    sub_category = forms.CharField(required=False, name="Sub_Category",max_length=100)

'''