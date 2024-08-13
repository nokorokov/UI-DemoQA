from dataclasses import dataclass


@dataclass
class Person:
    firstname: str = None
    lastname: str = None
    full_name: str = None
    email: str = None
    age: int = None
    salary: float = None
    department: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None

