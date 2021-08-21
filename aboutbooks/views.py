from django.shortcuts import render


def main(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'main.html', ctx)


def perword(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'perword.html', ctx)
def persilent(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'persilent.html', ctx)
def subsilent(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'subsilent.html', ctx)
