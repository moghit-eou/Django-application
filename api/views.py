from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def ping(request):
    print ("\nPinged! from django\n")
    return JsonResponse({"ok": True})

@csrf_exempt
def add_function(request):
    print ("\n--------------------add_function is called---------------\n")
    
    if request.method != 'POST':
        
        return JsonResponse({"Error" : "error catched"})
    
 
    data = json.loads(request.body)

    
    first_number = int(data.get('a' , 0 ) )
    second_number = int(data.get('b' , 0 ) )

    print_err(first_number)
    print_err(second_number)
    print_err(type(first_number))


    sum = first_number + second_number

    return JsonResponse({"sum" : sum * 100})

def print_err(data):
    print (f"\n -------------\n{data}\n -------------")