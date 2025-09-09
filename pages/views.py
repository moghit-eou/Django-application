from django.shortcuts import render , HttpResponse

def home(request):
    print("\n\n main page \n\n")
    return render(request, "home.html")  


def response_example(request):
     
    first = request.GET.get("first_number")
    second = request.GET.get("second_number")

    try :
        first = int(first)
        second = int(second)
        result = first + second
    except (TypeError, ValueError):
        return HttpResponse("Invalid input. Please provide two numbers.")

    return render(request,"base.html",{"the_result":result})