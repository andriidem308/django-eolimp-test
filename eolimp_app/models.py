from django.db import models
from django.contrib.auth.models import AbstractUser, User

#
# class User(AbstractUser):
#     is_teacher = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Group(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['group_name']


class Problem(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField()

    class Meta:
        ordering = ['date_created']


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['last_name', 'first_name']


class Solution(models.Model):
    problem_id = models.OneToOneField(Problem, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution_code = models.TextField()
    score = models.IntegerField(default=0)
    date_solved = models.DateTimeField()

    class Meta:
        ordering = ['date_solved']


class Lecture(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField()

    class Meta:
        ordering = ['date_created']


class Attachment(models.Model):
    lecture_id = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    attachment_file = models.FilePathField()

    class Meta:
        ordering = ['pk']


class ProblemTest(models.Model):
    problem_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.CharField(max_length=255)
    output_data = models.CharField(max_length=255)

    class Meta:
        ordering = ['pk']
