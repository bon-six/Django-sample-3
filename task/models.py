from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    status_choices = (('Initial', 'Initial'), 
                      ('On-going','On-going'), 
                      ('Closed','Closed')
    )
    status = models.CharField(max_length=20, choices=status_choices)
    pub_date = models.DateField()
    due_date = models.DateField()
    manager = models.ForeignKey(user_model, null=True, 
                         on_delete=models.SET_NULL,
                         related_name='managing_tasks'
    )
    member = models.ManyToManyField(user_model, blank=True, 
                         related_name='involving_tasks'
    )

    def __str__(self):
        return self.title
