from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QFrame, QTreeWidget, QTreeWidgetItem, QPushButton

from frames import partnerinfo
from partnerStaticName import Partner


class HistoryFrame(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.database = self.controller.connection
        self.updateStartValues()
        self.setLayout(self.widgetsLayoutContainer)

    def updateStartValues(self):
        self.widgetsLayoutContainer = QVBoxLayout()
        self.widgetsLayoutContainer.addWidget(QLabel("История партнера", objectName="title"))

        self.tables = QTreeWidget()
        self.widgetsLayoutContainer.addWidget(self.tables)
        self.tables.setHeaderLabels(["Продукт", "Партнер", "Количество", "Дата"])

        self.partnername = None
        for history in self.database.get_history(Partner.return_name()):
            self.partnername = history["partnername"]
            self.tableHistory = QTreeWidgetItem(self.tables)
            self.tableHistory.setText(0, history["productname"])
            self.tableHistory.setText(1, history["partnername"])
            self.tableHistory.setText(2, str(history["quantity"]))
            self.tableHistory.setText(3, str(history["saleDate"]))

        self.buttonRestoreTable = QPushButton("Перезагрузить таблицу")
        self.buttonRestoreTable.clicked.connect(self.restoreTable)
        self.widgetsLayoutContainer.addWidget(self.buttonRestoreTable)

        self.buttonBack = QPushButton("Назад", objectName="buttonBack")
        self.buttonBack.clicked.connect(self.showPartnerMoreInfoFrame)
        self.widgetsLayoutContainer.addWidget(self.buttonBack)

    def restoreTable(self):
        self.controller.restoreTable(HistoryFrame, self.partnername)

    def showPartnerMoreInfoFrame(self):
        self.controller.switch_to_new_frame(partnerinfo.PartnerCardFullInfo)
