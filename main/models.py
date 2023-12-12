from django.db import models

# Create your models here.
STATUSES = (
    ('todo', 'Todo'),
    ('doing', 'Doing'),
    ('done', 'Done')
)
class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=600, blank=True)
    status = models.CharField(choices=STATUSES)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}' if len(self.title) < 20 else f'{self.title[:20]}...'

