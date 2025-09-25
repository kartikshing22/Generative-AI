from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

person: Person = {"name":"kartik","age":25}
print(person)



"""
typed dict gives info about datatype of values but it does not gives error if we give wrong datatype
"""