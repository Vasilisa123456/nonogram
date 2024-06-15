import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap


class nonogramm(QMainWindow):
    def __init__(self):
        super(nonogramm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Нонограмм")
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/главный экран.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание надписи нонограмм
        self.Main_nadpis1 = QLabel(self)
        self.Main_nadpis1.setText("Нонограмм")
        self.Main_nadpis1.setStyleSheet("font: 900 italic 50pt \"Arial\";\n" "color: rgb(0, 0, 0);")
        self.Main_nadpis1.setGeometry(230, 200, 500, 100)

        # Создание кнопки начала игры
        self.igrat = QtWidgets.QPushButton(self)
        self.igrat.setText("Начало")
        self.igrat.setStyleSheet("font: 75 italic 35pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.igrat.setGeometry(300, 350, 300, 80)
        self.igrat.clicked.connect(self.open_window9)

        # Настройки кнопки Выход
        self.end = QPushButton('Выход', self)
        self.end.setGeometry(300, 450, 300, 80)
        self.end.setStyleSheet("font: 75 italic 35pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.end.clicked.connect(self.close)

    # Создание нового окна с правилами, уровнями и кнопкой назад
    def open_window9(self):
        self.n_window = NoWindow(self)
        self.hide()
        self.n_window.show()


# создание окна главное меню


class NoWindow(QMainWindow):
    def __init__(self, no_window):
        super().__init__()
        self.setWindowTitle('Нонограмм')
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/главный экран.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание кнопки уровни игры
        self.igrat = QtWidgets.QPushButton(self)
        self.igrat.setText("Уровни")
        self.igrat.setStyleSheet("font: 75 italic 35pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.igrat.setGeometry(280, 250, 350, 80)
        self.igrat.clicked.connect(self.open_window2)

        # Настройка кнопки Правила
        self.prav = QPushButton('Правила игры ', self)
        self.prav.setGeometry(280, 390, 350, 80)
        self.prav.setStyleSheet("font: 75 italic 30pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.prav.clicked.connect(self.open_window)

        # Создание кнопки назад в окне уровни
        self.back = QPushButton('<', self)
        self.back.setGeometry(650, 650, 200, 70)
        self.back.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.back_open(no_window))

    def back_open(self, no_window):
        no_window.show()
        self.close()

    # Создание окна правила
    def open_window(self):
        self.one_window = OneWindow(self)
        self.hide()
        self.one_window.show()

    # Создание окна начала игры
    def open_window2(self):
        self.two_window = TwoWindow(self)
        self.hide()
        self.two_window.show()


# создание окна правила игры


class OneWindow(QMainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.setWindowTitle('Нонограмм')
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/правила игры.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание кнопки назад
        self.back = QPushButton('Назад', self)
        self.back.setGeometry(650, 690, 200, 70)
        self.back.setStyleSheet("font: 75 italic 35pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.back_open(first_window))

    def back_open(self, first_window):
        first_window.show()
        self.close()


# Создание окна уровни


class TwoWindow(QMainWindow):
    def __init__(self, second_window):
        super().__init__()
        self.setWindowTitle('Нонограмм')
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения окна начало
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/уровни.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание кнопки назад в окне уровни
        self.back = QPushButton('<', self)
        self.back.setGeometry(650, 650, 200, 70)
        self.back.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.back_open(second_window))

        # Создание кнопки уровень легкий в окне уровни
        self.level1 = QPushButton('Легкий', self)
        self.level1.setGeometry(100, 150, 250, 80)
        self.level1.setStyleSheet("font: 75 italic 35pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level1.clicked.connect(self.open3_window)

        # Создание кнопки уровень средний в окне уровни
        self.level2 = QPushButton('Средний', self)
        self.level2.setGeometry(310, 300, 250, 80)
        self.level2.setStyleSheet("font: 75 italic 35pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level2.clicked.connect(self.open4_window)

        # Создание кнопки уровень сложный в окне уровни
        self.level3 = QPushButton('Сложный', self)
        self.level3.setGeometry(480, 460, 250, 80)
        self.level3.setStyleSheet("font: 75 italic 33pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level3.clicked.connect(self.open5_window)

    def back_open(self, first_window):
        first_window.show()
        self.close()

    # Создание окна уровень 1
    def open3_window(self):
        self.level1_window = ThreeWindow(self)
        self.hide()
        self.level1_window.show()

    # Создание окна уровень 2
    def open4_window(self):
        self.level2_window = FourWindow(self)
        self.hide()
        self.level2_window.show()

    # Создание окна уровень 3
    def open5_window(self):
        self.level3_window = FiveWindow(self)
        self.hide()
        self.level3_window.show()


# Определение класса FiveWindow перед его использованием
# Создание сложного уровня
class FiveWindow(QMainWindow):
    def __init__(self, level3_window):
        super().__init__()
        self.setWindowTitle('Нонограмм')
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения окна уровень 3
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/3.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание кнопки назад в окне уровни
        self.back = QPushButton('<', self)
        self.back.setGeometry(600, 620, 250, 65)
        self.back.setStyleSheet("font: 75 italic 29pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.open_window(level3_window))

        # Создание кнопки проверки правильности заполнения поля
        self.check_button = QPushButton('Проверить', self)
        self.check_button.setGeometry(50, 620, 315, 65)
        self.check_button.setStyleSheet("font: 75 italic 29pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.check_button.clicked.connect(self.check_solution)

        # Создание поля 15x15 клеточек
        self.cells = [[QPushButton('', self) for _ in range(15)] for _ in range(15)]
        for i in range(15):
            for j in range(15):
                self.cells[i][j].setGeometry(230 + j * 30, 150 + i * 30, 30, 30)
                self.cells[i][j].setStyleSheet("background-color: white")
                self.cells[i][j].clicked.connect(lambda checked, x=i, y=j: self.change_color(x, y))

    def change_color(self, i, j):
        button = self.cells[i][j]
        if button.styleSheet() == "background-color: white":
            button.setStyleSheet("background-color: black")
        else:
            button.setStyleSheet("background-color: white")

    def check_solution(self):
        # Создание массива для хранения цветов клеточек
        colors = [[self.cells[i][j].styleSheet() == "background-color: black" for j in range(15)] for i in range(15)]

        # Правильное заполнение клеточек для уровня 3
        correct_colors = [
            [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, True, True, True, False, True, True, False],
            [False, False, True, False, False, False, False, True, True, False, True, True, True, False, False],
            [False, False, False, False, True, True, True, True, True, True, True, True, False, False, False],
            [False, False, False, False, False, False, False, False, False, True,  True, True, False, False, False],
            [False, False, False, False, False, False, False, True, True, True, True, True, False, True, True],
            [False, False, False, False, False, False, True, True, False, False, False, True, True, True, False],
            [False, False, False, False, False, False, False, True, True, True, True, True, True, True, True],
            [False, False, False, False, False, False, True, True, False, False, True, True, False, True, True],
            [False, False, False, False, False, False, False, True, True, True, False, True, False, False, False],
            [False, False, False, False, True, True, True, False, True, True, True, True, False, False, False],
            [False, False, False, True, True, False, True, False, False, True, True, True, False, False, False],
            [False, False, False, True, False, False, False, False, False, True, True, False, False, False, False],
            [False, False, False, True, True, False, False, False, True, True, True, False, False, False, False],
            [False, False, False, False, True, True, True, True, True, True, False, False, False, False, False]
        ]

        # Проверка правильности заполнения клеточек
        if colors == correct_colors:
            QMessageBox.about(self, 'Результат', 'Гений! Ты прошел сложный уровень)')
        else:
            QMessageBox.about(self, 'Результат', 'Поле заполнено не правильно!')

    def open_window(self, level3_window):
        level3_window.show()
        self.close()


# Создание легкого уровня


class ThreeWindow(QMainWindow):
    def __init__(self, level_window):
        super().__init__()
        self.setWindowTitle('Нонограмм')
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения окна уровень 1
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/3.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание кнопки назад в окне уровни
        self.back = QPushButton('<', self)
        self.back.setGeometry(600, 620, 250, 65)
        self.back.setStyleSheet("font: 75 italic 29pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.open_level_window(level_window))

        # Создание кнопки проверки правильности заполнения поля
        self.check_button = QPushButton('Проверить', self)
        self.check_button.setGeometry(50, 620, 315, 65)
        self.check_button.setStyleSheet("font: 75 italic 29pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.check_button.clicked.connect(self.check_solution)

        # Создание поля 5x5 клеточек
        self.cells = [[QPushButton('', self) for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.cells[i][j].setGeometry(270 + j * 70, 150 + i * 70, 70, 70)
                self.cells[i][j].setStyleSheet("background-color: white")
                self.cells[i][j].clicked.connect(lambda checked, x=i, y=j: self.change_color(x, y))

    def change_color(self, i, j):
        button = self.cells[i][j]
        if button.styleSheet() == "background-color: white":
            button.setStyleSheet("background-color: black")
        else:
            button.setStyleSheet("background-color: white")

    def check_solution(self):
        # Создание массива для хранения цветов клеточек
        colors = [[self.cells[i][j].styleSheet() == "background-color: black" for j in range(5)] for i in range(5)]

        # Правильное заполнение клеточек для уровня 3
        correct_colors = [
            [False, False, True, False, False],
            [False, True, True, False, False],
            [False, False, True, True, False],
            [False, False, True, True, True],
            [False, False, False, True, False]
        ]

        # Проверка правильности заполнения клеточек
        if colors == correct_colors:
            QMessageBox.about(self, 'Результат', 'Молодец! Легкий уровень пройден)')
        else:
            QMessageBox.about(self, 'Результат', 'Поле заполнено не правильно!')

    def open_level_window(self, level_window):
        self.close()  # Закрываем текущее окно
        level_window.show()  # Показываем окно уровней


# Создание среднего уровня


class FourWindow(QMainWindow):
    def __init__(self, level1_window):
        super().__init__()
        self.setWindowTitle('Нонограмм')
        self.setGeometry(550, 150, 900, 800)

        # Создание фонового изображения окна уровень 2
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qw/3.png"))
        self.background.setGeometry(0, 0, 900, 800)
        self.background.setScaledContents(True)

        # Создание кнопки назад в окне уровни
        self.back = QPushButton('<', self)
        self.back.setGeometry(600, 620, 250, 65)
        self.back.setStyleSheet("font: 75 italic 29pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.open_level_level_window(level1_window))

        # Создание кнопки проверки правильности заполнения поля
        self.check_button = QPushButton('Проверить', self)
        self.check_button.setGeometry(50, 620, 315, 65)
        self.check_button.setStyleSheet("font: 75 italic 29pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.check_button.clicked.connect(self.check_solution)

        # Создание поля 10x10 клеточек
        self.cells = [[QPushButton('', self) for _ in range(10)] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                self.cells[i][j].setGeometry(250 + j * 40, 150 + i * 40, 40, 40)
                self.cells[i][j].setStyleSheet("background-color: white")
                self.cells[i][j].clicked.connect(lambda checked, x=i, y=j: self.change_color(x, y))

    def change_color(self, i, j):
        button = self.cells[i][j]
        if button.styleSheet() == "background-color: white":
            button.setStyleSheet("background-color: black")
        else:
            button.setStyleSheet("background-color: white")

    def check_solution(self):
        # Создание массива для хранения цветов клеточек
        colors = [[self.cells[i][j].styleSheet() == "background-color: black" for j in range(10)] for i in range(10)]

        # Правильное заполнение клеточек для уровня 3
        correct_colors = [
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, True, True, False, True, False, False, False],
            [False, False, False, True, True, False, True, False, False, False],
            [False, False, True, True, True, False, True, True, False, False],
            [False, True, True, True, True, False, True, True, True, False],
            [True, True, True, True, True, False, True, True, True, True],
            [False, False, False, False, False, True, False, False, False, False],
            [False, True, True, True, True, True, True, True, True, False],
            [False, False, True, True, True, True, True, True, False, False]
        ]

        # Проверка правильности заполнения клеточек
        if colors == correct_colors:
            QMessageBox.about(self, 'Результат', 'Умничка! Ты справился с средним уровнем)')
        else:
            QMessageBox.about(self, 'Результат', 'Поле заполнено не правильно!')

    def open_level_level_window(self, level1_window):
        level1_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = nonogramm()
    main_window.show()
    sys.exit(app.exec_())
