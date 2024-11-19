# Sistema de Gerenciamento de Biblioteca  

Este projeto foi desenvolvido para gerenciar uma biblioteca, permitindo a administração de livros, autores e categorias. Utiliza o framework Django e Django REST Framework para criar uma API RESTful robusta e escalável.

---

## Funcionalidades  

- **Gerenciamento de Livros**: Criação, leitura, atualização e exclusão de livros.  
- **Gerenciamento de Autores**: Criação, leitura, atualização e exclusão de autores.  
- **Gerenciamento de Categorias**: Criação, leitura, atualização e exclusão de categorias.  
- **API REST Documentada**: Documentação interativa para acesso às funcionalidades da API.  

---

## Dependências  

O projeto utiliza as seguintes bibliotecas e ferramentas:  

- **asgiref==3.8.1**  
- **attrs==24.2.0**  
- **Django==5.1**  
- **django-cors-headers==4.6.0**  
- **django-filter==24.3**  
- **djangorestframework==3.15.2**  
- **drf-spectacular==0.27.2**  
- **drf-yasg==1.21.8**  
- **inflection==0.5.1**  
- **jsonschema==4.23.0**  
- **jsonschema-specifications==2024.10.1**  
- **packaging==24.2**  
- **pytz==2024.2**  
- **PyYAML==6.0.2**  
- **referencing==0.35.1**  
- **rpds-py==0.21.0**  
- **sqlparse==0.5.1**  
- **tzdata==2024.1**  
- **uritemplate==4.1.1**  

---

## Instalação  

## Pré-requisitos

- **Python 3.8+**
- **pip** (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Snolaxluna/biblioteca-django
   cd Django-api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```
