import StrategyPrice


class DictionaryStr:
    def __init__(self):
        self.strategy = {
            'adulto': StrategyPrice.adult,
            'niño': StrategyPrice.child,
            'estudiante': StrategyPrice.student
        }

    def set_strategy(self, type_user, base_price):
        if type_user in self.strategy:
            return self.strategy[type_user](base_price)
        else:
            return "Tipo de usuario no válido"