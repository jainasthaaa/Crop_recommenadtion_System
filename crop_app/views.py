from django.shortcuts import render
from .ml_code import predict_crop

def home(request):
    # Initialize variables
    n = p = k = temperature = humidity = ph = rainfall = ""
    result = None

    if request.method == "POST":
        n = request.POST.get('n')
        p = request.POST.get('p')
        k = request.POST.get('k')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        ph = request.POST.get('ph')
        rainfall = request.POST.get('rainfall')

        # Only predict if all fields are filled
        if n and p and k and temperature and humidity and ph and rainfall:
            result = predict_crop([[int(n), int(p), int(k), float(temperature), float(humidity), float(ph), float(rainfall)]])

    context = {
        'result': result,
        'n': n,
        'p': p,
        'k': k,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall
    }
    return render(request, 'index.html', context)
