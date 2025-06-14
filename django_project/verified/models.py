from django.db import models

class VerifiedAddress(models.Model):
    wallet_address = models.CharField(max_length=80, unique=True)
    verified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wallet_address
