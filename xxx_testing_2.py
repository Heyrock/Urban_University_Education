class Wine:
    def __init__(self, name, grape, year):
        self.name = name
        self.grape = grape
        self.year = year

class RedWine(Wine):
    def serve(self):
        print(f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать комнатной температуры.")

class WhiteWine(Wine):
    def serve(self):
        print(f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать хорошо охлажденным.")

class RoseWine(Wine):
    def serve(self):
        print(f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year} году, рекомендуем подавать слегка охлажденным.")

class Winery:
    def __init__(self):
        self.wines = []

    def add_wine(self, wine):
        self.wines.append(wine)

    def serve_wines(self):
        for wine in self.wines:
            wine.serve()