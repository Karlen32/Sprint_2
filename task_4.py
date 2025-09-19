class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name: str, hours: int, rest_days: int, email: str):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name: str, hours: int, rest_days: int, email: str):
        if not hours:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name: str, hours: int, rest_days: int, email: str):
        if not email:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment: int):
        cls.hourly_payment = new_payment

    def salary(self) -> int:
        return self.hours * self.hourly_payment