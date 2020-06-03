from django.contrib.auth.models import User
from django.db import models
STATE_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)


class Address(models.Model):
    address = models.CharField(max_length=255)
    address_complement = models.CharField(
        max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, choices=STATE_CHOICES)
    country = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Addresses'

    @property
    def address_complement_normalized(self):
        return '' if self.address_complement is None else self.address_complement

    def __str__(self):
        return '%s, %s, %s' % (self.address, self.city, self.country)
