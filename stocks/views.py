from django.shortcuts import render
from django.http import JsonResponse
from stocks.models import DataTable

# Create your views here.
def home(request):
    data = "1234"
    return render(request, 'stocks/home.html', {'data':data,})

# Create your views here.
def showTable(request):
   form = DataTable.objects.all()
   contextDict = {'form':form}
   return render(request, 'stocks/showTable.html', contextDict)

def update_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('id')
        new_date = request.POST.get('date')
        new_trade_code = request.POST.get('trade_code')
        new_high = request.POST.get('high')
        new_low = request.POST.get('low')
        new_open = request.POST.get('open')
        new_close = request.POST.get('close')
        new_volume = request.POST.get('volume')

        try:
            data = DataTable.objects.get(id=data_id)
            
            data.date = new_date
            data.trade_code = new_trade_code
            data.high = new_high
            data.low = new_low
            data.open = new_open
            data.close = new_close
            data.volume = new_volume

            data.save()
            
            return JsonResponse({'success': True})
        except DataTable.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Data not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


