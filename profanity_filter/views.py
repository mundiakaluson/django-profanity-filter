from django.shortcuts import render, HttpResponse

def content_check(request):
    words = "Fuck off Slut Kids Motherfucker Wow Hey bitch Hey niggah"
    other_words = "Stupid mallakas. Cock suckers bloody bitches!"
    return render(request, 'main/index.html', {'words': words, 'other_words': other_words})