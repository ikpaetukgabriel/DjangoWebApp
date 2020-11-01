from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author':'Gabriel',
        'title': 'llll'
    },
    {
        'author':'Camilla',
        'title': 'mmmm'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'myApp/home.html', context)

def addStudent(request):
    return render(request, 'myApp/addStudent.html', {'name': 'Add Student oh'})

def viewStudent(request):
    return render(request, 'myApp/viewStudent.html', {'name': 'View Student oh'})

