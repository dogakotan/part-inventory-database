from PyQt5 import uic

with open("customer.py","w",encoding="utf-8") as fout:
    uic.compileUi("sqlproject.ui",fout)