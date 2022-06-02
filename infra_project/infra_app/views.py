from django.http import HttpResponse


def index(request):
    return HttpResponse(
        ('У меня получилось! С попытки №2 На серваке 51.250.17.12'
         'через контейнер Докер!! :))) ЮЮЮЮПППИИИИИ')
    )


def second_page(request):
    return HttpResponse('А это вторая страница!')
