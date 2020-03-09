import json


class Converter:#Convierte los datos desde html a Json

    def __init__(self,Temperat,timeup):
        self.Temperature = Temperat
        self.tiemp = timeup
        
    def HTML_To_Json(self):
        Data = {
            'Temperatura': self.Temperature,
            'tiempo': self.tiemp
        }
        converter = json.dumps(Data)
        return converter            

