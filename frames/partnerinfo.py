from PySide6.QtWidgets import (QVBoxLayout, QLabel, QFrame, QPushButton)
from frames import updateFrame, partners, getHistory
import partnerStaticName



class PartnerCardFullInfo(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)

        self.value_to_use_main_application_self = controller
        self.db_connect_values = controller.connection

        self.update_start_information()
        self.setLayout(self.main_layout)


    def update_start_information(self):
        self.main_layout = QVBoxLayout()

        self.single_partner_info = self.db_connect_values.take_current_partner_info(partnerStaticName.Partner.return_name())

        self.main_layout.addWidget(QLabel("Имя партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(self.single_partner_info[0]["name"]))

        self.main_layout.addWidget(QLabel("Телефон партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(f'+7 {self.single_partner_info[0]["phone"]}'))

        self.main_layout.addWidget(QLabel("Рейтинг партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(f'{self.single_partner_info[0]["rate"]}'))

        self.main_layout.addWidget(QLabel("Директор"))
        self.main_layout.addWidget(self.qlabel_pattern(self.single_partner_info[0]["director"]))

        self.main_layout.addWidget(QLabel("ИНН партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(self.single_partner_info[0]["inn"]))

        self.main_layout.addWidget(QLabel("Тип партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(self.single_partner_info[0]["type"]))

        self.main_layout.addWidget(QLabel("Почта партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(self.single_partner_info[0]["mail"]))

        self.main_layout.addWidget(QLabel("Адрес партнера"))
        self.main_layout.addWidget(self.qlabel_pattern(self.single_partner_info[0]["ur_addr"]))

        self.btn_back = QPushButton("Назад")
        self.btn_back.clicked.connect(
            lambda : self.value_to_use_main_application_self.switch_to_new_frame(partners.interface)
        )
        self.main_layout.addWidget(self.btn_back)

        self.buttonHistory = QPushButton("История", objectName="buttonHistory")
        self.buttonHistory.clicked.connect(
            lambda : self.value_to_use_main_application_self.switch_to_new_frame(getHistory.HistoryFrame)
        )
        self.main_layout.addWidget(self.buttonHistory)


        self.update_btn = QPushButton("Обновить данные о патнере")
        self.update_btn.clicked.connect(
            lambda : self.value_to_use_main_application_self.switch_to_new_frame(updateFrame.UpdatePartnerFrame)
        )

        self.main_layout.addWidget(self.update_btn)

    def qlabel_pattern(self, text):
        label = QLabel(text)
        label.setObjectName("PartnerInfo")
        return label
