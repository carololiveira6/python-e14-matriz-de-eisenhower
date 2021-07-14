## **Table of Contents**
- [E14 - Makriz de Eisenhower](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj10) 
  - [Objetivos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj11)
- [Diagrama de Relacionamentos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj12)
- [Rotas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj13) 
  - [POST /category](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj14) 
    - [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj15)
  - [POST /task](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj16) 
    - [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj17)
  - [POST /task_category](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj18) 
    - [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86d2pj19)
  - [GET /](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1f86e7suc0)
- [Entregáveis ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1egvoav555j)
  - [Repositório ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/4b_e_01_eisenhower.html&ref=master#mcetoc_1eh146n6m3)
# **E14 - Makriz de Eisenhower**
Nessa entrega você deverá criar uma aplicação que irá te ajudar a definir suas prioridades se baseando na matriz de Eisenhower.

![The eisenhower matrix](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.001.png)


## **Objetivos**
Praticar os conhecimentos em Flask (fazendo a criação de rotas), Flask-SQLAlchemy (fazendo criação de models e query com as mesmas), Flask-Migrate(fazendo a criação das tabelas no banco de dados e dando upgrade nelas), Blueprints e o design patter Flask Factory.


# **Diagrama de Relacionamentos**
Você deverá criar suas tabelas seguindo o diagrama abaixo:

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)


# **Rotas**
## **POST /category**
Deverá fazer a inserção dos dados na tabela **categories**:
### **Entradas e saídas**
Requisição no Insominia

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

Dado no banco de dados

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)





**Nota**: O status de retorno deve ser **201 CREATED**.
## **POST /task**
Deverá fazer a inserção dos dados na tabela **tasks**.

**importance**: se baseando na matriz de Eisenhower, só podemos ter 2 níveis de **importance**, sendo **important** ou **not important**, vamos numerá-los da seguinte forma, 1 para **important** e 2 para **not important**.

**urgency**: se baseando na matriz de Eisenhower, só podemos ter 2 níveis de **urgent**, sendo **urgent** ou **not urgent**, vamos numerá-los da seguinte forma, 1 para **urgent** e 2 para **not urgent**.



Agora que temos as descrições de **importance** e **urgency**, vamos seguir o seguinte padrão:

|importance: 1, urgency: 1|importance: 1, urgency: 2|importance: 2, urgency: 1|importance: 2, urgency: 2|
| :-: | :-: | :-: | :-: |
|Do It First|Delegate It|Schedule It|Delete It|


Você **DEVERÁ** criar uma lógica que dependendo do padrão recebido ele vai buscar na tabela de Eisenhower o tipo correto.

**Observação**: Os tipos da tabela de Eisenhower deverá ser colocado **MANUALMENTE** seja por uma service utilizando o psycopg2 ou diretamente no DBeaver, **NÃO** deverá existir uma rota para isso. 
### **Entradas e saídas**
Requisição no insominia

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

Dado no banco de dados

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

**Nota**: O status de retorno deve ser **201 CREATED**.



Caso passem um número maior que 2 você deverá fazer um tratamento:

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

**Nota**: O status de retorno deve ser **404 BAD REQUEST**.


## **POST /task\_category**
Deverá fazer a inserção dos dados na tabela **tasks\_categories**:
### **Entradas e saídas**
Requisição no insomnia

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

Dado no banco de dados

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

**Nota**: O status de retorno deve ser **201 CREATED**.


## **GET /**
Deverá ter o seguinte retorno:

![](Aspose.Words.d0a796b7-aa68-4f93-b53b-2bc49f1bd9ad.002.png)

**Nota**: O status de retorno deve ser **200 OK**.

**Observação**: O retorno **DEVE** ser uma lista de dicionários.

-----
# **Entregáveis** 
## **Repositório** 
- Link do **repositório** do **GitLab** 
- **Código fonte:** 
  - Pasta app. 
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter. 
### -----
# **Critérios de aceitação** 

|**Pts** |**Dado** |**Quando** |**É esperado** |
| :-: | :-: | :-: | :-: |
|2|diagrama|verificado as relacoes|seguir o que foi pedido|
|1|rota /category|feito a requisição|seguir o que foi pedido|
|3|rota /task|feito a requisição|seguir o que foi pedido|
|1|rota /task\_categorie|feito a requisição|seguir o que foi pedido|
|1|rota /|feito a requisição|seguir o que foi pedido|
|2|requirements e .env|clonado o repositorio|que os arquivos existam|


**Boa diversão! 😉**


