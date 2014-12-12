web_4kurs
=========
Web4.sln - файл проекта для Visual Studio, необязателен.

Для развёртывания вебприложения требуется :

python 2.7 - https://www.python.org/downloads/
pip - https://pip.pypa.io/en/latest/installing.html
virtualenv(опционально) - https://pypi.python.org/pypi/virtualenv

Вебприложение находится в директории Web4/

Для вебприложения можно создать своё виртуальное окружение для питон:
python virtualenv.py flask

Чтобы установить нужные пакеты для запуска вебприложения следует выполнить команду:
pip install -r requirements.txt

Если используется virtualenv, то для Linux:


flask/bin/pip install -r requirements.txt

для Windows:

flask\Scripts\pip install -r requirements.txt

Для запуска локального сервера следует выполнить:

Для Linux(не тестировал, возможно следует изменить формат завершения строк во всех исходных файлах):

flask\bin\python runserver.py

Для Windows:

flask\Scripts\python.exe runserver.py

Далее в браузере следует набрать http://localhost:5555/

В папке tmp содержатся файлы, которые скорее всего не понадобятся впоследсвии.

http://web4kurs-fleytman.rhcloud.com/ - приложение на хостинге(пока не запущено)
