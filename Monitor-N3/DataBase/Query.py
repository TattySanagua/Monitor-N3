from DataBase.Manager import DatabaseManager

class Query:

    @staticmethod
    def get_embalse():
        query = "SELECT fecha, hora, nivel_embalse FROM embalse;"
        results = DatabaseManager.fetch_data(query)
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

    @staticmethod
    def insert_data_embalse(fecha, hora, nivel_ambalse):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO embalse (fecha, hora, nivel_embalse) "
                 f"VALUES ('{fecha}', '{hora}', {nivel_ambalse});")
        database_manager.execute_query(query)
    @staticmethod
    def insert_data_l3_pc1(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc1 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc2(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc2 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc3(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc3 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc4(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc4 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc5(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc5 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc6(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc6 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc7(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_pc7 (fecha, nivel_piezometrico) "
                 f"VALUES ('{fecha}', {nivel_piezometrico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_f1(fecha, nivel_freatico):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO l3_f1 (fecha, nivel_freatico) "
                 f"VALUES ('{fecha}', {nivel_freatico});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_afo3_ei(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO afo3_ei (fecha, caudal) "
                 f"VALUES ('{fecha}', {caudal});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_afo3_pp(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO afo3_pp (fecha, caudal) "
                 f"VALUES ('{fecha}', {caudal});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_afo3_tot(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO afo3_tot (fecha, caudal) "
                 f"VALUES ('{fecha}', {caudal});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_parshall(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO parshall (fecha, caudal) "
                 f"VALUES ('{fecha}', {caudal});")
        database_manager.execute_query(query)