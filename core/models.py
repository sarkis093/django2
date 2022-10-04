from distutils.command.upload import upload
from django.db import models
from stdimage.models import StdImageField
# SIGNALS
from django.db.models import signals # fazer alguma coisa (pode ser antes ou depois) de inserir no banco de dados
from django.template.defaultfilters import slugify #(slug e.g = "url-com-hífen")

# essa classe serve como Base para outras classes
class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    #classe "Base" é abstrata, ou seja, não hé criada em banco de dados, serve como rascunho para outras classes
    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

#funcao fora da clase
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

# antes de salvar executa a funcao "produto_pre_save", quando houver qualquer chamada(sinal/signal) para a classe "Produto"
signals.pre_save.connect(produto_pre_save, sender=Produto)