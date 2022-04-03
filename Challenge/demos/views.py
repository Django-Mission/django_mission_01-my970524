from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def lotto(request):
    return render(request, 'lotto.html')

def lotto_result(request):
    game_num = int(request.GET.get('game_num'))

    # print(f'game_num: {game_num}')
    # print(type(game_num))

    result = []

    if game_num > 1:
        for i in range(game_num):
            pull_num = [x for x in range(1, 46)]
            lotto_num = random.sample(pull_num, 6)
            result.append(lotto_num)
    else:
        pull_num = [x for x in range(1, 46)]
        lotto_num = random.sample(pull_num, 6)
        result.append(lotto_num)
    
    # print(result)
    
    return render(request, 'lotto_result.html', {'game_nums': game_num, 'lotto_nums': result})
