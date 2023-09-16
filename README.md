# Documentação do Projeto - Recuperação de Carrinhos Abandonados

## Introdução
Este projeto tem como objetivo criar uma solução para aumentar as vendas de uma loja virtual, focando em fechar pedidos de clientes que abandonaram produtos em seus carrinhos de compras. Para isso, a solução envolve o envio de mensagens de retorno via e-mail, SMS e WhatsApp para esses clientes, incentivando-os a retornar ao carrinho e concluir a compra.

## Requisitos do Projeto
Para implementar essa solução, foram definidos os seguintes requisitos:

1. Recuperação de Dados dos Carrinhos Abandonados:
   - Os dados dos carrinhos abandonados são recuperados de uma fonte externa, que fornece informações sobre os produtos no carrinho, os detalhes do cliente e o momento em que o carrinho foi abandonado.
   - Esses dados são armazenados em um formato estruturado que pode ser processado para identificar os clientes e produtos associados a carrinhos abandonados.

2. Comunicação Multicanal:
   - A solução deve ser capaz de se comunicar com os clientes por meio de três canais: e-mail, SMS e WhatsApp.
   - A comunicação deve ser personalizada, incluindo informações sobre os produtos no carrinho e uma mensagem persuasiva para incentivar o cliente a retornar e concluir a compra.

3. Integração com Twilio:
   - A solução utiliza a plataforma Twilio para enviar mensagens SMS e WhatsApp.
   - As credenciais da conta Twilio (SID e token de autenticação) são armazenadas de forma segura e utilizadas para enviar mensagens.

4. Rastreamento do Status das Mensagens:
   - O projeto deve rastrear o status das mensagens enviadas para os clientes, para verificar se foram entregues com sucesso ou se ocorreram falhas de entrega.

## Arquitetura do Projeto
O projeto é implementado em Python e consiste em vários módulos interconectados. A seguir, descrevemos os principais componentes:

### `user_product.py`
Este módulo contém as classes essenciais para o projeto:

- `Product`: Representa um produto no carrinho, com atributos como nome, preço, data e hora de adição, quantidade e link para o produto.
- `User`: Representa um cliente, com atributos como número de telefone, endereço de e-mail e uma lista de produtos no carrinho.
   - `addProduct()`: Método para adicionar produtos ao carrinho do cliente.
   - `sendSMS()`: Método para enviar mensagens SMS para o cliente com informações sobre os produtos no carrinho.
   - `sendWhatsappMessage()`: Método para enviar mensagens via WhatsApp para o cliente.

### `tokens.py`
Este arquivo armazena as credenciais da conta Twilio, incluindo o `account_sid` e o `auth_token`.

### `main.py`
Este é o ponto de entrada do projeto. Ele realiza as seguintes tarefas:

- Recupera os dados dos carrinhos abandonados de um arquivo chamado `carts.txt`.
- Para cada carrinho abandonado, cria uma instância de `User` e adiciona os produtos ao carrinho do cliente.
- Envia mensagens SMS e WhatsApp para cada cliente com produtos no carrinho abandonado.

## Executando o Projeto
Para executar o projeto, siga as etapas abaixo:

1. Clone este repositório do GitHub para o seu ambiente de desenvolvimento.

2. Certifique-se de ter as bibliotecas Python necessárias instaladas. Você pode usar `pip` para instalar as dependências:
   
   ```bash
   pip install twilio requests
   ```

3. Crie um arquivo `carts.txt` com os dados dos carrinhos abandonados no formato especificado.

4. Edite o arquivo `tokens.py` e insira suas próprias credenciais Twilio.

5. Execute o arquivo `main.py` para iniciar o processo de envio de mensagens.

## Conclusão
Este projeto fornece uma solução para recuperar carrinhos abandonados e aumentar as vendas de uma loja virtual. A comunicação personalizada por meio de mensagens SMS e WhatsApp pode ser eficaz para incentivar os clientes a retornar e concluir suas compras. Certifique-se de adaptar o projeto às necessidades específicas da sua loja virtual e de seguir as diretrizes de privacidade e regulamentação ao lidar com os dados dos clientes.
