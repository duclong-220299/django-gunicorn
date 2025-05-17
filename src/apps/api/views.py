from django.http import JsonResponse

def example_view(request):
    data = {
        "message": "Hello, this is the API response!"
    }
    return JsonResponse(data)