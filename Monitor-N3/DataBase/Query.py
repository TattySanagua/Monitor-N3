from DataBase.Manager import DatabaseManager
import pandas as pd

class Query:

    @staticmethod
    def get_embalse():
        database_manager = DatabaseManager()
        query = "SELECT fecha, nivel_embalse FROM embalse;"
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha','nivel_embalse'])
            return df
        return pd.DataFrame()


    @staticmethod
    def get_precipiaciones():
        database_manager = DatabaseManager()
        query = """SELECT e.fecha,
                    e.nivel_embalse, 
                    p.valor,
                    (SELECT p3.valor FROM precipitacion p3
                        WHERE p3.fecha = DATE_SUB(e.fecha, INTERVAL 3 DAY)) AS tres_dias_previos,
                    (SELECT p5.valor FROM precipitacion p5
                        WHERE p5.fecha = DATE_SUB(e.fecha, INTERVAL 5 DAY)) AS cinco_dias_previos,
                    (SELECT p10.valor FROM precipitacion p10
                        WHERE p10.fecha = DATE_SUB(e.fecha, INTERVAL 10 DAY)) AS diez_dias_previos
                 FROM embalse e
                 LEFT JOIN precipitacion p ON e.fecha = p.fecha
                 ORDER BY e.fecha DESC;"""
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'valor', 'tres_dias_previos', 'cinco_dias_previos', 'diez_dias_previos'])
        return results

    @staticmethod
    def get_instrumentos():
        database_manager = DatabaseManager()
        query = """SELECT nombre, nombre_tipo, tipo_medicion, fecha_alta, fecha_baja, activo 
                    FROM instrumento INNER JOIN tipo USING(id_tipo);"""
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['Nombre', 'Tipo', 'Medición', 'Fecha de instalación', 'Fecha de baja', 'Activo'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_instrumentos_por_tipo(tipo):
        database_manager = DatabaseManager()
        query = """SELECT nombre, nombre_tipo, fecha_alta, fecha_baja, activo 
                        FROM instrumento INNER JOIN tipo USING(id_tipo) WHERE nombre_tipo = {tipo};"""
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['Nombre', 'Tipo', 'Fecha de instalación', 'Fecha de baja', 'Activo'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_tipo():
        database_manager = DatabaseManager()
        query = "SELECT nombre_tipo FROM tipo;"
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['Tipo'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_tipo_id(nombre_tipo):
        database_manager = DatabaseManager()
        query = f"SELECT id_tipo FROM tipo WHERE nombre_tipo = '{nombre_tipo}';"
        results = database_manager.fetch_data(query)
        if results:
            return results[0][0]
        return None

    @staticmethod
    def get_embalse_piezometros():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, GROUP_CONCAT(CONCAT(i.nombre, ': ', IFNULL(m.valor, '-')) 
                    ORDER BY i.nombre SEPARATOR '; ') AS nivel_piezometrico 
                    FROM embalse e 
                    LEFT JOIN instrumento i ON i.id_tipo = (SELECT id_tipo FROM tipo WHERE nombre_tipo = 'PIEZÓMETRO') AND i.activo = 1 
                    LEFT JOIN medicion m ON e.fecha = DATE(m.fecha) AND m.id_instrumento = i.id_instrumento 
                    GROUP BY e.fecha, e.nivel_embalse 
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_piezometros_data():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, i.nombre, m.valor AS nivel_piezometrico
                    FROM embalse e 
                    LEFT JOIN medicion m ON e.fecha = DATE(m.fecha)
                    LEFT JOIN instrumento i ON m.id_instrumento = i.id_instrumento
                    WHERE i.id_tipo = (SELECT id_tipo FROM tipo WHERE nombre_tipo = 'PIEZÓMETRO') AND i.activo = 1 
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'nombre', 'nivel_piezometrico'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_embalse_pc1_5_6():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, 
                        mp1.valor AS nivel_piezometrico_pc1,
                        mp5.valor AS nivel_piezometrico_pc5, 
                        mp6.valor AS nivel_piezometrico_pc6
                    FROM embalse e
                    LEFT JOIN medicion_piezometro mp1 ON e.fecha = DATE(mp1.fecha) 
                        AND mp1.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC1')
                    LEFT JOIN medicion_piezometro mp5 ON e.fecha = DATE(mp5.fecha)  
                        AND mp5.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC5')
                    LEFT JOIN medicion_piezometro mp6 ON e.fecha = DATE(mp6.fecha) 
                        AND mp6.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC6')
                    WHERE mp1.valor IS NOT NULL
                        OR mp5.valor IS NOT NULL
                        OR mp6.valor IS NOT NULL
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'nivel_piezometrico_pc1', 'nivel_piezometrico_pc5', 'nivel_piezometrico_pc6'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_embalse_freatimetros():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, GROUP_CONCAT(CONCAT(i.nombre, ': ', IFNULL(m.valor, '-')) 
                        ORDER BY i.nombre SEPARATOR '; ') AS nivel_freatico 
                        FROM embalse e 
                        LEFT JOIN instrumento i ON i.id_tipo = (SELECT id_tipo FROM tipo WHERE nombre_tipo = 'FREATÍMETRO') AND i.activo = 1 
                        LEFT JOIN medicion m ON e.fecha = DATE(m.fecha) AND m.id_instrumento = i.id_instrumento 
                        GROUP BY e.fecha, e.nivel_embalse 
                        ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'nivel_freatico'])
            return df
        return pd.DataFrame()
    @staticmethod
    def get_freatimetros_data():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, i.nombre, m.valor AS nivel_freatico
                    FROM embalse e 
                    LEFT JOIN medicion m ON e.fecha = DATE(m.fecha)
                    LEFT JOIN instrumento i ON m.id_instrumento = i.id_instrumento
                    WHERE i.id_tipo = (SELECT id_tipo FROM tipo WHERE nombre_tipo = 'FREATÍMETRO') AND i.activo = 1
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'nombre', 'nivel_freatico'])
            return df
        return pd.DataFrame()

    @staticmethod
    def get_embalse_f1_pc2_pc3_pc4():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, 
                        mf.valor AS nivel_freatico,
                        mp2.valor AS nivel_piezometrico_pc2,
                        mp3.valor AS nivel_piezometrico_pc3, 
                        mp4.valor AS nivel_piezometrico_pc4
                    FROM embalse e
                    LEFT JOIN medicion_freatimetro mf ON e.fecha = DATE(mf.fecha) 
                        AND mf.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-F1')
                    LEFT JOIN medicion_piezometro mp2 ON e.fecha = DATE(mp2.fecha) 
                        AND mp2.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC2')
                    LEFT JOIN medicion_piezometro mp3 ON e.fecha = DATE(mp3.fecha)  
                        AND mp3.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC3')
                    LEFT JOIN medicion_piezometro mp4 ON e.fecha = DATE(mp4.fecha) 
                        AND mp4.id_instrumento = (SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC4')
                    WHERE mf.valor IS NOT NULL
                        OR mp2.valor IS NOT NULL
                        OR mp3.valor IS NOT NULL
                        OR mp4.valor IS NOT NULL
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results,
                              columns=['fecha', 'nivel_embalse', 'nivel_freatico', 'nivel_piezometrico_pc2', 'nivel_piezometrico_pc3',
                                       'nivel_piezometrico_pc4'])
            print(df)
            return df
        return pd.DataFrame()
    @staticmethod
    def get_embalse_aforadores():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, 
                    GROUP_CONCAT(CONCAT(i.nombre, ': ', IFNULL(m.valor, '-')) ORDER BY i.nombre SEPARATOR '; ') AS caudal
                    FROM embalse e 
                    LEFT JOIN instrumento i ON i.id_instrumento = i.id_instrumento 
                    LEFT JOIN tipo t ON i.id_tipo = t.id_tipo 
                    LEFT JOIN medicion m ON e.fecha = DATE(m.fecha) AND m.id_instrumento = i.id_instrumento 
                    WHERE t.nombre_tipo LIKE '%AFORADOR%' AND i.activo = 1 
                    GROUP BY e.fecha, e.nivel_embalse 
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'caudal'])
            return df
        return results

    @staticmethod
    def get_aforadores_data():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, i.nombre, m.valor AS caudal
                    FROM embalse e 
                    LEFT JOIN medicion m ON e.fecha = DATE(m.fecha)
                    LEFT JOIN instrumento i ON m.id_instrumento = i.id_instrumento
                    LEFT JOIN tipo t ON i.id_tipo = t.id_tipo
                    WHERE t.nombre_tipo LIKE '%AFORADOR%' AND i.activo = 1
                    ORDER BY e.fecha DESC;""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'nombre', 'caudal'])
            return df
        return pd.DataFrame()


    @staticmethod
    def get_all():
        database_manager = DatabaseManager()
        query = ("""SELECT e.fecha, e.nivel_embalse, i.id_instrumento, i.nombre, 
                            ma.valor AS caudal, 
                            mf.valor AS nivel_freatico, 
                            mp.valor AS nivel_piezometrico
                    FROM embalse e LEFT JOIN medicion_aforador ma ON e.fecha = DATE(ma.fecha)
                                LEFT JOIN medicion_freatimetro mf ON e.fecha = DATE(mf.fecha)
                                LEFT JOIN medicion_piezometro mp ON e.fecha = DATE(mp.fecha)
                                LEFT JOIN instrumento i ON (mp.id_instrumento = i.id_instrumento 
                                                            OR mf.id_instrumento = i.id_instrumento
                                                            OR ma.id_instrumento = i.id_instrumento);""")
        results = database_manager.fetch_data(query)
        if results:
            df = pd.DataFrame(results, columns=['fecha', 'nivel_embalse', 'id_instrumento', 'nombre', 'caudal', 'nivel_freatico', 'nivel_piezometrico'])
            return df
        return pd.DataFrame()

    ####
    @staticmethod
    def insert_data_embalse(fecha, hora, nivel_ambalse):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO embalse (fecha, hora, nivel_embalse) "
                 f"VALUES ('{fecha}', '{hora}', {nivel_ambalse});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_precipitaciones(fecha, valor):
        database_manager = DatabaseManager()
        query = (f"INSERT INTO precipitacion (fecha, valor) "
                 f"VALUES ('{fecha}', {valor});")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc1(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC1'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc2(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC2'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc3(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC3'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc4(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC4'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc5(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC5'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc6(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC6'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_pc7(fecha, nivel_piezometrico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_piezometro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-PC7'), 
                '{fecha}', 
                {nivel_piezometrico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_l3_f1(fecha, nivel_freatico):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_freatimetro (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'L3-F1'), 
                '{fecha}', 
                {nivel_freatico});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_afo3_ei(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_aforador (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'AFO3-EI'), 
                '{fecha}', 
                {caudal});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_afo3_pp(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_aforador (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'AFO3-PP'), 
                '{fecha}', 
                {caudal});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_afo3_tot(fecha, caudal):
        database_manager = DatabaseManager()
        query = (f"""INSERT INTO medicion_aforador (id_instrumento, fecha, valor)
        VALUES ((SELECT id_instrumento FROM instrumento WHERE nombre = 'AFO3-TOT'), 
                '{fecha}', 
                {caudal});""")
        database_manager.execute_query(query)

    @staticmethod
    def insert_data_instrument(nombre, id_tipo, fecha_alta):
        database_manager = DatabaseManager()
        query = f"""INSERT INTO instrumento (nombre, id_tipo, fecha_alta, activo) 
                    VALUES ('{nombre}', '{id_tipo}', '{fecha_alta}', 1);"""
        database_manager.execute_query(query)

    @staticmethod
    def delete_instrument(nombre_instrumento):
        database_manager = DatabaseManager()
        query = f""" UPDATE instrumento SET activo = 0, fecha_baja = NOW()
                    WHERE nombre = '{nombre_instrumento}' AND activo = 1;"""
        database_manager.execute_query(query)