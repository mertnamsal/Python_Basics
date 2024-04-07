from property import Property, Apartmant, House
class Purchase(Property):
    def __init__(self, price='', taxes='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.taxes = taxes
        self.price = price

    def display(self):
        super().display()
        print(f'Purchase Detail\n'
              f'==================\n'
              f'Selling Price: {self.price}\n'
              f'Taxes: {self.taxes}')

    def prompt_init():
        return dict(
            price=input('What is the selling price: '),
            taxes=input('What is the estimated taxes: ')
        )

    prompt_init = staticmethod(prompt_init)

class ApartmantPurchase(Apartmant, Purchase):
    def prompt_init():
        init = Apartmant.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(House, Purchase):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)