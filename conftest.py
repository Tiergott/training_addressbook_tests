import pytest
import json, random, string, os.path
from models.addressbook_app import AddressBookApp
from models.addressbook_db import AddressBookDB
from models.group import Group


@pytest.fixture(scope="session")
def config():
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(file_name) as fc:
        return json.load(fc)


@pytest.fixture()
def app(config, selenium):
    driver = selenium #webdriver.Chrome()
    base_url = config["web"]["base_url"]
    app = AddressBookApp(driver, base_url)
    yield app
    app.quit()


@pytest.fixture(scope="session")
def db(config):
    # config = {"host": 'localhost', "user": 'root', "password": '', "db": "test"}
    db = AddressBookDB(**config["db"])
    yield db
    db.close()


@pytest.fixture()
def login_admin(app, config):
    app.login(username=config["web"]["user"], password=config["web"]["password"])
    yield
    app.logout()


@pytest.fixture()
def check_groups_exist(app, login_admin):
    if app.count_groups() == 0:
        app.create_group(name="1234", header="12345", footer="1234")


def random_string(maxlen):
    length = random.randrange(1, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    result = ''.join([random.choice(symbols) for _ in range(length)])
    return result


filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "groups_data.json")

with open(filename, encoding="utf8") as f:
    groups_data = json.load(f)

# Группы, которые мы получаем из данных из файла
groups_list = [Group(**data) for data in groups_data]

# Добавим немного рандомных групп:
groups_list += [Group(random_string(50), random_string(50), random_string(20))
                for _ in range(3)
                ]

resr_list = [str(g) for g in groups_list]


@pytest.fixture(params=groups_list, ids=resr_list)
def group(request):
    return request.param
