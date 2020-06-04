from django.http import HttpResponse

'''
helpful snippet

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data

content = JSONRenderer().render(serializer.data)
content
# b'{"id": 2, "title": "",....     } '''

def index(request):
    return HttpResponse("Hello, world. You're at the HOMEPAGE :).")