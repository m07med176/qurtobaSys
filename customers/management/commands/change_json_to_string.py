from customers.models import CustomerInfo
import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):


    def decodeJsonToCSV(self,data):
        if data == None: return ""
        if data == "":   return ""

        result = ""
        try:
            jsonData  = json.loads(data)
            for k,v in jsonData.items(): result+=k+","+v+"\n"
            return result
        except Exception:
            return None



    def handle(self, **options):
         
        for n,customer in enumerate(CustomerInfo.objects.all()):
            result = self.decodeJsonToCSV(customer.accounts)
            if result == None: 
                print("problem happend")
                break
            customer.accounts = result
            customer.save()
            print("done " +str(n))

