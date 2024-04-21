Чтобы запустить сайт нужно распаковать репозиторий на хостинг вместе со всеми файлами кроме файлов кэша. Затем нужно установить все зависимости (есть в requirements.txt) через bash консоль. Запуск осуществляется через main.py файл. Также нужно указать параметры в 

GOOGLE_CLIENT_ID = "",
GOOGLE_CLIENT_SECRET = "",
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration",
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db',
app.config['SECRET_KEY'] = "fdfhs34h23jbmbfg23b4jhfg",
context = ('certificate/cert.pem', 'certificate/private.key')
app.run(host='0.0.0.0', port='5000', ssl_context=context, debug=False)
