class StrategyPrice:
    @staticmethod
    def adult(price):
        return price * 1

    @staticmethod
    def child(price):
        return price * 0.4

    @staticmethod
    def student(price):
        return price * 0.5