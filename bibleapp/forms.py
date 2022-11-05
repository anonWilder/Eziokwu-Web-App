from django import forms

class loginForm(forms.Form):
	username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control form-control-lg'}))
	password = forms.CharField(label='Username',widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control form-control-lg'}))

class descriptionForm(forms.Form):
    description = forms.CharField(label='Description',widget=forms.Textarea(attrs={'placeholder':'Enter description','class':'form-control form-control-lg','rows':'30','columns':'7'}))
    