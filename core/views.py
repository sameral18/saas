from .models import User, Course,Message
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import SignupForm, AddCourseForm, AddWorkerForm,AddStudentForm,AddMessageForm
from django.views.generic import ListView


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = '/profile/'


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "GET":
            return render(request,'login.html')
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                print('user or pass is wrong')
    return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        coursename = request.POST['coursename']
        coursedescription = request.POST['coursedescription']
        coursepoints = request.POST['coursepoints']

        t = Course.objects.all()

        print(t.count())
    allcourses=Course.objects.all()
    allstudents=User.objects.filter(role=2).values()
    allworkers=User.objects.filter(role=3).values()

    return render(request,'profile.html',{'Course':allcourses,'UserStudent':allstudents,'UserWorker':allworkers})

@method_decorator(login_required(login_url='login'),name='dispatch')
class AccountSettingsView(UpdateView):
    model = User
    fields = ['username','email','first_name','last_name','avg','collage']
    template_name = 'account_settings.html'
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user


class add_courseView(CreateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'add-course.html'
    success_url = '/profile/'


class all_coursesView(ListView):
    model = Course
    template_name = 'allcourses.html'



class add_studentView(CreateView):
    model = Course
    form_class = AddStudentForm
    template_name = 'add-student.html'
    success_url = '/profile/'



class all_studentsView(ListView):
    model = User
    template_name = 'allstudents.html'



class add_workerView(CreateView):
    model = Course
    form_class = AddWorkerForm
    template_name = 'add-worker.html'
    success_url = '/profile/'

class all_workersView(ListView):
    model = User
    template_name = 'allworkers.html'



class add_messageView(CreateView):
    model = Message
    form_class = AddMessageForm
    template_name = 'add-message.html'
    success_url = '/profile/'

class all_messagesView(ListView):
    model = Message
    template_name = 'message.html'



def TestView(request):
    userModel= User.objects.all()
    testModel=Course.objects.all()
    return render(request,'courses.html',{'User':userModel,'Test':testModel})

class DeleteUser(DeleteView):
    model = User
    template_name = 'delete_user_confirm.html'
    success_message='user deleted'
    success_url = '/'