from django.db import models


class Config(models.Model):
    nomeDaConfiguracao = models.CharField(max_length=100)
    navBarCor = models.CharField(max_length=7)
    tituloPag = models.CharField(max_length=100)
    textNavBarCor = models.CharField(max_length=7)
    sobreEventoCor = models.CharField(max_length=7)
    textSobreOEventoCor = models.CharField(max_length=100)
    programacaoEventoCor = models.CharField(max_length=7)
    textProgramacaoEventoCor = models.CharField(max_length=100)
    contatoCor = models.CharField(max_length=7)
    textContatoCor = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.nomeDaConfiguracao


    class Meta():
        verbose_name_plural = "Configurações"
