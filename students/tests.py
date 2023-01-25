from django.test import TestCase
from .models import Student, Course

# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name="Test_First_Name", last_name="Test_Last_Name")
        Course.objects.create(department="CSC", number="394")


    def test_students_have_courses(self):

        course = Course.objects.get(id=1)

        student = Student.objects.get(id=1)

        student.student_courses.add(course)