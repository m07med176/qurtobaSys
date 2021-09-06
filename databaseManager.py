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

if __name__ == '__main__':
    db = DatabaseManager()
    # This Python file uses the following encoding: utf-8
    data = """ INSERT INTO rest (id, value, date, time, customer_id) VALUES (10, 0.0, '2021-09-01', '16:20:46', 32),(11, 0.0, '2021-09-01', '16:21:42', 31),(12, 0.0, '2021-09-01', '16:22:18', 30),(13, 125.0, '2021-09-04', '22:11:50', 33),(14, 409.0, '2021-09-02', '16:22:55', 34),(15, 1356.0, '2021-09-01', '16:23:54', 37),(16, 375.0, '2021-09-02', '16:23:13', 36) ;\n#0# INSERT INTO record (id, type, value, isDone, isDown, date, time, customerData_id) VALUES (23, 'فورى', 1000.0, 'false', 'false', '2021-09-01', '16:19:50', 32),(24, 'تنزيل', 250.0, 'false', 'true', '2021-09-01', '16:20:09', 32),(25, 'كاش', 400.0, 'false', 'false', '2021-09-01', '16:20:17', 32),(26, 'بى', 254.0, 'false', 'false', '2021-09-01', '16:20:21', 32),(27, 'فورى', 145.0, 'false', 'false', '2021-09-01', '16:20:25', 32),(28, 'تنزيل', 1500.0, 'false', 'true', '2021-09-01', '16:20:29', 32),(29, 'تنزيل', 49.0, 'false', 'true', '2021-09-01', '16:20:32', 32),(30, 'أمان', 250.0, 'false', 'false', '2021-09-01', '16:20:39', 32),(31, 'تنزيل', 300.0, 'false', 'true', '2021-09-01', '16:20:43', 32),(32, 'أمان', 50.0, 'false', 'false', '2021-09-01', '16:20:46', 32),(33, 'أمان', 248.0, 'false', 'false', '2021-09-01', '16:21:21', 31),(34, 'فورى', 50.0, 'false', 'false', '2021-09-01', '16:21:27', 31),(35, 'كاش', 250.0, 'false', 'false', '2021-09-01', '16:21:32', 31),(36, 'بى', 254.0, 'false', 'false', '2021-09-01', '16:21:36', 31),(37, 'تنزيل', 802.0, 'false', 'true', '2021-09-01', '16:21:42', 31),(38, 'بى', 254.0, 'false', 'false', '2021-09-01', '16:21:57', 30),(39, 'كاش', 58.0, 'false', 'false', '2021-09-01', '16:22:00', 30),(40, 'فورى', 558.0, 'false', 'false', '2021-09-01', '16:22:03', 30),(41, 'بى', 55.0, 'false', 'false', '2021-09-01', '16:22:06', 30),(42, 'بى', 25.0, 'false', 'false', '2021-09-01', '16:22:10', 30),(43, 'أخرى', 50.0, 'false', 'false', '2021-09-01', '16:22:15', 30),(44, 'تنزيل', 1000.0, 'false', 'true', '2021-09-01', '16:22:18', 30),(45, 'أخرى', 254.0, 'true', 'false', '2021-09-01', '16:22:33', 33),(46, 'أمان', 251.0, 'true', 'false', '2021-09-01', '16:22:37', 33),(47, 'فورى', 748.0, 'true', 'false', '2021-09-01', '16:22:42', 33),(48, 'بى', 581.0, 'true', 'false', '2021-09-01', '16:22:46', 33),(49, 'بى', 1834.0, 'true', 'false', '2021-09-01', '16:22:53', 33),(50, 'تنزيل', 3668.0, 'true', 'true', '2021-09-01', '16:22:59', 33),(51, 'بى', 255.0, 'false', 'false', '2021-09-01', '16:23:10', 34),(52, 'تنزيل', 558.0, 'false', 'true', '2021-09-01', '16:23:10', 34),(53, 'بى', 303.0, 'false', 'false', '2021-09-01', '16:23:13', 34),(54, 'أمان', 254.0, 'false', 'false', '2021-09-01', '16:23:17', 34),(55, 'أمان', 254.0, 'true', 'false', '2021-09-01', '16:23:34', 33),(56, 'أمان', 557.0, 'false', 'false', '2021-09-01', '16:23:43', 37),(57, 'تنزيل', 55.0, 'false', 'true', '2021-09-01', '16:23:50', 37),(58, 'بى', 854.0, 'false', 'false', '2021-09-01', '16:23:54', 37),(59, 'فورى', 588.0, 'true', 'false', '2021-09-02', '16:22:03', 33),(60, 'فورى', 855.0, 'true', 'false', '2021-09-02', '16:22:05', 33),(61, 'فورى', 588.0, 'true', 'false', '2021-09-02', '16:22:03', 33),(62, 'فورى', 855.0, 'true', 'false', '2021-09-02', '16:22:05', 33),(63, 'فورى', 589.0, 'false', 'false', '2021-09-02', '16:22:47', 34),(64, 'كاش', 566.0, 'false', 'false', '2021-09-02', '16:22:51', 34),(65, 'تنزيل', 1000.0, 'false', 'true', '2021-09-02', '16:22:55', 34),(66, 'كاش', 250.0, 'false', 'false', '2021-09-02', '16:23:03', 36),(67, 'طاير', 525.0, 'false', 'false', '2021-09-02', '16:23:06', 36),(68, 'تنزيل', 200.0, 'false', 'true', '2021-09-02', '16:23:09', 36),(69, 'تنزيل', 200.0, 'false', 'true', '2021-09-02', '16:23:13', 36),(70, 'تنزيل', 3140.0, 'true', 'true', '2021-09-04', '22:11:41', 33),(71, 'فورى', 125.0, 'false', 'false', '2021-09-04', '22:11:50', 33) ;\n#0# INSERT INTO customerinfo (id, name, surName, shopName, deviceNo, shopKind, phoneNo, address, accounts, date, time, seller_id, area) VALUES (28, 'احمد', '', '', 548, '1', '68458', 'ةبا', '', '2021-09-01', '16:11:28',21 , 'منية محلة الدمنه'),(29, 'عصمت', 'عصام', '', 2540, '1', '845484', 'ةياي', '', '2021-09-01', '16:12:45',23 , 'منية محلة الدمنه'),(30, 'رمضان احمد', '', '', 845400, '1', '99464', 'ةيةي', '', '2021-09-01', '16:13:18',23 , 'محلة الدمنه'),(31, 'جودت', 'ليل', '', 645, '1', '8484', 'تية', '', '2021-09-01', '16:13:48',24 , 'محلة الدمنه'),(32, 'وليد', '', '', 25540, '1', '8548', 'غةرى', '', '2021-09-01', '16:14:20',25 , 'محلة الدمنه'),(33, 'مالك', 'مالك', '', 54540, '1', '5475', 'ةللا', '', '2021-09-01', '16:15:20',24 , 'شها'),(34, 'محمد', '', '', 5478, '1', '8556', 'ةلل', '', '2021-09-01', '16:16:02',23 , 'شها'),(35, 'حسام', 'وائل', '', 2558, '1', '853247', 'تالبتىف', '', '2021-09-01', '16:17:59',21 , 'شها'),(36, 'المحمودى', '', '', 85742, '1', '5585', 'ةىببى', '', '2021-09-01', '16:18:47',24 , 'ميت مزاح'),(37, 'مراد', '', '', 547, '1', '85712', 'اابات', '', '2021-09-01', '16:19:12',23 , 'ميت مزاح') ;\n#0# INSERT INTO mandopinfo (id, code, email, name, phone, region, date, time) VALUES (14, 250, 'mohamed.arafa176@gmail.com', 'احمد جمال', '01010286080', 'طلخا', '2021-08-31', '22:06:51'),(16, 1, '', 'عادل', '', 'المنصوره', '2021-09-01', '07:11:58'),(18, 2, '', 'معاذ', '', 'دكرنس', '2021-09-01', '07:14:15'),(20, 655, 'لللل', 'نتا', '655', 'اال', '2021-09-01', '13:55:19'),(21, 6656, '', 'جمال', '', 'دمنه', '2021-09-01', '16:08:44'),(22, 588, 'mohamed.arafa176@gmail.com', 'عدنان', '05248', 'دمنه', '2021-09-01', '16:09:10'),(23, 254, 'amal.ali.elmetwalli@gmail.com', 'معاذ', '', 'دمنه', '2021-09-01', '16:09:36'),(24, 5807, 'biteam.net@gmail.com', 'صبرى', '95247', 'دمنه', '2021-09-01', '16:10:00'),(25, 555073, '', 'عيسى', '', 'دمنه', '2021-09-01', '16:10:24') ;\n#0#"""
    result = db.insertSchema(data)
    print(result)