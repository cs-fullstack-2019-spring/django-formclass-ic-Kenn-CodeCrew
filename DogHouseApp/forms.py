from django import forms


class HouseLoanForm(forms.Form):
    name = forms.CharField()
    yearlySalary = forms.DecimalField()
    yearsLoan = forms.IntegerField()
    neighborhood = forms.CharField()


class DogAdoption(forms.Form):
    name = forms.CharField()
    breed = forms.CharField()
    age = forms.DecimalField()
    gender = forms.CharField()