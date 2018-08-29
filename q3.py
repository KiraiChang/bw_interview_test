# -*- coding: utf-8 -*-
# Q1 2.x 預設的編碼是 ascii, 若是內含utf-8的內容則須加上述內容否則compiler會失敗
#    2.x 字串有兩種型態 1. aa='aa'一般字串; 2. aa=u'aa' unicode字串
#    unicode轉str => u'aaa'.encode('utf-8') -> 一般字串
#    str轉unicode => 'aaa'.decode('utf-8') -> unicode字串
# Q2 3.x 字串預設是unicode str不需要特別做轉換即可處理

# Q3 MVC structure
#   ~/largeApp
#       |-- run.py
#       |-- config.py
#       |--/venv
#       |--/app
#           |-- __init__.py
#           |-- /mod_1
#               |-- __init__.py
#               |-- controllers.py
#               |-- models.py
#               |-- forms.py
#           |-- /static
#               |-- style.css
#           |-- /templates
#               |-- layout.html
#               |-- index.html
#               |-- login.html
#               ...
#               |-- /temp_1
