from django import forms
from .models import Book, Address, Student, Address2, Student2, ProfilePicture

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'profile_picture']
        
class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']
        
class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses', 'profile_picture']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }
        
class ProfilePictureForm(forms.ModelForm):
    model = ProfilePicture
    fields = ['student', 'image']
