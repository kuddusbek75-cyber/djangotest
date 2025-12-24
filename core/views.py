from django.shortcuts import render, HttpResponse

# Контекст в шаблонах, ссылки

def main_view(request):
    return render(request, 'main_page.html', {})

def contacts_view(request):
    return render(request, 'contacts_page.html', {})

# request - запрос
# response - ответ
# return HttpResponse(f"{request.__dict__}")

# def test(request):
#     return render(request, 'index.html', {})

# def test2(request):
#     return HttpResponse("Саламчик!")