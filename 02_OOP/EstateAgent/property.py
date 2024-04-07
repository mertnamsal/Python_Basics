

from utilities import get_valid_input


class Property:
    def __init__(self, square_feet='', bedrooms='', bathrooms='', *args, **kwargs):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.square_feet = square_feet

    def display(self):
        print(f'General Informamtion\n'
              f'====================\n'
              f'Square Feet: {self.square_feet}\n'
              f'Bedrooms: {self.bedrooms}\n'
              f'Bathrooms: {self.bathrooms}\n')

    def prompt_init():
        return dict(
            square=input('Square Feet: '),
            bedrooms=input('Bedrooms: '),
            bathrooms=input('Bathrooms: ')
        )

    prompt_init = staticmethod(prompt_init)


class Apartmant(Property):
    def __init__(self, balcony='', laundry='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        super().display()
        print(f'Balcony: {self.balcony}\n'
              f'Laundry: {self.laundry}')

    def prompt_init():
        parent_init = Property.prompt_init()

        balcony = get_valid_input(
            input_question='Does apartmant have a balcony?',
            valid_options=('yes', 'no')
        )

        laundry = get_valid_input(
            input_question='What laundry type do you prefer?',
            valid_options=('coin', 'credit card', 'none')
        )

        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    def __init__(self, number_stories='', garage='', fenced='', pool='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pool = pool
        self.fenced = fenced
        self.garage = garage
        self.number_stories = number_stories

    def display(self):
        super().display()
        print(f'Number of Stories: {self.number_stories}\n'
              f'Fenced: {self.fenced}\n'
              f'Garage: {self.garage}\n'
              f'Pool: {self.pool}\n')

    def prompt_init():
        parent_init = Property.prompt_init()

        number_stories = input('How many stories do you want?')

        garage = get_valid_input(
            input_question='Do you want to garage?',
            valid_options=('attach', 'detached', 'none')
        )

        pool = get_valid_input(
            input_question='Do you prefer to pool your house?',
            valid_options=('yes', 'no')
        )

        fenced = get_valid_input(
            input_question='Do you prefer to fenced in your house?',
            valid_options=('yes', 'no')
        )

        parent_init.update({
            'number_stories': number_stories,
            'garage': garage,
            'fenced': fenced,
            'pool': pool
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)