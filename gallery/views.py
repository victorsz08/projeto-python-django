from django.shortcuts import render



def index(request):
    datas = {
        1: {
            "name": "Nebulosa de Carina",
            "subtitle": "Fonte: Nasa / James Webb"
        },
        2: {
            "name": "Galaxia NGC 1079",
            "subtitle": "Fonte: Nasa / Hubble"
        }
    }
    return render(request, 'gallery/index.html', {"cards": datas} )

def image(request):
    return render(request, 'gallery/imagem.html')