from django.db import models

from Accounts import models as AccountsModels
from ServerProject import models as ServerProjectModels

# Create your models here.
class Audit(models.Model):
    who_customer = models.ForeignKey(AccountsModels.customer, on_delete=models.CASCADE)
    who_provider = models.ForeignKey(AccountsModels.provider, on_delete=models.CASCADE)
    what_project = models.ForeignKey(ServerProjectModels.ServerProject, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now=False, auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
