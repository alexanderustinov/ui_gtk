## ui_gtk
Проект рождён из [примера](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_gtk4_sgskip.html) и 
дополнен преимущественным применением наследования

### Для работы
Используется pygobject, нужно его установить в соответствии с [инструкцией](https://pygobject.readthedocs.io/en/latest/getting_started.html).  
Так как в последней предлагается устанавливать программы в систему, проще всего работать, используя системный 
интерпретатор (а не venv или подобное). Для этого при создании проекта нужно этот интерпретатор выбрать (при работе
на windows путь к нему, вероятно, `C:\msys64\mingw64\bin\python.exe`)

При таком способе работы установку пакетов нужно делать используя тот менеджер пакетов, который вы использовали при 
установке pygobject. Это значит, что в windows стоит использовать pacman внутри mingw64-консоли msys ([краткая 
инструкция про работу с пакетами](https://www.msys2.org/docs/package-management/))  

Программа использует matplotlib, поэтому его тоже надо установить (для windows - `pacman -S mingw-w64-python-matplotlib`)

### Запуск
Запуск подразумевает выполнение модуля 
```shell
python3 -m gtk_proj 
```

На windows шелл pycharm в первую очередь "видит" python не из msys, поэтому запуск ломается об
ошибку импорта gi. Самый простой способ этого избежать - настроить конфигурацию запуска: слева от 
Run в интерфейсе, собирать по словам python, module (по запросу сниму видео-урок про это; повтор того, что было на паре) 

### Nuitka
Требует установки `mingw-w64-x86_64-python-nuitka` и использования
python из msys:
```shell
 C:\msys64\mingw64\bin\python.exe -m nuitka gtk_proj_.py 
--standalone --onefile --include-data-files=gtk_proj/default_config.toml=gtk_proj/de
fault_config.toml
```
20231204: пока (nuitka 1.8.3-1 и nuitka factory) запускается только в присутствии
msys в PATH (иначе не находит кусочки gtk4). Для gtk3 должно
работать (см. https://github.com/Nuitka/Nuitka/issues/2471 )