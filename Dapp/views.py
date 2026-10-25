from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads 

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body = request.body   #get value from the request bod
        form_data = loads(request_body) #convert jason format to python dictionary
        n1= form_data.get('num1') # get value of num1 from the dictionary
        n2= form_data.get('num2') # get value of num2 from the dictionary
        result = n1+n2
        print(request_body) # print the request body to the console for debugging
        print(type(request_body))
        data={
            "sum":result
        }
        return JsonResponse(data)
@method_decorator(csrf_exempt,name='dispatch')
class SubstractionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result=n1-n2
        print(request_body)
        data={
            "substraction":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result=n1*n2
        print(request_body)
        data={
            "multiplication":result
        }
        return JsonResponse(data)
@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result=n1/n2
        print(request_body)
        data={
            "division":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class FloordivisionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result=n1//n2
        print(request_body)
        data={
            "floordivision":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('score')
        n2=form_data.get('total')
        result=(n1/n2)*100
        print(request_body)
        data={
            "percentage":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class BMIView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('weight')
        n2=form_data.get('height')
        result=n1/((n2/100))**2
        print(request_body)
        data={
            "BMI":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class RectangleView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('length')
        n2=form_data.get('breadth')
        result=n1*n2
        print(request_body)
        data={
            "area":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class Age_calculatorView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('birth year')
        n2=form_data.get('current year')
        result=n2-n1
        print(request_body)
        data={
            "age":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class PrincipleinterestView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('principle')
        n2=form_data.get('rate')
        n3=form_data.get('time')
        result=(n2*n1*n3)/100
        print(request_body)
        data={
            "principle":n1,
            "rate":n2,
            "time":n3,
            "simple intrest":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ElectricityBillView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get('units')
        n2=form_data.get('rate')
        result=n1*n2
        print(request_body)
        data={
            "units":n1,
            "rate":n2,
            "electricity bill":result
        }
        return JsonResponse(data)
