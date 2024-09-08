from typing import Any
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets

class Institute(viewsets.ModelViewSet):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def create_new_institute(self,request):
        try:
            print("cdbe")
            response = {'data':'data','status':200}
            return Response(response['data'],response['status'])
        except Exception as e:
            print("chebdh")
            response = {'data':'data','status':500}
            return Response(response['data'],response['status'])
    
    def list_all_institute(self,request):
        try:
            print("cdbe")
            data =[{
                'name':'Notre Dame Academy',
                'address':'Pipal Pati Road',
                'city':'Munger',
                'district':'Munger',
                'pincode':'811201',
            }]
            response = {'data':data,'status':200}
            return Response(response['data'],response['status'])
        except Exception as e:
            print("chebdh")
            response = {'data':'data','status':500}
            return Response(response['data'],response['status'])
    
    

