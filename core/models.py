from django.db import models
 
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_admissao = models.DateField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = ['nome', 'sobrenome', 'data_admissao']

    def __str__(self):
        return str(self.nome) 

'''
class Posto(models.Model):
    nome = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = ['nome', 'rua', 'numero']

    def __str__(self):
        return self.nome
'''


class Folga(models.Model):
    data = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['data', 'medico']

    def __str__(self):
        return str(self.data) +' - '+ str(self.medico)


class Escala(models.Model):
    data = models.DateField(null=True)
    #posto = models.ForeignKey(Posto, on_delete=models.SET_NULL, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        unique_together = ['data', 'medico']

    def __str__(self):
        return str(self.medico)
