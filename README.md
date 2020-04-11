# COVID19 Backend

Este é o repositório do backend do projecto 1. Contém o servidor Django 

## A Ler
Antes de tudo, todos os novos utilizadores são aconselhados a lerem a [Wiki do Repositório](https://github.com/HelpingHandPT/COVID19-be/wiki)

## Requisitos

Este software foi desenvolvido e otimizado para ser executado com os seguintes requisitos / dependências:

* Python >= 3.7

## TODOs

Todas as tarefas a relizar estão explícitas como [Issues](https://github.com/HelpingHandPT/COVID19-be/issues) no repositório. Escolheu-se este modo porque o issue tracker do GitHub permite definir milestones e foi criado de forma a suportar TODOs.

## Bugs

Os bugs devem ser reportados igualmente nos [Issues do Repositório](https://github.com/HelpingHandPT/COVID19-be/issues) e devem seguir o seguinte template:

1. **Descrição Breve do Problema**
2. **Caminho da API (se aplicável)**
3. **Passos a Reproduzir (se reproduzível)**
4. **Resultado Esperado**

Antes de reportar bugs, certificar que o método em questão já foi implementado e não está em TODO.

# Django mapear modelos da BD

> https://docs.djangoproject.com/en/3.0/howto/legacy-databases/

`python manage.py inspectdb > models.py`

# Gerador serializers.py, views.py e urls.py

> https://github.com/Brobin/drf-generators

1. `python manage.py generate test_app --serializers`
2. `python manage.py generate test_app --views`
3. `python manage.py generate test_app --urls`

## Nota

Por enquanto, aceitamos todos os commits para branches de desenvolvimento, mas isso mudará em breve. Divirtam-se!
