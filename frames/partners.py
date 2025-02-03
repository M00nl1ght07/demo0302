from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QWidget,
    QPushButton,
    QLabel,
    QScrollArea, QHBoxLayout
)

import partnerStaticName
from frames import addPartner, partnerinfo


class interface(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()
        self.setLayout(self.widgets_layout)

    def update_start_values(self):
        self.widgets_layout = QVBoxLayout(self)

        self.heading = QLabel("Партнеры")
        self.heading.setObjectName("heading1")
        self.widgets_layout.addWidget(self.heading)
        self.scroll_area = self.create_scroll()
        self.widgets_layout.addWidget(self.scroll_area)
        self.btn = QPushButton("Добавить партнера")
        self.btn.clicked.connect(self.open_new_frame)
        self.widgets_layout.addWidget(self.btn)
        self.scroll_area.setWidget(self.create_partner_card())

    def create_scroll(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        return scroll_area

    def create_scroll_area_widget_container(self):
        scroll_area_widget_container = QWidget()
        return scroll_area_widget_container

    def create_partner_card(self):
        self.scroll_area_widget_container = (self.create_scroll_area_widget_container())
        self.card_layout = QVBoxLayout(self.scroll_area_widget_container)

        for partners in self.connection.take_partner_information():
            self.partner_card = QWidget()
            self.partner_card.setObjectName("partner_card")
            self.vbox = QVBoxLayout(self.partner_card)

            self.horizontal_layout = QHBoxLayout()
            self.label1 = QLabel(f'{partners["type"]} | {partners["name"].replace("  ", " ")}')
            self.horizontal_layout.addWidget(self.label1)
            self.label1.setObjectName("company_name")

            sale_percentage = self.take_sale_cont(partners["name"])
            self.label5 = QLabel(f'{sale_percentage}%')
            self.horizontal_layout.addWidget(self.label5)
            self.label5.setObjectName("company_percentage")
            self.vbox.addLayout(self.horizontal_layout)

            self.label2 = QLabel(f'{partners["director"]}')
            self.vbox.addWidget(self.label2)
            self.label2.setObjectName("company_director")

            self.label3 = QLabel(f'+7 {partners["phone"]}')
            self.vbox.addWidget(self.label3)
            self.label3.setObjectName("company_phone")

            self.label4 = QLabel(f'Рейтинг: {partners["rate"]}')
            self.vbox.addWidget(self.label4)
            self.label4.setObjectName("company_rate")

            self.btn = QPushButton("Подробнее")
            self.btn.setObjectName("card_btn")
            self.btn.clicked.connect(self.open_single_partner)
            self.vbox.addWidget(self.btn)

            self.card_layout.addWidget(self.partner_card)
        return self.scroll_area_widget_container

    def open_new_frame(self):
        self.controller.switch_to_new_frame(addPartner.interface_reg_parther)

    def take_sale_cont(self, partner_name: str):
        count: int = self.connection.sale_sum(partner_name)[0]['procent']
        if (count == None):
            return 0
        if (count > 300000):
            return 15
        if (count > 50000):
            return 10
        if (count > 10000):
            return 5
        return 5

    def open_single_partner(self):
        sender = self.sender()
        partner_name = sender.parent().findChild(QLabel, "company_name").text().split("|")[-1].strip()
        partnerStaticName.Partner.set_name(partner_name)
        self.controller.switch_to_new_frame(partnerinfo.PartnerCardFullInfo, partner_name)
