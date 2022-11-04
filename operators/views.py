from math import factorial
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Additionviews(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response (data=res) 
# class Factorialviews(APIView):
#     def post(self,request,*args,**kwargs):          
#          n1=request.data.get("num")                  
#          res=factorial(n1)                           
#          return Response (data=res)                  

class Factorialviews(APIView):
    def post(self,request,*args,**kwargs):          
         n1=request.data.get("num") 
         fact=1
         for i in range(1,(n1+1)):
            fact=fact*i
         return Response(data=fact)

# class Primeornotviews(APIView):
#     def post(self,request,*args,**kwargs):          
#          n1=request.data.get("num") 
#          fact=1
#          for i in range(1,(n1+1)):
#             fact=fact*i
#          return Response(data=fact)       
class Substractionview(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response (data=res)        
class Multiplicationviews(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1*n2
        return Response (data=res)    

class Divisionviews(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1/n2
        return Response (data=res)                                                                       