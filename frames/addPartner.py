from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QPushButton,
    QLabel,
    QLineEdit
)

from frames import messageBox
from frames import partners

class interface_reg_parther(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()

        self.setLayout(self.widgets_layout_conainer)

    def update_start_values(self):
        self.widgets_layout_conainer = QVBoxLayout()

        self.widgets_layout_conainer.addWidget(QLabel("Введите имя"))
        self.input_partner_name = self.create_patern_QLineEdit("Строим Селим Выживаем")

        self.widgets_layout_conainer.addWidget(QLabel("Введите тип партнера (ООО, ОАО, ПАО, ЗАО)"))
        self.input_partner_type = self.create_patern_QLineEdit("ООО")
        self.input_partner_type.setMaxLength(3)

        self.widgets_layout_conainer.addWidget(QLabel("Введите имя директора"))
        self.input_partner_director = self.create_patern_QLineEdit("Ввод имени директора")

        self.widgets_layout_conainer.addWidget(QLabel("Введите телефон (в формате +7 xхх ххх хх хх)"))
        self.input_partner_phone = self.create_patern_QLineEdit("+7 999 777 66 55")
        self.input_partner_phone.setMaxLength(16)

        self.widgets_layout_conainer.addWidget(QLabel("Введите почту (в формате example@mail.ru)"))
        self.input_partner_mail = self.create_patern_QLineEdit("example@mail.ru")

        self.widgets_layout_conainer.addWidget(QLabel("Введите юридический адрес (в формате XXXXXX, Ленинградская область, город Приморск, ул. Парковая, 21)"))
        self.input_partner_ur_addr = self.create_patern_QLineEdit("188910, Ленинградская область, город Приморск, ул. Парковая, 21")

        self.widgets_layout_conainer.addWidget(QLabel("Введите инн (в формате XXXXXXXXXX)"))
        self.input_partner_inn = self.create_patern_QLineEdit("7656478391")
        self.input_partner_inn.setMaxLength(10)

        self.widgets_layout_conainer.addWidget(QLabel("Введите рейтинг (X)"))
        self.input_partner_rate = self.create_patern_QLineEdit("9")
        self.input_partner_rate.setMaxLength(2)

        self.btn_add_partner_to_db = QPushButton("Добавить партнера")
        self.btn_add_partner_to_db.clicked.connect(self.add_partner_to_db)
        self.widgets_layout_conainer.addWidget(self.btn_add_partner_to_db)

        self.back_brn = QPushButton("Назад")
        self.back_brn.clicked.connect(
            lambda: self.controller.switch_to_new_frame(partners.interface)
        )
        self.widgets_layout_conainer.addWidget(self.back_brn)

    def create_patern_QLineEdit(self, placeholder_text):
        input_text = QLineEdit()
        input_text.setPlaceholderText(placeholder_text)
        self.widgets_layout_conainer.addWidget(input_text)
        return input_text

    def create_text_enter_hint(self, hint_message: str):
        hint = QLabel(hint_message)
        hint.setObjectName("text_enter_hint")
        self.widgets_layout_conainer.addWidget(hint)

    def add_partner_to_db(self):
        partner_dict_data : dict = {
            "name": self.input_partner_name.text(),
            "type": self.input_partner_type.text(),
            "director": self.input_partner_director.text(),
            "phone": self.input_partner_phone.text()[3:],
            "mail": self.input_partner_mail.text(),
            "ur_addr": self.input_partner_ur_addr.text(),
            "inn": self.input_partner_inn.text(),
            "rate": self.input_partner_rate.text(),
        }
        if self.connection.partner_add_function(partner_dict_data):
            messageBox.send_info_message_box("Партнер успешно добавлен")
            return
        messageBox.send_info_message_box("Партнер не добавлен")
        return