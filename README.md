# API Agendamento de Tarefas:
A API aqui desenvolvida tem a função de uma "To-Do List". A aplicação feita em FLASK representa um exemplo clássico de API de microserviços. Permite adicionar novas tarefas, atualizar parcialmente ou completamente as informações, além de excluir tarefas existentes, ou seja, o CRUD de todos os dias.

A API expõe rotas para acesso completo das tarefas anotadas ('/tarefas'), todas armazenadas por enquanto em um arquivo JSON. Para facilitar o manuseio dos dados de forma individual uma rota por id foi criada ('/tarefas/<int: id>'). Nesta rota é permitido utilizar os métodos HTTP (GET, POST, PUT, PATCH e DELETE), tendo cada um seu comportamente característico. 

## DEPLOY
O deploy da aplicação encontra-se disponível em no link: [Agendamento-de-tarefas](
https://agendamento-tarefas.onrender.com/)

## Próximas implementações:
1. Documentação com Swagger
2. Desing frontend 
3. Manipulação das tarefas pelo navegador/frontend
