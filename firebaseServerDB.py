                                ## Imports ##
#)Firebase
from datetime import time
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import collections
import os
import json
import pandas as pd
import io 
import re

class FirebaseServerice:
        def __init__(self):
            self.deviceNom = []
            try:
                self.initTransactions = firebase_admin.get_app('qurdoba')
            except ValueError:
                self.initTransactions = self.transactions()
            try:
                self.initDataEltogar = firebase_admin.get_app('Data Eltogar')
            except ValueError:
                self.initDataEltogar = self.dataEltogar()

        # ------------ Server ------------ #
        def dataEltogar(self):
                self.REALDB_URL = "https://data-eltogar-default-rtdb.asia-southeast1.firebasedatabase.app/"
                        ## config ##
                cred = credentials.Certificate({
                "name":"Data Eltogar",
                "type": "service_account",
                "project_id": "data-eltogar",
                "private_key_id": "e363581c4c160b5dd51e7ba1407101fffe828ef5",
                "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCLvCN8e7sqvABQ\n5XK0lo4BmNE8qmlsr3TaEojTMSKa945kUOvpjQ85A30xcsdbLC0HVkwDMQp3CTWj\njGUkWNb//37SlZclCe7WWPx8ApjrvNF2dxffskJkgYyNhlMsTODMOZVj5bPhxnmq\nc/NPv+7NxFxDzGVGX9FMVLjtRYzj+o+2pEXPfm28q1cWdPLNnjO4htyn/VUksyzv\n1k4mqaH7sFw8q2dW8bt2oKS23xPQfk2X/0yfZ5iY7nX/McXTYquIAoNWfIWqJ0o2\nL2OAyWlIe3tt/ou6UW6+ahsFsJgIDMA6BzmUpjsPGkvY9FCJPfWfWzNU0rNfqNEO\n6ezQ8W39AgMBAAECggEAHVNctzFYdH2EK3Yb/p5iKx+hOfQhr/eatHGTWY9ETfWK\nYq9A84DxIuwCiDAoeo/o21NXHIxcP+Mk6K/8QgaLCKrcOOHAGLve7gk64+O/qCm2\nZABWeFH28RTnJIR+TBvOSc4D9jUs7UM0IXu4IpKLUY/WNTxePMi7KiPVs6YXDXkm\n4RxLHy+gJHuxKYLobg3aEUzIf2ZwPEsEBxiYj+kui/oKcIeX9r7PeWo0piyQJbNT\ncffX71gtow6P0mkp/OIhaVeInDk2kvyF7KpB7bi9e4XyO0TmX3zCvoLTW9WbbAc3\nxy7Xzd5cSh6NlY0pka2nB9bGnBZJ07FyTcUvcJnmwQKBgQDEvYaTDVJnMv45RPqQ\nF9UuJqzBPz5qg5muzGO1frqTxhwFDcOqp+Y5aAoXfIaKKNFQHtn7+Yt0MhxK8n2r\nN2td6uaqQ7+qFpMuaJzLgfwdrTnHh9ac4C2k8FNZ2t8tq+86pN618L4TN7RX8pTo\nh8tQyeux+iIZ5K5UTDX7/rRG+QKBgQC10vmo3b3/1c43cbuRjyPQBJo7WGLm2xxj\n7frsLj+Q2W9xOwC+ULz+y6mcJfX+6Rc/aaxVdxC5Plplsu817pE5q68AWcRv15G1\nj0DydClecAxmfArKxfrMdiuQ6SJbjQSMDWwid+c42DOXlCCpD2wBKZspmP0Zf9TQ\nrnYywGuMJQKBgQC+hS7SLt9ysq3/9a2TZpD5/VfkWANwkHp+DM4uD0hNHFc8CaVH\nGQrY4siLD/sVxgtUxFuiKHmEj5ZYedV6vdNKgtTXY34zD2N+WK4mYX0tm/fNIt2Q\n04NAK777z/m6N7sWllxZ4oWfBJ2vYWoUeJRKaw/FLY5idtLfLWJF4tTfuQKBgB1T\n8Xc+hSYeC4w/6RxadVFZXLNT12gbUaIAweeUsiYgHGysMrt/9Gw415vbN6mtWVWe\nKvECKo1mtFgRG6qcV4pw2eJ5mEjeAZ/CgpxZBk84TZe+TFNWydRu/yn5oNQZk/Ev\nPRD2PDKcFP5PI1GBrk8lseRsy+5wAxjB+0jGZtKNAoGBALSxM7xJKnWQ/ygPRnCf\naQqL8qfxp3s9zEjzMlnBHDDjpuLWMmc+jft4lDHNHBDfxIJMkL3CS9ZBWxad9yd4\ncNonNUDY6S9DfLiv4NwSzb6Y6u7A/qjNnpcMOKrJY8RdCSJwu+O26+OvN2wWGnkr\nzN7p+qSVOni9j4C3axyk8L5d\n-----END PRIVATE KEY-----\n",
                "client_email": "firebase-adminsdk-u5wn7@data-eltogar.iam.gserviceaccount.com",
                "client_id": "108657792726570775375",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-u5wn7%40data-eltogar.iam.gserviceaccount.com"
                }
                )

                return firebase_admin.initialize_app(cred,{ 'databaseURL':self.REALDB_URL},name="Data Eltogar")

        def transactions(self):

                self.REALDB_URL = "https://qurdoba-9eac4-default-rtdb.firebaseio.com/"

                                ## config ##
                #if not firebase_admin._apps:
                cred = credentials.Certificate({
                                                "name":"qurdoba",
                                                "type": "service_account",
                                                "project_id": "qurdoba-9eac4",
                                                "private_key_id": "2c93a85a9c4fb75dfc984e84eeb0ad2962c5c05d",
                                                "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDjl9l2oLiKwK69\nW+kO6SRHOrQGF0xGVn4Te+pwSkOrV0ARhSbZ3DCgyypN75NN1s2lMPvU3pPJR40n\ngmPazQRo+3RGeuNdRBwXEU9ignmAP/vIToo282oimjchXmNQ0QI/dRzxKuEHyDr0\nxXjkT/vPEfpUB2QedFAvNHPh0haIgy3SRxVJ85k0RzELnfDwlSbzSp5ehQ1bEE2d\nA//Oc3Q6mOBSKB/iY5U9g0rnTsYoR0JRzc8uxpOgFnIPrOunNdryn0sqFzmHT0Vc\nTqcVLMF1HYgPdPRjtkJjq1d3kI/FOXZAcqs2xsGIZdq8NJCNiXf7DuKQ3iCXD61p\nboMQQVYjAgMBAAECggEAaiiFNdEn4wiXORoq7lqPIm5eVEz/tftYGWx+YNwzDjPH\nXaS3B32ubQH2/J1YH0GncHsVrCgZ1RP74kbunrtsaC+J/+oILZO8aoIXfkKPu+Oc\nZMVFsPX/Np6qQnVNa//hxYmx80fl6QRbg5qslgo80Ux4cEN2TsJAOJSFzPp6qjds\nYEAW6MnIKvp9SfMDl53freT0vvl104GnUpYpC1iLHNHCB7Myszp1HRt11n5dkNtY\ncRNnXBaHIZOrASf3nU2BRqrWyyeWsS9iTprn2egdMLBGkAHskK85mvfQvPSgsRLV\n934jIV/0qbLxG7sCQMNQ8khoM0ZhMhp0Z1/+PofuWQKBgQD+0aRZgJdSlti1lSWT\nzPQhEGeWybnUyP9mnb41/YvTm8F7o2JpCbNFArZh9wz++PcEhS0DBLCEzpVWJ7o3\nlLAr2TEqySlqrrpXoYSDQW4aSf+AMTJaBdhBWuTnfbabKmsYyKj1jZFveNSba58d\nUlN2lKMXKYqKULcivZ05fTDsRwKBgQDkpecI26twuVRzvOFiRHhJdkfyAC/ImpQw\n1UU9HKOJ9uRVSVrxxjJOz0aENd9X/qiKI0FVPg9ui99AD2rUQNcuA23uFNoP7Rcb\nJyuqX5UW7YCSQ0TvR2q8K07cRL3Pz0a7PiddYZBRSO14Cbnnici6pbZqZ4w6aS/L\npnrKWD+hRQKBgQDVUwpkx2tnf9NiiL8RsgY62/Hs4WpKQg7WiH5h0qZJe96JtClB\nyBYlUvT+pIVju2eIiDk7iqSAOjX5D38s4rRtsQEhUZDzt91WWWiHPbKAHazhU85U\nYQo/BGoXhj3mPqez8uDH2UGE8cIDbyCgungXEK5MSMGrs5Dta5IBO9ZGJwKBgDB+\nr33FeZsy86KIkRUSiKCsIZ5GQ9w8TOn+kezgQh9k6hDcuhlFfC4S8FXiRziWnpCN\n4bF+tC8yI2um2XWjOwBbYdl5OrbeBmSP7kb4dtqiDP74nYpSj2TRmqxFOCz3PX1B\nNYAszTswSI2JIpDlPFm6A/KVe7x3ytdau/hmtzgxAoGBAOGrsUmSUa7NyIiR/Fox\nm42dpfplcv0RpIAznPlQWsqel2FYOV7ceUroaOZcqPnD+7zuSLgxn8WO9AAZ7aaQ\nbz1O4jtfrmobtPlfguA0Xj0/aKTT/M5F4Qe7IoU9iWOM4WadWSIe797KRgy/JAdh\nxCbq1TxUP8uyIE72PCrZeI9J\n-----END PRIVATE KEY-----\n",
                                                "client_email": "firebase-adminsdk-8z6ie@qurdoba-9eac4.iam.gserviceaccount.com",
                                                "client_id": "110142186399434571201",
                                                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                                "token_uri": "https://oauth2.googleapis.com/token",
                                                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                                                "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8z6ie%40qurdoba-9eac4.iam.gserviceaccount.com"
                                                }
                )
                return firebase_admin.initialize_app(cred,{ 'databaseURL':self.REALDB_URL },name="qurdoba")

        # ---------------- Manadeep Customer ---------------- #
        def getDublicatedNo(self):
                if len(self.deviceNom) > 0:
                        dublicates = [item for item, count in collections.Counter(self.deviceNom).items() if count > 1]
                        print(dublicates)
                        return {"state":True,
                                "content":dublicates}
                else:
                        return {"state":False,
                                "content":[]}
        def getAllMandopCustomer(self):
                #.equal_to(subjectId) order_by_child
                # root
                ref = db.reference(app=firebase_admin.get_app('qurdoba')).child('sellers').get()
                data = [val for _,val in ref.items()]
                # manadeep name
                names = [i.get('user_name') for i in [ i['user_info'] for i in data]]
                namesEmail =  [[email,val["user_info"].get('user_name')] for email,val in ref.items()]
                # get each mandop database
                csv = [val.get('DataBases') for _,val in ref.items()]
                customerHead = "id,name,deviceNo,phoneNo,area,address,a\n"

                mainCustomers = pd.concat(
                        [pd.read_csv(  io.StringIO( customerHead + data['Customers'])  , sep=",", error_bad_lines=False) for data in csv if data is not None] 
                        )
                dublicates  = list(set(mainCustomers[mainCustomers['deviceNo'].duplicated(keep=False)]['deviceNo'].values.tolist()))
                dataTable = []
                for customer in mainCustomers.values.tolist():
                        tableRaw = {}
                        deviceNo = customer[2]                                        
                        nameOfM = "غير معروف" #names[n].replace("-","")
                        tableRaw["mandopName"] = re.sub("\d","",nameOfM)
                        tableRaw["customerName"] = customer[1] #" ".join(customer[1].split(" ")[0:2])
                        tableRaw["deviceNo"] = deviceNo
                        try:
                                tableRaw["phoneNo"] = "0" + customer[5]
                        except TypeError as e:
                                tableRaw["phoneNo"] = ""
                        tableRaw["area"] = customer[4]
                        tableRaw["address"] = customer[3]
                        dataTable.append(tableRaw)                                
                        
                # for n,i in enumerate(csv):
                #         try:
                #                 # if name is none
                #                 if names[n] is None:
                #                         continue
                #                 try:
                #                         customers = pd.read_csv(  io.StringIO( customerHead + i['Customers'])  , sep=",")
                #                 except Exception as e:
                #                         continue
                #                 # if name in this black list (:
                #                 if names[n] in ['قرطبة للإتصالات','عطيه',"6-الكنانى","5-منير"]:
                #                         continue
                #                 for customer in customers.values.tolist():
                #                         tableRaw = {}
                #                         deviceNo = customer[2]                                        
                #                         nameOfM = names[n].replace("-","")
                #                         tableRaw["mandopName"] = re.sub("\d","",nameOfM)
                #                         tableRaw["customerName"] = " ".join(customer[1].split(" ")[0:2])
                #                         tableRaw["deviceNo"] = deviceNo
                #                         try:
                #                                 tableRaw["phoneNo"] = "0" + customer[5]
                #                         except TypeError as e:
                #                                 tableRaw["phoneNo"] = ""
                #                         tableRaw["area"] = customer[4]
                #                         tableRaw["address"] = customer[3]
                #                         dataTable.append(tableRaw)                                
                #         except Exception as e:
                #                 continue
                if len(dublicates) > 0:
                        return {"state":True,
                                "content":dublicates,
                                "all_data":dataTable,
                                "manadeep":namesEmail}
                else:
                        return {"state":False,
                                "content":[],
                                "all_data":dataTable,
                                "manadeep":namesEmail}
                #customers = [i.get('Customers') for i in csv]
        def collectCustomers(self,email):
                #.equal_to(subjectId) order_by_child
                # root
                ref = db.reference(app=firebase_admin.get_app('qurdoba')).child('sellers').get()
                data = [val for _,val in ref.items()]
                # manadeep name
                names = [i.get('user_name') for i in [ i['user_info'] for i in data]]
                namesEmail =  [[email,val["user_info"].get('user_name')] for email,val in ref.items()]
                # get each mandop database
                csv = [val.get('DataBases') for _,val in ref.items()]
                customerHead = ""
                dataTable = []
                for n,i in enumerate(csv):
                        try:
                                # if name is none
                                if names[n] is None:
                                        continue
                                # if name in this black list (:
                                if names[n] in ['قرطبة للإتصالات','عطيه',"6-الكنانى","5-منير"]:
                                        continue
                                try:
                                        customerHead+= i['Customers']
                                except Exception as e:
                                        continue
                        except Exception as e:
                                continue
                db.reference(app=firebase_admin.get_app('qurdoba')).child(f"sellers/{email}/DataBases").update({ f'Customers':customerHead })

        # ---------------- Data Eltogar ---------------- #
        def getMandopData(self,mandopName):
                ref = db.reference("customersdata/alldata")
                querry = ref.order_by_child("nameOfMandoop").equal_to(mandopName)
                return [val for _,val in querry.get().items()]
        def getAllData(self):
                        ref = db.reference("customersdata/alldata",app=firebase_admin.get_app('Data Eltogar'))
                        data = []
                        for _,val in ref.get().items():
                                try:
                                        data.append(val)
                                except Exception:
                                        continue
                        return data
                        # ---------------- get single item ---------------- #  
        def getDataItem(self,itemId):
                ref = db.reference("customersdata/alldata")
                return [val for _,val in ref.child(itemId).get().items()]

        # ---------------- Manadeep Transactions ---------------- #
        def getAllSellers(self):
                #.equal_to(subjectId) order_by_child
                ref = db.reference(app=firebase_admin.get_app('qurdoba')).child('sellers').get()
                data = [val for _,val in ref.items()]
                names = [i.get('user_name') for i in [ i['user_info'] for i in data]]
                
                csv = [val.get('DataBases') for _,val in ref.items()]
                customerHead = "id,name,deviceNo,phoneNo,area,address,a\n"
                restHead = "id,deviceNo,value,date,d\n"
                transHead = "id,kind,value,name,deviceNo,f,date,time,datetime\n"
                dataTable = []
                for n,i in enumerate(csv):
                        try:
                                customers = pd.read_csv(  io.StringIO( customerHead + i['Customers'])  , sep=",")
                                rest = pd.read_csv(  io.StringIO( restHead + i['Rest'])  , sep=",") 
                                transactions =pd.read_csv(  io.StringIO( transHead + i['Transactions'])  , sep=",")
                                if names[n] in ['قرطبة للإتصالات','عطيه','3-إبراهيم',"6-الكنانى","5-منير"]:
                                        continue
                                
                                for customer in customers.values.tolist():
                                        tableRaw = {}
                                        deviceNo = customer[2]

                                        #kind = trans[1]
                                        try:
                                                singleRest = rest.loc[rest['deviceNo'] == deviceNo ].tail(1).values.tolist()[0][2]
                                        except Exception as e:
                                                singleRest = "غير معروف"
                                                #print(e,"singleRest")
                                        try:
                                                trans = transactions.loc[transactions['deviceNo'] == deviceNo ].tail(1).values.tolist()[0]
                                        except Exception as e:
                                                trans = ["غير معروف","غير معروف","غير معروف","غير معروف","غير معروف","غير معروف","غير معروف","غير معروف","غير معروف"]
                                                #print(e,"trans")
                                        tableRaw["mandopName"] = names[n]
                                        tableRaw["customerName"] = " ".join(customer[1].split(" ")[0:2])
                                        tableRaw["deviceNo"] = deviceNo
                                        tableRaw["rest"] = singleRest
                                        tableRaw["lastTrans"] = trans[2]
                                        tableRaw["date"] = trans[6]
                                        tableRaw["time"] = trans[7]

                                        tableRaw["phoneNo"] = "0"+customer[5]
                                        tableRaw["area"] = customer[4]
                                        tableRaw["address"] = customer[3]
                                        dataTable.append(tableRaw)
                                
                        except Exception as e:
                                #print(e)
                                continue
                return dataTable
                #customers = [i.get('Customers') for i in csv]
        # ----------------- Accounts of Office ------------------- #
        def getAccountOffice(self,seller,manager):
                #.equal_to(subjectId) order_by_child
                ref = db.reference(app=firebase_admin.get_app('qurdoba')).child('sellers').get()
                customerHead = "id,name,deviceNo,phoneNo,area,address,a\n"
                restHead = "id,deviceNo,value,date,d\n"
                customers = ""
                rest =""
                data = [[node,val] for node,val in ref.items() if node in [manager,seller]]
                for email,data in ref.items():
                        if email == manager:
                                rest = pd.read_csv(  io.StringIO( restHead  + data['DataBases']['Rest'] )  , sep=",").fillna('') 
                        if email == seller:
                                customers = pd.read_csv(  io.StringIO( customerHead +  data['DataBases']['Customers']  )  , sep=",", error_bad_lines=False).fillna('')                
                                

                #transHead = "id,kind,value,name,deviceNo,f,date,time,datetime\n"
                #transactions =pd.read_csv(  io.StringIO( transHead + data[0][1]['DataBases']['Transactions'] )  , sep=",")
                areas = customers['area'].unique()
                allData = []
                for area in areas:
                        header = {}
                        if area != '': areaM = area
                        else: areaM = 'غير معروف'
                        header['deviceNo'] = 0
                        header['customerName'] = areaM
                        header['phoneNo'] = '1111111111111112111111111'
                        header['rest'] = 0.0
                        allData.append(header)
                        data = customers.loc[customers['area'] == area ].values.tolist()
                        repeat = False
                        for i in data:
                                try:
                                        row = {}
                                        row['deviceNo'] = i[2]
                                        row['customerName'] = i[1]
                                        row['phoneNo'] = i[3]
                                        restN= rest.loc[rest['deviceNo'] == i[2] ].tail(1).values.tolist()
                                        if len(restN)>0:
                                                repeat = True
                                                if int(restN[0][2]) !=0:
                                                        row['rest'] = restN[0][2]
                                                        allData.append(row)       
                                except IndexError as e:
                                        continue
                        if not repeat:
                                allData.pop(-1)
                return allData
                #customers = [i.get('Customers') for i in csv]

        def getOfficeTransactions(self,manager,deviceNo):
                ref = db.reference(app=firebase_admin.get_app('qurdoba')).child(f'sellers/{manager}/DataBases/Transactions').get()
                transHead = "id,kind,value,name,deviceNo,f,date,time,datetime\n"
                transactions =pd.read_csv(  io.StringIO( transHead + ref )  , sep=",")
                transactions = transactions.loc[transactions['deviceNo'] == deviceNo ].sort_values('datetime',ascending=False).values.tolist()
                allData = []
                for trans in transactions:
                        data ={}
                        data['transections_id'] = trans[0]
                        data['transections_accountno'] = trans[4]
                        data['transections_isdone'] = trans[5]
                        data['transections_type'] = trans[1]
                        data['transections_customer'] = trans[3]
                        data['transections_date'] = trans[6]
                        data['transections_time'] = trans[7]
                        data['transections_datetime'] = trans[8]
                        data['transections_value'] = trans[2]
                        allData.append(data)
                return allData
                
if __name__ == '__main__':
        master = FirebaseServerice()
        master.getAccountOffice('ibrahim0sakr55055@gmail0com')