from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)

class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions
    def __str__(self):
        return self.user.username

class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


class Stude(models.Model):
    CLASS_CHOICES = [
        ('2019MPFT-Aug5-Sep6','2019MPFT-Aug5-Sep6'),
    ]
    PARTICIPATE_CHOICES = [
        ('Yes','Yes'),
        ('No','NO'),
        ('Maybe','Maybe')
    ]
    CORE_CHOICES = [
        ('Yes','Yes'),
        ('No','NO'),
        ('Maybe','Maybe')
    ]
    INFLUENCE_CHOICES = [
        ('Facebook','Facebook'),
        ('Twitter','Twitter'),
        ('Alumni','Alumni'),
        ('Event','Event'),
        ('Instagram','Instagram'),
        ('Moringa-Website','Moringa-Website'),
        ('Referall','Referall'),
        ('Google','Google'),
        ('Nairobi-Tech-Week','Nairobi-Tech-Week'),
        ('Other','Other')
    ]
    HEAR_CHOICES = [
        ('Facebook','Facebook'),
        ('Twitter','Twitter'),
        ('Alumni','Alumni'),
        ('Event','Event'),
        ('Instagram','Instagram'),
        ('Moringa-Website','Moringa-Website'),
        ('Referall','Referall'),
        ('Google','Google'),
        ('Nairobi-Tech-Week','Nairobi-Tech-Week'),
        ('Other','Other')
    ]
    EDUCATION_CHOICES = [
        ('High-School','High-School'),
        ('Diploma','Diploma'),
        ('Bachelor-Degree','Bachelor-Degree'),
        ('Masters','Masters'),
        ('Doctorate','Doctorate'),
        ('Other','Other')

    ]
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Prefer not to say','Prefer not to say')
    ]
    PAY_CHOICES = [
        ('Yes','Yes'),
        ('No','No')
    ]
    first_name = models.CharField(max_length =40)
    last_name = models.CharField(max_length =40)
    email = models.CharField(max_length =100)
    class_name = models.CharField(max_length =100,choices=CLASS_CHOICES)
    phone_Number =   models.IntegerField(default=0, null=True)
    Gender = models.CharField(max_length =100,choices=GENDER_CHOICES, null=True)
    Have_you_participated_in_a_Moringa_School_training_before = models.CharField(max_length =100,choices=PARTICIPATE_CHOICES, null=True)
    Are_you_interested_in_joining_Moringa_Core_after_Moringa_Prep =models.CharField(max_length =100,choices=CORE_CHOICES, null=True)
    Where_did_you_hear_about_Moringa_School = models.CharField(max_length =100,choices=HEAR_CHOICES, null=True)
    Whcih_avenue_was_most_influential_in_joining_Moringa_School =models.CharField(max_length =100,choices=INFLUENCE_CHOICES, null=True)
    Do_you_understand_that_you_need_to_pay_the_full_amount = models.CharField(max_length =100,choices=PAY_CHOICES, null=True)
    What_is_your_highest_level_of_education_completed =models.CharField(max_length =100,choices=EDUCATION_CHOICES, null=True)
    article_link = models.CharField(max_length =100)

    def __str__(self):
<<<<<<< HEAD
        name = self.first_name
        return name
=======
        name = self.first_name     
        return name
>>>>>>> origin/feature/models
