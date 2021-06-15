import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox


def dialog():
    mbox = QMessageBox()

    mbox.setText("您好")
    mbox.setDetailedText("吴晨是很好人")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle('吴晨')

    label = QLabel(w)
    label.setText("Behold the Guru, 吴晨")
    label.move(100, 130)
    label.show()

    btn = QPushButton(w)
    btn.setText('等一下吴晨')
    btn.move(110, 150)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    sys.exit(app.exec_())




