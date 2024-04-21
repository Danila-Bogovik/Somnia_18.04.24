Чтобы запустить сайт нужно распаковать репозиторий на хостинг вместе со всеми файлами. Затем нужно установить все зависимости (есть в requirements.txt). Запуск осуществляется через app.py файл. Также нужно указать параметры:

Настройки Google Сloud:

  Authorized JavaScript origins:
  
    https://domain.ex
    
  Authorized redirect URIs:
  
    https://domain.ex/login/callback

Также необходимо заполнить в app.py:

GOOGLE_CLIENT_ID = "Client ID",

GOOGLE_CLIENT_SECRET = "Client secret",

