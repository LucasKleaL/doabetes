from PyQt5 import uic, QtWidgets
import sqlite3

banco = sqlite3.connect('cadastroProdutos.db')

cursor = banco.cursor()

def funcao_principal():
    if formulario.queroReceber.isChecked():
        print("O usuario deseja receber ")
        if formulario.checkBox_7.isChecked():
            print('Aparelho medidor de glicose')
        if formulario.checkBox_8.isChecked():
            print('Tiras para medir glicose')
        if formulario.checkBox_9.isChecked():
            print('Insulina')
        if formulario.checkBox_11.isChecked():
            print('Canetas de aplicação de insulina')
        if formulario.checkBox_10.isChecked():
            print('Seringas de aplicação')
        if formulario.checkBox_12.isChecked():
            print('Insumos de bomba de infusão')


    elif formulario.queroDoar.isChecked():
        print("O usuario deseja doar ")
        if formulario.checkBox.isChecked():
            print('Aparelho medidor de glicose')
        if formulario.checkBox_2.isChecked():
            print('Tiras para medir glicose')
        if formulario.checkBox_3.isChecked():
            print('Insulina')
        if formulario.checkBox_4.isChecked():
            print('Canetas de aplicação de insulina')
        if formulario.checkBox_5.isChecked():
            print('Seringas de aplicação')
        if formulario.checkBox_6.isChecked():
            print('Insumos de bomba de infusão')

    elif formulario.queroDoarEReceber.isChecked():
        print("O usuario deseja doar")
        if formulario.checkBox.isChecked():
            print('Aparelho medidor de glicose')
        if formulario.checkBox_2.isChecked():
            print('Tiras para medir glicose')
        if formulario.checkBox_3.isChecked():
            print('Insulina')
        if formulario.checkBox_4.isChecked():
            print('Canetas de aplicação de insulina')
        if formulario.checkBox_5.isChecked():
            print('Seringas de aplicação')
        if formulario.checkBox_6.isChecked():
            print('Insumos de bomba de infusão')

        print('O usuario deseja receber:')
        if formulario.checkBox_7.isChecked():
            print('Aparelho medidor de glicose')
        if formulario.checkBox_8.isChecked():
            print('Tiras para medir glicose')
        if formulario.checkBox_9.isChecked():
            print('Insulina')
        if formulario.checkBox_11.isChecked():
            print('Canetas de aplicação de insulina')
        if formulario.checkBox_10.isChecked():
            print('Seringas de aplicação')
        if formulario.checkBox_12.isChecked():
            print('Insumos de bomba de infusão')




app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario2.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()