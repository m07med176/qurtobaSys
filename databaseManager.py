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
            create_mandop = """CREATE TABLE "customers_mandopinfo" (
                            "id" INTEGER NOT NULL DEFAULT 'nextval(''customers_mandopinfo_id_seq''::regclass)',
                            "code" INTEGER NULL DEFAULT NULL,
                            "email" VARCHAR(100) NULL DEFAULT NULL,
                            "name" VARCHAR(100) NOT NULL,
                            "phone" VARCHAR(11) NULL DEFAULT NULL,
                            "region" VARCHAR(50) NULL DEFAULT NULL,
                            "date" DATE NULL DEFAULT NULL,
                            "time" TIME NULL DEFAULT NULL,
                            PRIMARY KEY ("id")
                        );"""

            create_customer = """CREATE TABLE "customers_customerinfo" (
            "id" INTEGER NOT NULL DEFAULT 'nextval(''customers_customerinfo_id_seq''::regclass)',
            "name" VARCHAR(100) NOT NULL,
            "surName" VARCHAR(50) NULL DEFAULT NULL,
            "shopName" VARCHAR(45) NULL DEFAULT NULL,
            "deviceNo" INTEGER NULL DEFAULT NULL,
            "shopKind" VARCHAR(50) NULL DEFAULT NULL,
            "phoneNo" VARCHAR(11) NOT NULL,
            "address" TEXT NULL DEFAULT NULL,
            "accounts" TEXT NULL DEFAULT NULL,
            "date" DATE NULL DEFAULT NULL,
            "time" TIME NULL DEFAULT NULL,
            "seller_id" INTEGER NOT NULL,
            "area" VARCHAR(50) NULL DEFAULT NULL,
            PRIMARY KEY ("id"),
            UNIQUE INDEX "customers_customerinfo_deviceNo_key" ("deviceNo"),
            INDEX "customers_customerinfo_seller_id_bec685fc" ("seller_id"),
            CONSTRAINT "customers_customerin_seller_id_bec685fc_fk_customers" FOREIGN KEY ("seller_id") REFERENCES "public"."customers_mandopinfo" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION
        )
        ;"""
            create_record = """CREATE TABLE "transactions_record" (
            "id" INTEGER NOT NULL DEFAULT 'nextval(''transactions_record_id_seq''::regclass)',
            "type" VARCHAR(50) NOT NULL,
            "value" DOUBLE PRECISION NOT NULL,
            "isDone" BOOLEAN NULL DEFAULT NULL,
            "isDown" BOOLEAN NULL DEFAULT NULL,
            "date" DATE NOT NULL,
            "time" TIME NOT NULL,
            "customerData_id" INTEGER NOT NULL,
            PRIMARY KEY ("id"),
            INDEX "transactions_record_customerData_id_4e0f660f" ("customerData_id"),
            CONSTRAINT "transactions_record_customerData_id_4e0f660f_fk_customers" FOREIGN KEY ("customerData_id") REFERENCES "public"."customers_customerinfo" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION
        )
        ;"""
            create_rest = """CREATE TABLE "transactions_rest" (
            "id" INTEGER NOT NULL DEFAULT 'nextval(''transactions_rest_id_seq''::regclass)',
            "value" DOUBLE PRECISION NULL DEFAULT NULL,
            "date" DATE NULL DEFAULT NULL,
            "time" TIME NULL DEFAULT NULL,
            "customer_id" INTEGER NOT NULL,
            PRIMARY KEY ("id"),
            UNIQUE INDEX "transactions_rest_customer_id_key" ("customer_id"),
            CONSTRAINT "transactions_rest_customer_id_0fd5bfec_fk_customers" FOREIGN KEY ("customer_id") REFERENCES "public"."customers_customerinfo" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION
        );"""

            drop_rest = 'DROP TABLE IF EXIST "transactions_rest" CASCADE ;'
            drop_record = 'DROP TABLE "transactions_record" CASCADE ;'
            drop_customer = 'DROP TABLE "customers_customerinfo CASCADE ";'
            drop_seller = 'DROP TABLE IF EXISTS "customers_mandopinfo CASCADE ";'
            #result = data['database']
            cursor.execute(drop_seller)
            cursor.execute(create_mandop)

            
            return "تم رفع الداتابيز بنجاح "

        except (Exception, psycopg2.Error) as error:
            print( "Error while fetching data from PostgreSQL ", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()


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

    def accounts(self,id=0,deviceNo='',dateFrom='',dateTo=''):
        customer = ''
        if deviceNo != '' and deviceNo.isdigit():
            customer = f" accounts.accountno = {deviceNo} "
        else: 
            customer = f" accounts.customer = '{deviceNo}' "
        filter = "";
        if id == 0:
            filter = "";
        elif id == 1:
            filter = " WHERE accounts.date = CURRENT_DATE "
        elif id == 2:
            filter = f" WHERE {customer} "
        elif id == 3:
            filter = f" WHERE accounts.date = '{dateFrom}' "
        elif id == 4:
            filter = f" WHERE ( {customer} )  AND accounts.date = '{dateFrom}' "
        elif id == 5:
            filter =f" WHERE accounts.date >= '{dateTo}' AND accounts.date <= '{dateFrom}' "
        elif id == 6:
            filter0 = f" WHERE ( {customer} ) "
            filter = filter0+f" AND (accounts.date >= '{dateTo}' AND accounts.date <= '{dateFrom}') "
        try:
            connection = psycopg2.connect(
                host="ec2-34-254-69-72.eu-west-1.compute.amazonaws.com",
                database="d84lv9hqj4cvad",
                user="pkekjaplofajah",
                password="5f23b729fd13ec1e966727ead1da9717e48c44bd830a6753ee23f54e14d3b099")
            cursor = connection.cursor()
            sql = "SELECT * FROM accounts "+filter
            cursor.execute(sql)
            data =  cursor.fetchall()
            allData = []
            for i in data:
                row = {
                    "seller":i[0],
                    "customer":i[1],
                    "accountno":i[2],
                    "date":i[3],
                    "fawry":i[4],
                    "aman":i[5],
                    "bee":i[6],
                    "tayer":i[7],
                    "cash":i[8],
                    "another":i[9],
                    "down":i[10],
                    "summition":i[11],
                    "rest":i[12]
                    
                }
                allData.append(row)
            return allData

        except (Exception, psycopg2.Error) as error:
            print(sql)
            print( "Error while fetching data from PostgreSQL"+ str(error))
            return []

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()


if __name__ == '__main__':
    db = DatabaseManager()
    result = db.accounts()
    print(result)