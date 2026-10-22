from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
# ### Category Choices
# - Faculty
# - Academics
# - Infrastructure
# - Administration
# - Facilities
# - Other

  CATEGORY_CHOICES = (
    ('faculty','Faculty'),
    ('academics','Academics'),
    ('infrastructure','Infrastructure'),
    ('administration','Administration'),
    ('facilities','Facilities'),
    ('other','Other')
    
  )
  
  DEPARTMENT_CHOICES = (
    ('cse','Computer Science'),
    ('ece','Electronics and Communication'),
    ('eee','Electrical and Electronics'),
    ('me','Mechanical'),
    ('ce','Civil'),
    ('ai_ds','AI and Data Science'),
    ('other','Other')
  )
  
  SENTIMENT_CHOICES = (
    ('positive','Positive'),
    ('negative','Negative'),
    ('neutral','Neutral'),
    ('unknown','Unknown')
  )
 
  
  student = models.ForeignKey(User,on_delete=models.CASCADE)
  
  department = models.CharField(max_length=200,choices=DEPARTMENT_CHOICES)
  
  feedback_text = models.TextField()
  
  sentiment = models.CharField(max_length=200,choices=SENTIMENT_CHOICES)
  
  category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)
  
  created_at = models.DateTimeField(auto_now_add=True)
  
  