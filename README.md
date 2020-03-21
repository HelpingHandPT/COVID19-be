# COVID19-BE Documentação Técnica

Este documento contém tudo o que um developer precisa de saber para configurar e correr este software.

## Requisitos

Este software foi desenvolvido e otimizado para ser executado com os seguintes requisitos / dependências:

* Python >= 3.7

## Instalação

O código reside no GitHub. Antes de começarem, verifiquem se possuem uma assinatura GPG. Se não possuem ou não sabe como adicionar uma assinatura GPG à vossa conta, vejam a secção [Adicionar assinatura GPG](#adicionar-assinatura-gpg). Além disso, antes de iniciar, verifiquem se instalaram o software necessário.

1. Criar uma pasta onde quisermos
2. Abrir terminal nessa pasta vazia
3. Criar um virtualenv

Ubuntu e macOS

    python3 -m venv NOME

Windows


    python -m venv NOME

(O script cria a pasta de destino especificada e instala o pip (porque não especificamos a opção --without-pip))

4. Ativar o venv

Ubuntu e MacOS

Executa o seguinte commando para saber o nome da shell utilizada no terminal
    
    echo $SHELL

No macOS, o padrão é /bin/bash e isto significa que está a ser usada a bash shell. Dependendo da shell, devemos utilizar diferentes commandos para ativar o virtualenv.

No caso da bash shell ou zsh em Linux ou macOS, usar o seguinte comando para ativar o virtualenv

    NOME/bin/activate

No caso de csh ou tcsh shell, corer o seguinte comando para ativar o virtualenv
    
    NOME/bin/activate.csh

No caso de fish shell, corer o seguinte comando para ativar o virtualenv
    
    NOME/bin/activate.fish

Windows
    
    NOME\Scripts\activate

Para desativar, Linux, macOS e Windows

    deactivate


5.	Clone do repositório
   
  ````
  git clone git@github.com:tiago-peres/COVID19-be.git
  ````
    
6.	Mudar para o branch develop
  
  ````
  git checkout develop
  ````
    
7.	Criar um branch remoto (para as alterações que formos fazer)
  
  ````
  git checkout -b NOME
  ````
    
8.	Entrar dentro da pasta e instalar os requerimentos (se houver novos) 

   ````
   cd COVID19-be
   pip install -r requirements.txt 
   ````
    
9.	Correr o servidor

   ````
   python manage.py runserver 
   ````


10. Fazer o que quisermos. Depois para enviar as alterações que fizemos para o branch
   
   ````
   git add .
   git commit -m “MENSAGEM”
   git push origin BRANCH
   ````

## Adicionar assinatura GPG

Esta seção explica como adicionar uma assinatura GPG que pode ser usada com a vossa conta do GitHub. Assumimos que estão a trabalhar num ambiente Ubuntu / Debian ou, no caso de Windows, têm [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (sugerimos Ubuntu 18.04 LTS). A geração de GPG pode demorar muito, é por isso que recomendamos que instalem o **rng-tools** antes de começarem. Podem instalar o rng-tools executando este comando:

```commandline
$ sudo apt-get install rng-tools
```

A partir do terminal, executar o seguinte comando:

```commandline
$ gpg --gen-key
```

Serão perguntados que tipo de chave (key) querem (**Please select what kind of key you want:**). Escolham "1" (RSA):

```commandline
Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
```

Escolher o tamanho da chave (keysize). Nós recomendamos 2048 bits:

```commandline
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)
```

Agora temos de definir durante quanto tempo a a chave será válida. Escolham "0" (a chave nunca expira):

```commandline
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
```

Preencham os detalhess. Precisam de utilizar o email da vossa conta GitHub. Além disso, o email precisa de já ter sido verificado.

```commandline
You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and Email Address in this form:
    "Tiago Peres (Der Dichter) <tiagomartinsperes@gmail>"
```

Próximo passo é escolher a Passphrase para proteger a chave secreta. Introduzam a passphrase quando perguntados:

```commandline
You need a Passphrase to protect your secret key.
```

Após estes passos, deverão ver algo semelhante a isto:

```commandline
gpg: key 6707BED523BAE04F marked as ultimately trusted
gpg: revocation certificate stored as '/home/tiago/.gnupg/openpgp-revocs.d/8A78D192A0915490B2365B676707BED523BAE04F.rev'
public and secret key created and signed.

pub   rsa2048 2020-03-16 [SC]
      8A78D192A0915490B2365B676707BED523BAE04F
uid                      Tiago Peres <tiagomartinsperes@gmail.com>
sub   rsa2048 2020-03-16 [E]
```

Lista as chaves secretas

```commandline
$ gpg --list-secret-keys --keyid-format LONG
```

Exemplo de resultado:

```commandline
sec   rsa2048/6707BED523BAE04F 2020-03-16
      8A78D192A0915490B2365B676707BED523BAE04F
uid                 [ultimate] Tiago Peres <tiagomartinsperes@gmail.com>
ssb   rsa2048/27DA88CF2BFED46B 2020-03-16
```

Vamos usar **6707BED523BAE04F** para gerar o bloco de chave pública PGP. Substituir **6707BED523BAE04F** com a gerada pelo teu GPG. 

```commandline
$ gpg --armor --export 6707BED523BAE04F
```

Copiar o bloco de código gerado por este comando, inclusive **-----BEGIN PGP PUBLIC KEY BLOCK-----** e 
**-----END PGP PUBLIC KEY BLOCK-----**. Ir ao [GitHub -> Account -> Settings -> SSH and GPG keys](https://github.com/settings/keys) 
e adicionar a nova chave GPG.

De seguida, configurar a git signingkey globalmente:

```commandline
$ git config --global user.signingkey 6707BED523BAE04F
```

E é isso ! Agora, toda vez que fazem commit de um trabalho, devem adicionar o parâmetro -S

```commandline
$ git commit -S -m 'Helping Hand'
```

Por enquanto, aceitamos todos os commits para branches de desenvolvimento, mas isso mudará em breve. Divirtam-se!
