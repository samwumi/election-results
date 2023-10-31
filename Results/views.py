from django.shortcuts import render, get_object_or_404

from .models import AnnouncedPuResults
from django.db.models import Sum
from .models import Party
from .forms import PollingUnitResultForm
from django.shortcuts import render, redirect


def polling_unit_result(request, polling_unit_id):
    results = AnnouncedPuResults.objects.filter(polling_unit_id=polling_unit_id)
    return render(request, 'polling_unit_result.html', {'results': results})

from django.shortcuts import render
from .models import PollingUnit

def view_lga_total_results(request):
    
    selected_lga_id = request.GET.get('lga_id')
    
    
    polling_units = PollingUnit.objects.filter(lga_id=selected_lga_id)
    
    


    parties = Party.objects.all()
    total_results = {party.partyname: 0 for party in parties}

    for unit in polling_units:
        for party in parties:
            unit.results.filter(party=party.partyid)
            party_results = unit.results.filter(party=party.partyid)
        
        party_total = party_results.aggregate(Sum('result'))['result__sum']
        total_results[party.partyname] += party_total


    return render(request, 'lga_total_results.html', {'total_results': total_results})


def add_polling_unit_result(request):
    if request.method == 'POST':
        form = PollingUnitResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polling_unit_results')
    else:
        form = PollingUnitResultForm()

    return render(request, 'add_polling_unit_result.html', {'form': form})

