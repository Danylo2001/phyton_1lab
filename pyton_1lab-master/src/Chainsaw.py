class Chainsaw:
    chainsaws_quantity = 0

    def __init__(self, name="", power=0, turns_per_minute=0, weight=0,
                 price=0, registration_country=""):
        self.name = name
        self.power = power
        self.turns_per_minute = turns_per_minute
        # In KG
        self.weight = weight
        # In UAH
        self.price = price
        self.registration_country = registration_country
        Chainsaw.chainsaws_quantity += 1

    def __del__(self):
        print("Destructor was called")

    def __str__(self):
        return "Chainsaw{" \
               + "name='" + self.name + "'" \
               + ", power=" + str(self.power) \
               + ", turns_per_minute=" + str(self.turns_per_minute) \
               + ", weight=" + str(self.weight) \
               + ", price=" + str(self.price) \
               + ", brand_registration_country='" + self.registration_country + "'" + "}"

    @staticmethod
    def get_static_chainsaws_quantity():
        return Chainsaw.chainsaws_quantity
