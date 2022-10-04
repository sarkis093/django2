from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

# PARA CADA FORMULARIO DA APLICACAO, IREMOS TER UMA CLASSE.
# existem form's diferentes(comportamentos) ex: "forms.Form", "forms.ModelForm"...

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=50)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@meudominio.com.br',
            to=['contato@meudominio.com.br','outroemail@email.com'],
            headers={'Reply-to': email}
        )

        mail.send()

#formulario (form) de Produtos.
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']