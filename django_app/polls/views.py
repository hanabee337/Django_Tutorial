from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    # pub_date 필드를 기준으로 내림차순 정렬한 결과를 latest_question_list에 할당
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/index.html')
    # 템플릿 로더를 이용해서 'polls/index.html'에서 템플릿 파일을 가져온다

    # 템플릿 파일에 전달할 context 객체를 정의
    context = {
        # 'latest_question_list'라는 키에 값을 할당, 할당 키로 템플릿에서 사용가능하다.
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#    output = ','.join([q.question_text for q in latest_question_list])
#    output2 = ''
    # 전부 붙인 후 마지막만 slice
#    for q in latest_question_list:
#        output2 += q.question_text + ','
#    output2 = output2[:-2]
#    return HttpResponse(output2)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(reques, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
