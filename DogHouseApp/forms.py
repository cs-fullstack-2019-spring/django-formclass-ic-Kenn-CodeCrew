from django import forms


class HouseLoanForm(forms.Form):
    name = forms.CharField()
    yearlySalary = forms.DecimalField()
    yearsLoan = forms.IntegerField()
    neighborhood = forms.CharField()
