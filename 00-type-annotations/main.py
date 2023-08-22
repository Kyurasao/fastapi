from datetime import datetime
from typing import List, Union, Tuple, Set, Dict, Optional

from pydantic import BaseModel


def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


print(get_name_with_age("john", 12))


def process_items_1(items: List[str]):
    for item in items:
        print(item.capitalize())


def process_items_2(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s.pop()


def process_items_3(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name.title())
        print(item_price.hex())


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

# при аннотации типов питон сам пытается исправить ошибки, но не показывает их в коде
# id, friends
# что должно было произойти с signup_ts ?????