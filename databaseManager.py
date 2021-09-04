import psycopg2
class DatabaseManager:
    def insertSchema(self,data):
        try:
            connection = psycopg2.connect(
                host="ec2-34-254-69-72.eu-west-1.compute.amazonaws.com",
                database="d84lv9hqj4cvad",
                user="pkekjaplofajah",
                password="5f23b729fd13ec1e966727ead1da9717e48c44bd830a6753ee23f54e14d3b099")
            cursor = connection.cursor()
            print(data)
            return "تم تنزيل الداتابيز بنجاح "

        except (Exception, psycopg2.Error) as error:
            return "Error while fetching data from PostgreSQL "+ error

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                return "PostgreSQL connection is closed"


    def getDataSchema(self):
        try:
            connection = psycopg2.connect(
                host="ec2-34-254-69-72.eu-west-1.compute.amazonaws.com",
                database="d84lv9hqj4cvad",
                user="pkekjaplofajah",
                password="5f23b729fd13ec1e966727ead1da9717e48c44bd830a6753ee23f54e14d3b099")
            cursor = connection.cursor()
            tables ={
                "customers_mandopinfo":" INSERT INTO mandopinfo (id, code, email, name, phone, region, date, time) VALUES ",
                "customers_customerinfo":" INSERT INTO customerinfo (id, name, surName, shopName, deviceNo, shopKind, phoneNo, address, accounts, date, time, seller_id, area) VALUES ",
                "transactions_rest":" INSERT INTO rest (id, value, date, time, customer_id) VALUES ",
                "transactions_record":" INSERT INTO record (id, type, value, isDone, isDown, date, time, customerData_id) VALUES "
                }
            
            shema = ""
            for table in tables.keys():
                sql = f"select * from {table}"
                cursor.execute(sql)
                data = []
                for i in cursor.fetchall():
                    row = []
                    for m in i:
                        if str(type(m)) == "<class 'datetime.date'>":
                            row.append(m.strftime('%Y-%m-%d'))
                        elif str(type(m)) == "<class 'datetime.time'>":
                            row.append(m.strftime("%H:%M:%S"))
                        elif m == None: row.append("")
                        elif m == False: row.append(0)
                        elif m == True:row.append(1)
                        else: row.append(m)
                    data.append(tuple(row))

                # data = tables[table]+",".join(data) + +";"

                data = tables[table]+",".join([str(i) for i in data ])+";\n#0#" # i[2]. strftime('%Y-%m-%d')
                shema+=data
                # for row in data:
            return shema

        except (Exception, psycopg2.Error) as error:
            return "Error while fetching data from PostgreSQL"+ error

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                return "PostgreSQL connection is closed"
