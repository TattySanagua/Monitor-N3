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
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc1 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc2():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc2 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc3():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc3 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc4():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc4 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc5():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc5 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc6():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc6 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_pc7():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_pc7 using(fecha);")
        results = database_manager.fetch_data(query)
        return results

    @staticmethod
    def get_l3_f1():
        database_manager = DatabaseManager()
        query = ("SELECT fecha, nivel_embalse, nivel_piezometrico FROM embalse "
                 "INNER JOIN l3_f1 using(fecha);")
        results = database_manager.fetch_data(query)
        return results