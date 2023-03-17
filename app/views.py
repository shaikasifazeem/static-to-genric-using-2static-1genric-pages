from django.shortcuts import render
def rain(request):
    return render(request,'rain.html')

def water(request):
    return render(request,'water.html')
