from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import  ListTasks, DetailTask  #, TaskViewSet 

'''
router = SimpleRouter()
router.register('', TaskViewSet)

urlpatterns = router.urls
'''

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('', ListTasks.as_view()),
]
