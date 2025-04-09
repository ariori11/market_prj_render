from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


from .models import Accommodation
def accommodations(request):
    title = 'размещение'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }

    return render(request, 'mainapp/accommodations.html', content)


from django.shortcuts import get_object_or_404
from .models import ListOfCountries

def accommodation(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, 'mainapp/accommodation_details.html', content)


