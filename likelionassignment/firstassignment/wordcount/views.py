from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')


def about(request):
        return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET.get('fulltext')
return render(request, 'wordcount/count.html', {
'fulltext': full_text
})
    return render(request, 'wordcount/count.html', {'fulltext': full_text})


