from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import TaskViewSet  #ListTasks, DetailTask

router = SimpleRouter()
router.register('', TaskViewSet)

urlpatterns = router.urls

'''
urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('', ListTasks.as_view()),
]
'''