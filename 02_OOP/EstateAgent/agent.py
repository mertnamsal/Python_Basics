
from purchase import ApartmantPurchase, HousePurchase
from rental import ApartmantRental, HouseRental
from utilities import get_valid_input

class Agent():
    def __init__(self):
        self.properties = []

    def display_property_list(self):
        for item in self.properties:
            item.display()

    process_type = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmantRental,
        ('apartment', 'purchase'): ApartmantPurchase
    }

    def request_property(self):
        property_type = get_valid_input(
            input_question='What type of property do you want?',
            valid_options=('house','apartment')
        )

        payment_type = get_valid_input(
            input_question='What payment type do you prefer?',
            valid_options=('purchase','rental')
        )

        generated_class = self.process_type[(property_type, payment_type)]
        init_args = generated_class.prompt_init()
        self.properties.append(generated_class(**init_args))


agent = Agent()
agent.request_property()
agent.display_property_list()