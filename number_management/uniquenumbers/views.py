import requests
from django.http import JsonResponse
def index(request):
    urls = request.GET.getlist('url')
    result = set()
    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()
            numbers=data.get('numbers',[])
            result.update(numbers)
        except requests.exceptions.Timeout:
            print(f"URL {url} timed out and will be ignored")
        except Exception as e:
            pass  
    output=list(result)
    return JsonResponse({'numbers': output})
