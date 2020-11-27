class IncorrectInput(Exception):
    pass


class RateField:
    field_description = "Rate"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        try:
            self.value = float(value)
        except ValueError:
            raise IncorrectInput(f"value {value} can't be converted to float")
