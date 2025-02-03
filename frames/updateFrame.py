from PySide6.QtWidgets import (QLineEdit, QVBoxLayout, QLabel, QFrame, QPushButton)
from frames import partners, messageBox
import partnerStaticName

class UpdatePartnerFrame(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)

        self.controller = controller
        self.db_connection = controller.connection

        self.update_start_information()
        self.setLayout(self.main_layout)

    def update_start_information(self):
        self.main_layout = QVBoxLayout()

        self.title_add_window_name = QLabel(self)
        self.title_add_window_name.setText("Обновление данных о партнере")
        self.title_add_window_name.setObjectName("Title")
        self.main_layout.addWidget(self.title_add_window_name)

        self.single_partner_info = self.db_connection.take_current_partner_info(partnerStaticName.Partner.return_name())

        # Добавление объектов на Фрейм
        self.create_text_enter_hint("Имя партнера")
        self.partner_name_entry = self.create_line_pattern(self.single_partner_info[0]["name"])


        self.create_text_enter_hint("Юридический адрес партнера (в формате XXXXXX, Ленинградская область, город Приморск, ул. Парковая, 21)")
        self.partner_address_entry = self.create_line_pattern(self.single_partner_info[0]["ur_addr"])

        self.create_text_enter_hint("Телефон партнера (в формате +7 xхх ххх хх хх)")
        self.partner_phone_entry = self.create_line_pattern(self.single_partner_info[0]["phone"])
        self.partner_phone_entry.setMaxLength(13)
        self.partner_phone_entry.setInputMask("+7 000 000 00 00")

        self.create_text_enter_hint("Электронная почта партнера (в формате example@mail.ru)")
        self.partner_mail_entry = self.create_line_pattern(self.single_partner_info[0]["mail"])

        self.create_text_enter_hint("ИНН партнера (в формате XXXXXXXXXX)")
        self.partner_inn_entry = self.create_line_pattern(self.single_partner_info[0]["inn"])
        self.partner_inn_entry.setMaxLength(10)

        self.create_text_enter_hint("Рейтинг партнера (X)")
        self.partner_rate_entry = self.create_line_pattern(str(self.single_partner_info[0]["rate"]))
        self.partner_rate_entry.setMaxLength(2)

        self.create_text_enter_hint("Тип партнера (ООО, ОАО, ПАО, ЗАО)")
        self.partner_type_entry = self.create_line_pattern(self.single_partner_info[0]["type"])
        self.partner_type_entry.setMaxLength(3)

        self.create_text_enter_hint("Директор (в формате Фамилия Имя Отчество)")
        self.partner_director_entry = self.create_line_pattern(self.single_partner_info[0]["director"])

        self.add_btn = QPushButton("Обновить")
        self.add_btn.clicked.connect(
            self.func
        )
        self.main_layout.addWidget(self.add_btn)


        self.back_brn = QPushButton("Назад")
        self.back_brn.clicked.connect(
            lambda : self.controller.switch_to_new_frame(partners.interface)
        )

        self.main_layout.addWidget(self.back_brn)

    def create_line_pattern(self, placeholder_text):
        input_text = QLineEdit()
        input_text.setText(placeholder_text)
        self.main_layout.addWidget(input_text)
        return input_text

    def create_text_enter_hint(self, hint_message: str):
        ''' Создание подсказки для ввода текста '''
        hint = QLabel(hint_message)
        hint.setObjectName("text_enter_hint")
        self.main_layout.addWidget(hint)


    def func(self):
        partner_dict_data: dict = {
            "type": self.partner_type_entry.text(),
            "name": self.partner_name_entry.text(),
            "director": self.partner_director_entry.text(),
            "mail": self.partner_mail_entry.text(),
            "phone": self.partner_phone_entry.text()[3:],
            "ur_addr": self.partner_address_entry.text(),
            "inn": self.partner_inn_entry.text(),
            "rate": self.partner_rate_entry.text(),
        }
        if self.db_connection.update_partner_info_func(partnerStaticName.Partner.return_name(), partner_dict_data):
            messageBox.send_info_message_box("Данные о партнере обновлены")
            return
        messageBox.send_info_message_box("Данные о партнере не обновлены")
        return