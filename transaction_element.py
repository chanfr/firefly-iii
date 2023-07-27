from datetime import datetime

from classification_class import ClassificationClass

SEPARATOR = "|"

CLASSES = [
    ClassificationClass("Padel", "Carlos Alfredo", ["Clases"]),
    ClassificationClass("Padel", "Playtomic", []),
    ClassificationClass("Padel", "Bizum", [], 0, 10),
    ClassificationClass("Padel", "RUBEN GUZMAN GUZMAN", []),
    ClassificationClass("Lotería", "SIMBA", ["Loteria-Palas"]),
    ClassificationClass("Alimentacion", "FROIZ", []),
    ClassificationClass("Alimentacion", "PRIMOS", []),
    ClassificationClass("Alimentacion", "ALDI", []),
    ClassificationClass("Alimentacion", "LIDL", []),
    ClassificationClass("Alimentacion", "MERCADONA", []),
    ClassificationClass("Farmacia", "Farmacia", []),
    ClassificationClass("Gas", "Sunflower", ["Gastos Casa"]),
    ClassificationClass("Luz", "ELECTRICIDAD", ["Gastos Casa"]),
    ClassificationClass("Comidas Fuera", "VEATS", []),
    ClassificationClass("Comidas Fuera", "UBER * EATS", []),
    ClassificationClass("Comidas Fuera", "RESTAURANTE MANILA", ["Manila"]),
    ClassificationClass("Comidas Fuera", "Just Eat", []),
    ClassificationClass("Comidas Fuera", "BUEN SUSHI-MOSTOLES", []),
    ClassificationClass("Coche", "Repsol Waylet", ["Gasolina"]),
    ClassificationClass("Coche", "BIP DRIVE", ["Peaje"]),
    ClassificationClass("TV", "NETFLIX", []),
    ClassificationClass("Aws", "aws", []),
    ClassificationClass("Telefono", "Telefonica", ["Gastos Casa"]),
    ClassificationClass("Bebe", "kiabi", []),
    ClassificationClass("Bebe", "TOBOGAN ZERO", []),
    ClassificationClass("Apple", "itunes", []),
    ClassificationClass("Securitas", "Securitas", ["Gastos Casa"]),
    ClassificationClass("Comunidad", "Residencial Florida", ["Gastos Casa"]),
    ClassificationClass("Compras Amazon", "Amazon", []),
    ClassificationClass("Transporte", "METRO DE MADRID", ["Metro"]),
    ClassificationClass("Transporte", "RENFE CERCANIAS", ["Metro"]),
    ClassificationClass("Transporte", "RENFE AVE TNA 28-MADRID", ["Metro"]),
    ClassificationClass("Transporte", "RENFE CERCANIAS TNA 28 2-MADRID", ["Metro"]),
    ClassificationClass("Médicos", "CLINICA DENTAL", ["Dentista"]),
    ClassificationClass("Multimedia Casa", "SpotifyES", ["Spotify"]),
    ClassificationClass("Ayudas", "DEVOLUCIONES TRIBUTARIAS", ["Madre trabajadora"], 0, 100),
    ClassificationClass("AliExpress", "aliexpress", []),
    ClassificationClass("Ropa", "JACK&JONES", []),
    ClassificationClass("Gimnasio", "ENJOY WELLNESS", []),
    ClassificationClass("Tabaco", "ESTANCO", []),
]



class TransactionElement():
    def __init__(self, str_element):
        splitted_data = str_element.split(SEPARATOR)
        self._operation_date = datetime.strptime(splitted_data[0], '%d/%m/%Y')
        self._description = splitted_data[1]
        self._effective_date = datetime.strptime(splitted_data[2], '%d/%m/%Y')
        self._amount = float(splitted_data[3])
        self._total_money = float(splitted_data[4])
        self._ref1 = splitted_data[5]
        self._ref2 = splitted_data[6]
        self._classification = None
        self._tags = [""]
        self.set_classification()

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._operation_date

    @property
    def description(self):
        return self._description

    @property
    def classification(self):
        return self._classification

    @classification.setter
    def classification(self, a):
        self._classification = a

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, a):
        self._tags = a

    def set_classification(self):
        for class_item in CLASSES:
            if class_item.is_contained(self.description, self.amount):
                self.classification = class_item.class_name
                self.tags = class_item.tags
                break

    def __str__(self):
        return f'{self.description} ({self.amount}) -> {self.classification}'


