# Sistema de Mensagens AMQP

Este projeto demonstra como enviar mensagens usando o protocolo AMQP (Advanced Message Queuing Protocol) com a biblioteca `is_wire.core`. 
O código permite que os usuários publiquem mensagens para diferentes destinatários em um broker de mensagens.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado:

- Python 3.x
- A biblioteca `is_wire` (instale via pip)
- Um broker AMQP (como RabbitMQ) em execução

## Explicação

Esse repositório possui dois algoritmos que desempenham as seguintes funções:
 - pub_aula1: Esse algoritmo pode ser dividido em alguns passos:
   - Solicita o usuário o ip para se conectar com um Broker RabbitMQ previamente ativo;
   - Cria um loop onde o usuário publica mensagens para outros usuários. O algoritmo solicita o nome do usuário destino e a mensagem a ser publicada. As mensagens serão armazenadas no tópico "Aluno.(NomeDoAlunoDestino)".;

- sub_aula1: Esse algoritmo pode ser dividido em alguns passos:
   - Solicita o usuário o ip para se conectar com um Broker RabbitMQ previamente ativo;
   - Cria um loop onde o usuário consome mensagens de um tópico. O algoritmo solicita o nome do tópico. As mensagens serão consumidas do tópico "Aluno.(NomeDoAlunoDestino)"

## A seguir um passo a passo de como os arquivos foram enviados para este repositorio

- git init #inicia um repositorio local
- git add pub_aula1.py #adiciona o arquivo que criamos no repositorio local criado
- git add sub_aula1.py #msm coisa
- git commit -m "Att geral" # adiciona um commit master (-m) com comentario "att geral"
- git push #envia o repositorio local criado


## A seguir um passo a passo dos comandos usados para criar um docker com os arquivos criados

- mkdir docker1 # cria uma pasta chamada docker1 separada para criar os arquivos docker
- nano Dockerfile # É necessário criar um arquivo chamado Dockerfile que vai conter a imagem docker ( a imagem está no repositorio vitorbermond/espaco1:pubsub no docker hub)
- mv sub_aula1.py ~/docker1 # no nosso caso foi necessario usar esse comando move para jogar os arquivos criados numa pasta separada junto ao dockerfile
- mv pub_aula1.py ~/docker1 # msm coisa
- docker build -t vitorbermond/espaco1:pubsub . # constroi a imagem docker usando os itens na pasta criada
- docker images # É possível ver as imagens docker criadas na maquina
- docker push vitorbermond/espaco1:pubsub # envia a imagem criada e construida para o docker hub
- docker run -ti vitorbermond/espaco1:pubsub # roda a imagem que acabamos de criar (os arquivos serao executados)

para baixar a imagem em outro lugar é so usar pull em vez de push
- docker pull vitorbermond/espaco1:pubsub 


