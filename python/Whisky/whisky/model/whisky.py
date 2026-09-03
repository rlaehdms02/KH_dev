class Whisky:
    def __init__(self, whisky_name, whisky_year, price):
        self.whisky_name = whisky_name
        self.whisky_year = whisky_year
        self.price = price

    def __str__(self):
        return f"{self.whisky_name} {self.whisky_year}년도 {self.price}원"
    def to_dict(self) -> dict:
        return {"위스키": self.whisky_name, "년도": self.whisky_year, "가격": self.price}
    @staticmethod
    def from_dict(dict_data) -> Whisky:
        return Whisky(dict_data["위스키"], dict_data["년도"], dict_data["가격"])

