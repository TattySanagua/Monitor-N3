from Manager import DatabaseManager

class Query:

    @staticmethod
    def get_embalse():
        database_manager = DatabaseManager()
        query = "SELECT fecha, hora, nivel_embalse FROM embalse;"
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_precipiaciones():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, valor, tres_dias_previos, cinco_dias_previos, diez_dias_previos "
                 "FROM precipitacion;")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc1():
        database_manager = DatabaseManager()
        query = "SELECT fecha, nivel_piezometrico FROM l3_pc1;"
        results = database_manager.fetch_data(query)
        return results