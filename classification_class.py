

class ClassificationClass():
    def __init__(self, class_name, description_criteria, tags, min_amount=None, max_amount=None):
        self._class_name = class_name
        self._description_criteria = description_criteria
        self._tags = tags
        self._min_amount = min_amount
        self._max_amount = max_amount

    @property
    def tags(self):
        return self._tags

    @property
    def class_name(self) -> str:
        return self._class_name

    @property
    def description(self) -> str:
        return self._description_criteria

    @property
    def min_amount(self) -> float:
        return self._min_amount

    @property
    def max_amount(self) -> float:
        return self._max_amount

    def is_contained(self, description: str, amount: float):
        check_amount = -amount if amount < 0 else amount

        if self.description.lower() not in description.lower():
            return False
        if self.min_amount is not None:
            if check_amount < self.min_amount:
                return False
        if self.max_amount is not None:
            if check_amount > self.max_amount:
                return False

        return True




