# Link Shortener API

API REST desenvolvida com Django, Django REST Framework (DRF), Python e PostgreSQL para encurtamento e redirecionamento de URLs.

## Sobre o Projeto

A Link Shortener API é uma aplicação backend responsável por receber uma URL, gerar um identificador curto e permitir o redirecionamento para o endereço original.

O projeto foi construído utilizando Django e DRF para estruturação da API e PostgreSQL como banco de dados relacional.

## Tecnologias Utilizadas

- Python  
- Django  
- Django REST Framework (DRF)  
- PostgreSQL  

## Funcionamento

A API recebe uma URL, valida os dados, gera um código curto e salva essa relação no banco de dados. Quando o código curto é acessado, a aplicação busca a URL correspondente e realiza o redirecionamento para o endereço original.

## Endpoints

Os endpoints estão organizados em dois grupos principais: autenticação e encurtamento de URLs.

### Encurtamento de URL

POST /short/url/  
Cria uma nova URL encurtada (requer autenticação).

GET /short/<link_id>/  
Redireciona para a URL original associada ao identificador.

### Autenticação

POST /account/register/  
POST /account/login/  
POST /account/logout/  

POST /account/password/change/  
POST /account/password/change/request/  
POST /account/password/change/forgot/

## Objetivo

Projeto desenvolvido para prática e consolidação de conceitos de desenvolvimento backend com Django, DRF e PostgreSQL.