

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Usuario(models.Model):
    sobrenome = models.CharField(max_length=100)
    matricula = models.CharField(
        max_length=7,
        unique=True,
        validators=[MinLengthValidator(7), MaxLengthValidator(7)]
    )
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.sobrenome

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('MANUTENCAO', 'Em manutenção'),
        ('DESATIVADO', 'Desativado'),
    ]
    
    modelo = models.CharField(max_length=50, default='Spark X1')
    numero_serie = models.CharField(
        max_length=5,
        unique=True,
        validators=[MinLengthValidator(5), MaxLengthValidator(5)]
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='DISPONIVEL')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.modelo} - {self.numero_serie}"

class Aluguel(models.Model):
    STATUS_CHOICES = [
        ('ANDAMENTO', 'Em andamento'),
        ('DEVOLVIDO', 'Devolvido'),
        ('ATRASADO', 'Atrasado'),
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_saida = models.DateTimeField(auto_now_add=True)
    data_devolucao_prevista = models.DateTimeField()
    data_devolucao_real = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ANDAMENTO')

    def save(self, *args, **kwargs):
        if self.data_devolucao_real and self.data_devolucao_real > self.data_devolucao_prevista:
            self.status = 'ATRASADO'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.sobrenome} - {self.equipamento.modelo}"