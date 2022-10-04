from email.message import Message
from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(req):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(req, 'index.html', context=context)

def contato(req):
    form = ContatoForm(req.POST or None) # nao tem dados quando carrega a pagina, somente quando os dados sao enviados
    if str(req.method) == 'POST':
        print(f'Post: {req.POST}')
        if form.is_valid():
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']

            # print('Mensagem enviada!')
            # print(f'Nome: {nome}')
            # print(f'E-mail: {email}')
            # print(f'Assunto: {assunto}')
            # print(f'Mensagem {mensagem}')

            form.send_email()

            messages.success(req, 'E-mail enviado com sucesso!')
            form = ContatoForm() # após enviar os dados os campos do formulário são limpos novamente.
        else:
            messages.error(req,'Erro ao enviar e-mail')
    context = {
        'form': form,
    }
    return render(req, 'contato.html', context=context)

def produto(req):
    if str(req.user) != 'AnonymousUser':
        if str(req.method) == 'POST':
            form = ProdutoModelForm(req.POST, req.FILES)
            if form.is_valid():
                # prod = form.save(commit=False) # form.save == False ainda nao salva
                # print(f'Nome: {prod.nome}')
                # print(f'Preco: {prod.preco}')
                # print(f'Estoque: {prod.estoque}')
                # print(f'Imagem: {prod.imagem}')
                form.save()
                
                messages.success(req, 'Produto salvo com sucesso')
                form = ProdutoModelForm() # limpar formulario
            else:
                messages.error(req, 'Erro ao salvar o produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form,
        } 
        return render(req, 'produto.html', context=context)
    else:
        return redirect('index')
