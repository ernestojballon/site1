from django.db import models
from django.utils import timezone
import datetime
from django.db import connection




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def alll(self):
        with connection.cursor() as cursor:
            # cursor.execute("select * from question where pub_date= %s", [self.pub_date])
            cursor.execute('select * from polls_question')
            row = cursor.fetchall()

        return row
    def imp(self):
        print('hola')
        return

    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text