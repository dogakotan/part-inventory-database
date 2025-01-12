#include "sqlproject.h"
#include "ui_sqlproject.h"

sqlproject::sqlproject(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::sqlproject)
{
    ui->setupUi(this);
}

sqlproject::~sqlproject()
{
    delete ui;
}
