# school_roster_app/views.py

from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name,
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = { 
      "school_name": my_school.name,
      "staff": my_school.staff,
      }
    return render(request, "pages/list_staff.html", my_data)


def staff_detail(request, employee_id):
    staff = my_school.find_staff_by_id(employee_id)
    my_data = { 
      "school_name": my_school.name,
      "staff": staff,
      }
    return render(request, "pages/staff_detail.html", my_data)


def list_students(request):
    my_data = {
      "school_name": my_school.name,
      "students": my_school.students,
      }
    return render(request, "pages/list_students.html", my_data)


def student_detail(request, student_id):
    student = my_school.find_student_by_id(student_id)
    my_data = { 
      "school_name": my_school.name,
      "student": student,
    }
    return render(request, "pages/student_detail.html", my_data)