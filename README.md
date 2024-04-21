Чтобы запустить сайт нужно распаковать репозиторий на хостинг вместе со всеми файлами кроме файлов кэша. Затем нужно установить все зависимости (есть в requirements.txt) через bash консоль. Запуск осуществляется через main.py файл. Также нужно указать параметры в 

Настройки Пoogle Сloud:

  Authorized JavaScript origins:
  
    https://domain.ex
    
  Authorized redirect URIs:
  
    https://domain.ex/login/callback

Также необходимо заполнить в app.py:

GOOGLE_CLIENT_ID = "Client ID",

GOOGLE_CLIENT_SECRET = "Client secret",

