from django.shortcuts import render, redirect
from myApp.models import Student

# Create your views here.


def home(request):
    return render(request, 'myApp/home.html')

def addStudent(request):
    return render(request, 'myApp/addStudent.html')

def add(request):
    try:
        first_name = request.GET["first_name"].title()
        last_name = request.GET["last_name"].title()
        age = int(request.GET["age"])
        address = request.GET["address"].upper()
        phone_number = request.GET["phone_number"]
        student_class = request.GET["student_class"]
        unique_number = request.GET["unique_number"]

        student = Student(first_name=first_name, last_name=last_name, 
                    age=age, address=address, phone_number=phone_number, student_class=student_class,unique_number=unique_number)
        student.save()

    except Exception as e:
        print("Unable to save to database: {}".format(e))
    return redirect("site-home")


def viewStudent(request):
    """
    Display only the details of the item_id specified.
    """
    try:
        # Get the item based on the item_id
        student = Student.objects.values()

        student = {"student": student}

        # Create and display the HTML page
        return render(request, 'myApp/viewStudent.html', student)
    except Exception as e:
        # TODO: Send an error message back to the main index page
        print("exception: {}".format(e))
        return redirect("site-home")

def delete(request):
    unique_number = request.GET["unique_number"]
    
    entry= Student.objects.filter(unique_number=unique_number)
    entry.delete()

    return redirect('site-viewStudent')