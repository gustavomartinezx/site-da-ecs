from django.db import models

class Extensionista(models.Model):
    AREA_CHOICES = [
        ("COMOP", "COMOP"),
        ("COPED", "COPED"),
        ("COAD", "COAD"),
        ("COED", "COED"),
    ]


    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    rgm = models.CharField(max_length=20, unique=True)
    area = models.CharField(max_length=6, choices=AREA_CHOICES)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        from django.utils import timezone
        if self.pk:
            self.updated_at = timezone.now()
        elif not self.updated_at:
            self.updated_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ({self.area})"
