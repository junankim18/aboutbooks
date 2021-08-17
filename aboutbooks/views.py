from django.shortcuts import render


def main(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'main.html', ctx)
