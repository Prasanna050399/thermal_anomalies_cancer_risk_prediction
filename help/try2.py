from PyQt5.QtCore import QDate
from datetime import datetime, date

date = QDate.currentDate()
print(type(date), date)
date = date.toPyDate()
print(type(date), date)
date = str(date)
print(type(date), date)
