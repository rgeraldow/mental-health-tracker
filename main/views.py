from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245623',
        'name': 'Rogerio Geraldo Wibhowo',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
