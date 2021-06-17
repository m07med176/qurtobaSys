                                ## Imports ##
#)Firebase
from datetime import time
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import os
import json
import pandas as pd
import io 


class FirebaseManager:
        # ---------------- get all items ---------------- #transactions
        def getAllSellers(self):
                firebase_admin.get_app()
                #.equal_to(subjectId) order_by_child
                ref = db.reference().child('sellers').get()
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
                                        tableRaw["customerName"] = customer[1]
                                        tableRaw["deviceNo"] = deviceNo
                                        tableRaw["rest"] = singleRest
                                        tableRaw["lastTrans"] = trans[2]
                                        tableRaw["date"] = trans[6]
                                        tableRaw["time"] = trans[7]

                                        tableRaw["phoneNo"] = customer[5]
                                        tableRaw["area"] = customer[4]
                                        tableRaw["address"] = customer[3]
                                        dataTable.append(tableRaw)
                                
                        except Exception as e:
                                #print(e)
                                continue
                return dataTable
                #customers = [i.get('Customers') for i in csv]

