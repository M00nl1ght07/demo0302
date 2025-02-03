from PySide6.QtWidgets import QMessageBox


def send_info_message_box(message_text: str):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Информация")
    msgBox.setText(message_text)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Yes |QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
    msgBox.setIcon(QMessageBox.Icon.Information)
    result = msgBox.exec()
    print(result)
    return result

def send_discard_message_box(message_text: str):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Информация")
    msgBox.setText(message_text)
    msgBox.setStandardButtons(QMessageBox.StandardButton.Yes |QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Yes)
    msgBox.setIcon(QMessageBox.Icon.Warning)
    result = msgBox.exec()
    print(result)
    return result