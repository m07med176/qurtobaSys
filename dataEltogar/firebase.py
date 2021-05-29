                                ## Imports ##
#)Firebase
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import os

class FirebaseManager:
        def __init__(self):
                                 ## vars ##
                self.cirteficate = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), "data-eltogar-sdk.json")))

                
                self.REALDB_URL = "https://data-eltogar-default-rtdb.asia-southeast1.firebasedatabase.app/"

                                ## config ##
                cred = credentials.Certificate({
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
                firebase_admin.initialize_app(cred,{ 'databaseURL':self.REALDB_URL })


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
                ref = db.reference("customersdata/alldata")
                return [val for _,val in ref.get().items()]
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
                        
if __name__ == "__main__":
        dbM = FirebaseManager()
        data = dbM.getMandopData("حسن")
        dbM.justifyJson(data)


#                 push , set , update , get      #
## ref2.update({ 'child/Ahmed':"mohamed arafa" })

"""
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('height').get()
for key, val in snapshot.items():
print('{0} was {1} meters tall'.format(key, val))
"""


