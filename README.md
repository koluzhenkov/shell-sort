### Требования:

[Python](https://www.python.org/) версии 3.8 или выше  
[allure-commandline](https://docs.qameta.io/allure/#_installing_a_commandline) для генерации и просмотра отчета

### Установка
```
git clone https://github.com/koluzhenkov/shell-sort.git
cd 
pip install -r requirements.txt
```
### Запуск приложения
```
python application.py
```
или
```
python application.py --array={числа через запятую}
```

### Запуск тестов
```
python -m pytest --alluredir=reports
```
Для генерации и просмотра html-отчета:  
```allure serve reports```
