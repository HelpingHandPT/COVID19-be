# Servidor DJango

Actualmente, apenas existe uma única app de teste que serve como exemplo e que
simplesmente retorna

**Nota**: actualmente,  a estrutura do projecto usa um *url.py* para cada
serviço, que por sua vez é incluindo no *url.py* da raíz do projecto. Esta é a
forma como o tutorial está estruturado e parece-me ser o melhor método para
organizar o projecto.

# API

### GET \\test\\

Retorna a string `“This is a test message indicating everything went ok!”`
indicando que o serviço está a funcionar.
