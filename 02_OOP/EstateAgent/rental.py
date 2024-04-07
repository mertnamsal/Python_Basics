
from property import Property, Apartmant, House
from utilities import get_valid_input

class Rental(Property):
    def __init__(self, furnished='', extras='', rent='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rent = rent
        self.extras = extras
        self.furnished = furnished

    def display(self):
        super().display()
        print(f'Rental Detail\n'
              f'===============\n'
              f'Rent: {self.rent}\n'
              f'Furnished: {self.furnished}\n'
              f'Extras: {self.extras}')

    def prompt_init():
        return dict(
            furnished=get_valid_input(
                input_question='Do you want to furniture furnished?',
                valid_options=('yes', 'no')
            ),
            extras=input('What are the extras prefer?'),
            rent=input('What is the estimated montly rental?')
        )

    prompt_init = staticmethod(prompt_init)


class ApartmantRental(Apartmant, Rental):
    def prompt_init():
        init = Apartmant.prompt_init()
        init.update(
            Rental.prompt_init()
        )

        return init

    prompt_init = staticmethod(prompt_init)


class HouseRental(House, Rental):
    def prompt_init():
        init = House.prompt_init()
        init.update(
            Rental.prompt_init()
        )

        return init

    prompt_init = staticmethod(prompt_init)


