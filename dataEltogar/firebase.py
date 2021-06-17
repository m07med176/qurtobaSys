                                ## Imports ##
#)Firebase
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import os

class FirebaseServer:
        # ---------------- add item ---------------- #
        def addSubjectItem(self,name,descrioption,urlImage):
                        ref = db.reference("Subject")
                        key = ref.push().key       
                        ref.child(key).set({
                                        'subjectId':f'{key}',
                                        'subjectName':f'{name}',
                                        'subjectDescription':f'{descrioption}',
                                        'subjectImage':f'{urlImage}'
                                        })
        # ---------------- get all items ---------------- #
        def getAllData(self):
                        firebase_admin.get_app()
                        ref = db.reference("customersdata/alldata")
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

        # ---------------- Querry mandop ---------------- #
        def getMandopData(self,mandopName):
                ref = db.reference("customersdata/alldata")
                querry = ref.order_by_child("nameOfMandoop").equal_to(mandopName)
                return [val for _,val in querry.get().items()]
        # ---------------- Justify json ---------------- #

        def justifyJson(self,data):
                return 
                        
