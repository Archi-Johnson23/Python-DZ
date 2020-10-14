from views import render_template
from models import User, Phone , Adres, City


def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default.jinja2", cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit.jinja2", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users':users}, template="all_users.jinja2", cls=cls)
    input("Продолжить?")
    return 'main', None # (next state, data)

#---------------------------------------------------------------------Adres
def add_adres_controller(data=None, cls=True):
    render_template(context={}, template="add_adres.jinja2", cls=cls)
    adres_number = input()
    adres = Adres.add(adres_number)
    return 21, adres # (next state, data)

#---------------------------------------------------------------------City
def add_city_controller(data=None,cls=True):
    render_template(context={}, template="add_city.jinja2", cls=cls)
    city_n = input()
    city = City.add(city_n)
    return 21, city # (next state, data)

def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.add(username)
    return 21, user # (next state, data)

def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user # (next state, data)

def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input()
    if answer == 'Y':
        return 21, user
    return 51, user # (next state, data)

def get_controller(state):
    return controllers_dict.get(state, default_controller)


controllers_dict = { # use dict type instead of if else chain
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller and add_city_controller and add_adres_controller ,
    21: add_phone_controller, # user can't enter 21 of int type
    212: add_more_controller
}