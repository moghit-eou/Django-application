from django.shortcuts import render , HttpResponse

def home(request):
    return render(request, "home.html")  


def calculate_api(request):
     
    first = request.GET.get("first_number")
    second = request.GET.get("second_number")

    try :
        first = int(first)
        second = int(second)
        result = first + second
    except (TypeError, ValueError):
        return HttpResponse("Invalid input. Please provide two numbers.")

    return render(request,"base.html" , {"the_result":result})