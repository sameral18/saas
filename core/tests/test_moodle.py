
from django.test import TestCase
from django.contrib.auth.models import Course


class CourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name='Test Course',
            description='This is a test course',
            course_points=100
        )

    def test_course_str(self):
        self.assertEqual(str(self.course), 'Test Course')

    def test_course_fields(self):
        self.assertEqual(self.course.name, 'Test Course')
        self.assertEqual(self.course.description, 'This is a test course')
        self.assertEqual(self.course.course_points, 100)

    def test_course_points_default_value(self):
        course = Course.objects.create(name='Test Course 2')
        self.assertEqual(course.course_points, None)
