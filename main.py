from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from customer import *

#-------------------------  PROJECT MEMBERS  ---------------------------
#- 22110002010 DOĞA BENGÜ KOTAN - 
#- 2110002025 ÇİSEM GÜRE --
#- 22110002024 MELİSA ŞENER --

#------------------------ Interface operations -------------------------

application = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_sqlproject()
ui.setupUi(window)
window.show()

#------------------------ Database operations -------------------------

import sqlite3

connection = sqlite3.connect("misproject.db")
process = connection.cursor()
connection.commit()



#--- Add / Show / Delete Records ---

ui.table.setHorizontalHeaderLabels(("CustomerID","Name Surname", "Address", "Phone", "E-mail"))

def add_record():
    customername = ui.line1.text()
    address = ui.line2.text()
    phone = ui.line3.text()
    email = ui.line4.text()
 
    try:
        insert = "INSERT INTO CUSTOMERS (customername, address, phone, email) VALUES (?, ?, ?, ?)"
        process.execute(insert, (customername, address, phone, email))  # Burada düzeltme yapıldı
        connection.commit()
        ui.statusbar.showMessage("Customer Added Successfully!", 10000)
        show_record()

    except Exception as e:
        ui.statusbar.showMessage(f"Error: {str(e)}", 10000)  # Hata mesajını daha ayrıntılı göster



def show_record():
    ui.table.clear()
    ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.table.setHorizontalHeaderLabels(("CustomerID","Name Surname", "Address", "Phone", "E-mail"))
    query = "select * from CUSTOMERS"
    process.execute(query)

    for indexLine, recordNum in enumerate(process):
        for indecxColumn, recordColumn in enumerate(recordNum):
            ui.table.setItem(indexLine,indecxColumn,QTableWidgetItem(str(recordColumn)))


def delete_record():
    delete_message = QMessageBox.question(window, "Delete Confirmation", "Are you sure you want to delete this record?", QMessageBox.Yes | QMessageBox.No)

    if delete_message == QMessageBox.Yes:
        selected_record = ui.table.selectedItems()
        selectDelete_record = selected_record[0].text()

        query = "DELETE FROM CUSTOMERS WHERE customerid = ?" 

        try:
            process.execute(query, (selectDelete_record,))
            connection.commit()
            ui.statusbar.showMessage("Customer Deleted Successfully!", 10000)
            show_record()
        except Exception as e:
            ui.statusbar.showMessage(f"Error: {str(e)}", 10000)

    else:
        ui.statusbar.showMessage("Transaction Cancelled!", 10000)


def search_query():
    """
    QUERY METHOD
    """



#--- Buttons ---
ui.button1.clicked.connect(add_record)
ui.button2.clicked.connect(delete_record)





show_record()

sys.exit(application.exec_())