from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Question, Choice


def index(request):

    # pub_date 필드를 기준으로 내림차순 정렬한 결과를 latest_question_list에 할당
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    # shorcut을 이용해 잛게 처리
    return render(request, 'polls/index.html', context)

    #template = loader.get_template('polls/index.html')
    # 템플릿 로더를 이용해서 'polls/index.html'에서 템플릿 파일을 가져온다

    # 템플릿 파일에 전달할 context 객체를 정의
    #context = {
        # 'latest_question_list'라는 키에 값을 할당, 할당 키로 템플릿에서 사용가능하다.
    #    'latest_question_list': latest_question_list,
    #}
    # 템플릿에 context와 request객체를 사용해서
    #return HttpResponse(template.render(context, request))

#    output = ','.join([q.question_text for q in latest_question_list])
#    output2 = ''
    # 전부 붙인 후 마지막만 slice
#    for q in latest_question_list:
#        output2 += q.question_text + ','
#    output2 = output2[:-2]
#    return HttpResponse(output2)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    """
    Q1)
    request.method== 'POST'일 때
    전달받은 데이터 출력

    POST 형식이 아닐 경우, polls/detail.html을 render

    POST 형식으로 전달됐을 경우,
    전달받은 POST객체에서
    'choice' 키의 값을 HttpResponse로 되돌려준다

    Q2)
    1. 'choice'키로 전달된 Choice개객체의 id를 이용해서
    2. 해당 Choice객체의 votes값을 1ㄴㄹ려주고 데이터베이스에 업데이트,
    3. 완ㄹ되면 다시 Question detail 페이지로 이동
    """
    if request.method == 'POST':
        #Q1)
        # print(request.POST)
        # value = request.POST['choice']
        # return HttpResponse(value)

        # Q2) id == pk(primary key)
        choice_id = request.POST['choice']
        choice = Choice.objects.get(id=choice_id)

        choice.votes+=1
        choice.save()

        # return redirect('polls:detail', question_id=question_id)
        return redirect('polls:results', question_id=question_id)
    else:
        question = Question.objects.get(id=question_id)
        context = {
            'question': question,
        }
        return render(request, 'polls/detail.html', context)

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # Q3) 인자로 주어진 question_id에 해당하는 Quesion객체를 context에 담아 render에 보낸다
    question = Question.objects.get(id=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
