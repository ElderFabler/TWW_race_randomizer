from PyQt5 import QtWidgets, QtCore
from randomizer import rand_it
import time

class RandWindow(QtWidgets.QWidget):
    def __init__(self):
        #QtWidgets.QWidget.__init__(self,parent = None)
        super().__init__()

        self.lords_list = [
        "Тирион","Теклис","Алариэль Сияющая","Алит Анар","Эльтарион","Имрик",
        "Лорд Маздамунди","Крок-Гар","Техенхауин","Тиктак'то","Накай Скиталец","Гор-Рок","Оксиотль",
        "Малекит","Морати","Ведьма Хеллеброн","Локхир Жесткосердный","Малус Тёмный Клинок","Ракарт",
        "Квик Головогрыз","Лорд Скролк","Третч Подлый Хвост","Икит Клешня","Мастер смерти Сникч","Трот Нечистый",
        "Лютор Гаркон","Граф Ноктил","Аранесса Солёная Ярость","Килостра Плавник",
        "Сеттра Бессмертный","Верховный жрец Хатеп","Верховная царица Халида","Архан Чёрный",
        "Император Карл Франц","Фолькмар Мрачный Лик","Бальтазар Гельт","Марк Вульфхарт",
        "Торгрим Злопамятный","Громбриндал - Белый Гном","Белегар Железный Молот","Унгрим Железный Кулак","Торгрим Железнобров",
        "Гримгор Железношкур","Скарсник","Вуррзаг Великий Зелёный пророк","Гром Пузан","Ажаг Мясник",
        "Манфред фон Карштайн","Хельман Горст","Влад фон Карштайн","Изабелла фон Картайн","Генрих Кеммлер",
        "Вульфрик Странник","Трогг",
        "Луан Леонкур","Альберик из Бордело","Фея-заклинательница","Рапанс де Лионесс",
        "Орион","Дуртху","Сёстры Сумерек","Дрича",
        "Харзрак Одноглазый","Малагор Тёмный Предвестник","Моргур Тенедар","Таврокс Медный Бык",
        "Архаон Навеки Избранный","Холек Солнцеед","Князь Зигвальд Великолепный",
        "Скарбранд","Н'Кари","Ку'Гат","Кайрос","Мяо Ин","Джао Мин","Гризус Златозуб","Скраг Мясник",
        "Царица Катарина", "Великий патриарх Косталтын","Борис Урсус","Белакор","Валькия Кровавая",
        "Фестус Повелитель Пиявок","Вилитч Проклятый","Азазель Князь Проклятий","Алкалуропс Богоубийца",
    ]

        self.modal_wind = ModalWind(self)

        self.but_choose_list = QtWidgets.QPushButton("Choose your lords list")
        self.but_choose_all = QtWidgets.QPushButton("Choose from all")
        self.but_close = QtWidgets.QPushButton("Close")
        self.label = QtWidgets.QLabel("Press button")

        self.but_choose_list.setFixedSize(250,50)
        self.but_choose_all.setFixedSize(250,50)
        self.but_close.setFixedSize(250,50)

        self.setStyleSheet(
            "QPushButton {font-family: 'Courier New', monospace; font: bold; font-size: 16px;}\
                QLabel {font-family: 'Courier New', monospace; font: bold; font-size: 16px;}\
                    QCheckBox {font-family: 'Courier New', monospace; font: bold; font-size: 14px;}\
                        QToolBox::tab {font-family: 'Courier New', monospace; font: bold; font-size: 16px;}"
        )

        glout = QtWidgets.QGridLayout()
        vlout_choose = QtWidgets.QVBoxLayout()

        vlout_choose.addWidget(self.but_choose_list)
        vlout_choose.addWidget(self.but_choose_all)
        #vlout.addWidget(self.but_close)
        glout.addLayout(vlout_choose,0,0,alignment = QtCore.Qt.AlignVCenter)
        glout.addWidget(self.label,1,0,alignment = QtCore.Qt.AlignHCenter)
        glout.addWidget(self.but_close,2,0,alignment = QtCore.Qt.AlignBottom)
        self.setLayout(glout)

        self.but_choose_all.clicked.connect(self.choose_from_all)
        self.but_choose_list.clicked.connect(self.modal_wind.show)
        self.but_close.clicked.connect(app.quit)

    def choose_from_all(self):
        lord_is = rand_it(self.lords_list)
        self.label.setText(lord_is)

    

