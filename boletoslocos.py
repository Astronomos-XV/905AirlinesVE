"""import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QTextEdit, QVBoxLayout

class TicketReservationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reserva de Boletos de Avión")
        self.resize(400, 400)

        layout = QVBoxLayout()

        self.name_label = QLabel("Nombre:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.surname_label = QLabel("Apellido:")
        self.surname_input = QLineEdit()
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)

        self.id_label = QLabel("Número de Identificación:")
        self.id_input = QLineEdit()
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_input)

        self.passenger_type_label = QLabel("Tipo de Pasajero:")
        self.adult_radio = QRadioButton("Adulto")
        self.child_radio = QRadioButton("Niño")
        self.elderly_radio = QRadioButton("Adulto Mayor")
        layout.addWidget(self.passenger_type_label)
        layout.addWidget(self.adult_radio)
        layout.addWidget(self.child_radio)
        layout.addWidget(self.elderly_radio)

        self.destinations_label = QLabel("Destinos:")
        self.destinations_combo = QComboBox()
        self.destinations_combo.addItem("Nueva York - $500")
        self.destinations_combo.addItem("París - $700")
        self.destinations_combo.addItem("Tokio - $900")
        layout.addWidget(self.destinations_label)
        layout.addWidget(self.destinations_combo)

        self.save_button = QPushButton("Guardar Información")
        self.save_button.clicked.connect(self.save_info)
        layout.addWidget(self.save_button)

        self.info_display = QTextEdit()
        layout.addWidget(self.info_display)

        self.setLayout(layout)

    def save_info(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        passenger_id = self.id_input.text()
        passenger_type = "Adulto" if self.adult_radio.isChecked() else "Niño" if self.child_radio.isChecked() else "Adulto Mayor"
        destination = self.destinations_combo.currentText()

        info = f"Nombre: {name}\nApellido: {surname}\nID: {passenger_id}\nTipo: {passenger_type}\nDestino: {destination}\n"

        with open("informacion_pasajero.txt", "a") as file:
            file.write(info)

        self.info_display.append(info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicketReservationApp()
    window.show()
    sys.exit(app.exec())"""


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QComboBox, QTextEdit, QCalendarWidget, QVBoxLayout

class TicketReservation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('905 Airlines')
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: lightyellow;")
        self.name_label = QLabel('<b><font color="green">Nombre:</font></b>')
        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("background-color: white;")

        self.surname_label = QLabel('<b><font color="green">Apellido:</font></b>')
        self.surname_input = QLineEdit()
        self.surname_input.setStyleSheet("background-color: white;")

        self.id_label = QLabel('<b><font color="green">Número de Cedula:</font></b>')
        self.id_input = QLineEdit()
        self.id_input.setStyleSheet("background-color: white;")

        self.date_label = QLabel('<b><font color="green">Fecha de Salida:</font></b>')
        self.calendar = QCalendarWidget(self)
        self.calendar.setStyleSheet("background-color: lightgreen;")
        self.passenger_type_label = QLabel('<b><font color="green">Tipo de Pasajero:</font></b>')
        self.adult_radio = QRadioButton('Adulto')
        self.child_radio = QRadioButton('Niño')
        self.elderly_radio = QRadioButton('Adulto Mayor')

        self.destination_label = QLabel('Destino:')
        self.destinations = QComboBox()
        self.destinations.setStyleSheet("background-color: white;")
        self.destinations.addItem('Nueva York - $500')
        self.destinations.addItem('París - $700')
        self.destinations.addItem('Roma - $750')
        self.destinations.addItem('Budapest - $850')
        self.destinations.addItem('Tokio - $900')
        

        self.save_button = QPushButton('Guardar Información')
        self.save_button.setStyleSheet("background-color: white;")
        self.save_button.clicked.connect(self.save_info)

        self.info_display = QTextEdit()
        self.info_display.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_input)
        layout.addWidget(self.date_label)
        layout.addWidget(self.calendar)
        layout.addWidget(self.passenger_type_label)
        layout.addWidget(self.adult_radio)
        layout.addWidget(self.child_radio)
        layout.addWidget(self.elderly_radio)
        layout.addWidget(self.destination_label)
        layout.addWidget(self.destinations)
        layout.addWidget(self.save_button)
        layout.addWidget(self.info_display)

        self.setLayout(layout)

    def save_info(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        id_number = self.id_input.text()
        date = self.calendar.selectedDate().toString()
        passenger_type = ''
        if self.adult_radio.isChecked():
            passenger_type = 'Adulto'
        elif self.child_radio.isChecked():
            passenger_type = 'Niño'
        else:
            passenger_type = 'Adulto Mayor'
        destination = self.destinations.currentText()

        info = f'Nombre: {name}\nApellido: {surname}\nID: {id_number}\nFecha: {date}\nTipo de Pasajero: {passenger_type}\nDestino: {destination}\n\n'

        with open('informacion_reserva.txt', 'a') as file:
            file.write(info)

        self.info_display.append(info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicketReservation()
    window.show()
    sys.exit(app.exec())
