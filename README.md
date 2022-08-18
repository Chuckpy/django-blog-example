# Blog APP

- [Blog APP](#chalenge-app)
  - [Objetivo](#objetivo)
  - [Principais Caracteristicas](#principais-caracteristicas)
  - [Principais Funcionalidades](#principais-funcionalidades)
  - [Como Utilizar](#como-utilizar)
    - [Base URL](#base-url)
    - [Não é preciso usar o navegador!](#não-é-preciso-usar-o-navegador)
    - [Autenticação](#autenticação)
      - [Register](#register)
      - [Login](#login)
    - [Postagens](#postagens)
      - [Listagem](#listagem)
      - [Criar](#criar)

## Objetivo

O desafio do projeto foi criar um blog ficticio com retornos em JSON em apis RESTFUL, objetos de serialização aninhados e um esquema de autênticação simples.

## Principais Caracteristicas

- Fácil Entendimento e Adaptação
- Fácil Escalabilidade
- Resistente a possíveis falhas

### Não é preciso usar o navegador!

Caso possua o Insomnia, basta importar o pacote de requisições pelo imnsonia, o nome do arquivo para importar é 'challenge_insomnia.json' esta nesse mesmo repositório, nos documentos git.

### Autenticação

Aqui estão os usuários do banco dedados, que são usados para autenticação do projeto.

#### Register 

`POST users/`

```json
{
	"email":"email@email.com",
	"password":"password",
	"first_name":"first_name",
    "last_name":"last_name"    
}
```
***response :***
```json
{
	"email":"email@email.com",
	"password":"password",
	"first_name":"first_name",
    "last_name":"last_name",
    "is_active":true
}
```

#### Login

`POST users/token/`

***payload :***

```json
{
	"email":"email@email.com",
	"password":"password"
}

```

***response :***
```json
{
	"refresh": "refresh_token",
	"access": "access_token"
}
```

### Postagens

A ideia do projeto é que poder criar publicações a partir de um usuário autenticado no projeto.

#### Listagem 

`GET /`

Essa api é uma simples listagem com um paginamento, pode ser paginada usando query params "pages=<numero_da_pagina>"

***response*** :

```json
{
  "count": 99,
  "next": <url da prox pagina>,
  "previous": <url da pagina anterior>,
  "results": [
   {
        "author": 2,
        "title": "Title",
        "subtitle": "SubTitle",
        "type": 1,
        "content": "Content",
        "status": true,
        "keywords_set": [
            {
                "name": "Nome"
            },
            {
                "name": "Nome"
            }
        ]
    },
            . . .
  ]
}
```

#### Criar

`POST /`

Api feita para criar os objetos de publicação.

***payload*** :

```json
   {
        "author": 2,
        "title": "Title",
        "subtitle": "SubTitle",
        "type": 1,
        "content": "Content",
        "status": true,
        "keywords_set": [
            {
                "name": "Nome"
            },
            {
                "name": "Nome"
            }
        ]
    }
```


***response*** :

```json

{
	"success": true,
	"data":  {
        "author": 2,
        "title": "Title",
        "subtitle": "SubTitle",
        "type": 1,
        "content": "Content",
        "status": true,
        "keywords_set": [
            {
                "name": "Nome"
            },
            {
                "name": "Nome"
            }
        ]
    }
}

```
