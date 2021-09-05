# projeto-agenda
Código referente ao mini curso Desenvolvimento Web com Django da DIO (Digital Inovation One)

Para utilizar esse projeto você precisa:

* Ter o <a href="https://www.python.org/downloads/">Python</a> instalado (versão 3.*)

* Instalar os pacotes:
  
  1. pip install virtualenv
    
      1. após instalar abra a pasta no terminal
    
      2. crie um ambiente virtual: python  -m venv env . (windows)
    
      3. ative: env\scripts\activate
    
  
  2. pip install django (no terminal)
  
      1. python manage.py makemigrations
      
      2. python manage.py migrate
      
      3. python manage.py runserver
      
Após os passos acima acesse <a href="http://127.0.0.1:8000/agenda/">Link</a> 

Para carregar arquivos staticos:

1. salve o arquivo na pasta core/static
  
  1. para utilizar nos arquivos HTML: <link rel="stylesheet" type="text/css" href="{% static "base.css" %}">
  
  2. para imagens: <img src="{% static "base.png" %}">
  