class ModalWind(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)        

        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setWindowTitle("Choose your lords!")

        self.main = parent
        self.lords_dict = {
            "Высшые эльфы":["Тирион","Теклис","Алариэль Сияющая","Алит Анар","Эльтарион","Имрик",],
            "Людоящеры":["Лорд Маздамунди","Крок-Гар","Техенхауин","Тиктак'то","Накай Скиталец","Гор-Рок","Оксиотль",],
            "Тёмные эльфы":["Малекит","Морати","Ведьма Хеллеброн","Локхир Жесткосердный","Малус Тёмный Клинок","Ракарт",],
            "Скавены":["Квик Головогрыз","Лорд Скролк","Третч Подлый Хвост","Икит Клешня","Мастер смерти Сникч","Трот Нечистый",],
            "Цари гробниц":["Сеттра Бессмертный","Верховный жрец Хатеп","Верховная царица Халида","Архан Чёрный",],
            "Берег вампиров":["Лютор Гаркон","Граф Ноктил","Аранесса Солёная Ярость","Килостра Плавник"],
            "Империя":["Император Карл Франц","Фолькмар Мрачный Лик","Бальтазар Гельт","Марк Вульфхарт",],
            "Гномы":["Торгрим Злопамятный","Громбриндал - Белый Гном","Белегар Железный Молот","Унгрим Железный Кулак","Торгрим Железнобров",],
            "Зеленокожие":["Гримгор Железношкур","Скарсник","Вуррзаг Великий Зелёный пророк","Гром Пузан","Ажаг Мясник",],
            "Графства вампирова":["Манфред фон Карштайн","Хельман Горст","Влад фон Карштайн","Изабелла фон Картайн","Генрих Кеммлер",],
            "Норска":["Вульфрик Странник","Трогг",],
            "Бретония":["Луан Леонкур","Альберик из Бордело","Фея-заклинательница","Рапанс де Лионесс",],
            "Лесные эльфы":["Орион","Дуртху","Сёстры Сумерек","Дрича",],
            "Зверолюды":["Харзрак Одноглазый","Малагор Тёмный Предвестник","Моргур Тенедар","Таврокс Медный Бык",],
            "Кислев":["Царица Катарина", "Великий патриарх Косталтын","Борис Урсус",],
            "Великий Катай":["Мяо Ин","Джао Мин",],
            "Королевства огров":["Гризус Златозуб","Скраг Мясник",],
            "Какие-то хаоситы":[
                "Архаон Навеки Избранный","Холек Солнцеед","Князь Зигвальд Великолепный","Скарбранд",
                "Н'Кари","Ку'Гат","Кайрос","Белакор","Валькия Кровавая","Фестус Повелитель Пиявок",
                "Вилитч Проклятый","Азазель Князь Проклятий","Алкалуропс Богоубийца",
            ],
        }

        self.label = QtWidgets.QLabel("Open tabs and choose")
        self.but_confirm = QtWidgets.QPushButton("Confirm")
        self.but_close = QtWidgets.QPushButton("Close")

        gridout = QtWidgets.QGridLayout()
        count = 0
        for i in list(self.lords_dict.keys()):
            if count % 6 == 0:
                self.toolbox = QtWidgets.QToolBox()
                gridout.addWidget(self.toolbox,0,count // 6)
            else:
                pass
            w = QtWidgets.QWidget()
            wvlout = QtWidgets.QVBoxLayout()
            for j in self.lords_dict[i]:
                radio = QtWidgets.QCheckBox(j)
                wvlout.addWidget(radio)
            w.setLayout(wvlout)
            self.toolbox.addItem(w,i)
            self.toolbox.setCurrentIndex(99)
            count += 1

        hlout = QtWidgets.QHBoxLayout()
        hlout.addWidget(self.but_confirm)
        hlout.addWidget(self.but_close)

        self.vlout = QtWidgets.QVBoxLayout()
        self.vlout.addWidget(self.label)
        self.vlout.addLayout(gridout)
        self.vlout.addLayout(hlout)

        self.setLayout(self.vlout)

        self.but_confirm.clicked.connect(self.check_it)
        self.but_close.clicked.connect(self.close)

    def check_it(self):
        self.user_list = []
        for i in range(0,self.vlout.itemAt(1).columnCount()):
            for j in range(0,self.vlout.itemAt(1).itemAtPosition(0,i).widget().count()):
                item = self.vlout.itemAt(1).itemAtPosition(0,i).widget().widget(j).layout()
                for k in range(0,item.count()):
                    box = item.itemAt(k).widget()
                    if box.isChecked():
                        self.user_list.append(box.text())
                    else:
                        pass
        if self.user_list == []:
            self.main.label.setText("Empty lords list")
            self.close()
        else:
            lord_is = rand_it(self.user_list)
            self.main.label.setText(lord_is)
            self.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    win = RandWindow()
    win.setWindowTitle("Choose your lord!")
    win.resize(250,250)
    win.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)


    win.show()

    sys.exit(app.exec_())