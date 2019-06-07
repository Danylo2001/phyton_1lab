from src.Chainsaw import Chainsaw


def main():
    makita = Chainsaw("Makita", 1800, 870, 4.9, 3800, "China")
    bosch = Chainsaw("Bosch", 1800, 920, 4)
    bosch.price = 4300
    bosch.registration_country = "Germany"
    einhell = Chainsaw("Einhell")
    einhell.power = 2000
    einhell.turns_per_minute = 7800
    einhell.weight = 5
    einhell.price = 3200
    einhell.registration_country = "Ukraine"

    print("There are", Chainsaw.get_static_chainsaws_quantity(), "chainsaws:")
    print(makita)
    print(bosch)
    print(einhell)


main()
