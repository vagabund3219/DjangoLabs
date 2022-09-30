from django import forms

class UserForm(forms.Form):

    name = forms.CharField(label='Client name', max_length=15,help_text='Second name must be no longer 15 symbols')
    age = forms.IntegerField(label='Client age')
    check=forms.BooleanField(label='Are you male?')
    choose=forms.NullBooleanField(label='Are you male' )
    email = forms.EmailField(label='Write your mail')
    # reg = forms.RegexField(label='Input mail', regex=r'[0-9]+', error_messages=({'required': 'only nmbers!!!'}))
    reg = forms.RegexField(regex="G.*s")
    urlText = forms.URLField(label="Input url")
    filePath=forms.FilePathField(label='Choose file', path='C:/Users/lqmn/Downloads')
    file=forms.FileField(label='File')
