from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def lotto(request):
    pull_num = [x for x in range(1, 46)]
    lotto_num = random.sample(pull_num, 6)
    print(lotto_num)

    return render(request, 'lotto.html', {'lotto_num': lotto_num})