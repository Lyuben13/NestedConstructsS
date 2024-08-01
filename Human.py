class Human:
    def __init__(
            self, full_name: str, date_of_birth: str,
            phone: str, city: str, country: str,
            home_address: str
    ):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.city = city
        self.country = country
        self.home_address = home_address

    def show_info(self):
        person_info = f'{self.full_name}, date of birth:{self.date_of_birth}, was born in {self.city}, {self.country}'
        return person_info

    def get_first_name(self):
        first_name = self.full_name.split()[0]
        return f'First name: {first_name}'

human1 = Human('John Smith', '12.01.1991',
               '0882321312', 'Plovdiv', 'Bulgaria',
                      'ul.Dunav172'
)

print(human1.show_info())
print(human1.get_first_name())