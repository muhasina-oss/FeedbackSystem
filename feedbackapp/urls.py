from django.urls import path

from feedbackapp.views import RegisterUserView,FeedbackListCreateView
from feedbackapp.views import FeedbackRetrieveUpdateDeleteView,FeedbackAnalyticsView


urlpatterns = [
  
  path('users/',RegisterUserView.as_view()),
  
  path('feedbacks/',FeedbackListCreateView.as_view()),
    
  path('feedbacks/<int:pk>/',FeedbackRetrieveUpdateDeleteView.as_view()),
  
  path('feedbacks/summary/',FeedbackAnalyticsView.as_view()),
]
