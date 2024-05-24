import DictionaryStr
class Main:
    @staticmethod
    def execute():
        dict_strategy = DictionaryStr.DictionaryStr()
        price = 100
        
        print(f"Precio para adulto: {dict_strategy.set_strategy('adulto', price)}")
        print(f"Precio para niño: {dict_strategy.set_strategy('niño', price)}")
        print(f"Precio para estudiante: {dict_strategy.set_strategy('estudiante', price)}")

if __name__ == "__main__":
    Main.execute()