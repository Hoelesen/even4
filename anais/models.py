from django.db import models

# Create your models here.
# models: Evento, Trabalho, Autor, Área Temática
class AreaTematica(models.Model):
    nome = models.CharField(max_length=100)

#banner, resumo, artigo completo ...
class Modalidade(models.Model):
        nome = models.CharField(max_length=100)

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    apresentação = models.TextField()
    #corpo editorial (comissão científica e comissão organizadora)
    comissao_organizadora = models.TextField()
    comissao_cientifica = models.TextField()
    areas_tematicas = models.ManyToManyField(AreaTematica)
    contato = models.CharField(max_length=200)
    #edicoes_anteriores
    edicao_anterior = models.OneToOneField('Evento', null=True, on_delete=models.SET_NULL)
    anais = models.OneToOneField('Anais', null=True, on_delete=models.CASCADE)
    icone = models.ImageField(upload_to='images/')
    banner = models.ImageField(upload_to='images/')

class Anais(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=17)
    data_de_publicacao = models.DateField()
    pais_de_publicacao = models.CharField(max_length=100)#país
    idioma_de_publicacao = models.CharField(max_length=100)

class Trabalho(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField('Autor')
    modalidade = models.ForeignKey(Modalidade, related_name='trabalhos', on_delete=models.SET_NULL, null=True)
    area_tematica = models.ForeignKey(AreaTematica, related_name='trabalhos', on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=200, null=True)
    anais = models.ForeignKey(Anais, related_name='trabalhos', on_delete=models.SET_NULL, null=True)
    pdf = models.FileField(upload_to='uploads/%Y/')

class Afiliacao(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=100)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nome_para_citacao = models.CharField(max_length=100)
    contato = models.EmailField()
    afiliacao = models.ForeignKey(Afiliacao, related_name='autores', on_delete=models.SET_NULL, null=True)
