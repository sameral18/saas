from django.contrib.auth.forms import UserCreationForm
from .models import User, Course,Message
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2','avg','collage']




class AddCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name','description']



class AddMessageForm(ModelForm):
    class Meta:
        model = Message
        fields=['to','msg_from','subject','message']



class AddWorkerForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2','collage','role']


class AddStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2','avg','collage']



