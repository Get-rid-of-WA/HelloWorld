from django.db import models

from Accounts import models as AccountsModels
from ServerProject import models as ServerProjectModels

# Create your models here.
class Schedule(models.Model):
    own = models.ForeignKey(AccountsModels.provider, on_delete=models.CASCADE)
    project = models.ForeignKey(ServerProjectModels.ServerProject, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()