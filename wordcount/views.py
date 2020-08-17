from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
# render(request객체, 템플릿이름, (선택)사전형객체)


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    # .split() : 문자열을 공백 기준으로 나눠서 리스트 형태로 저장하는 함수
    words = text.split()
    # 총 단어수 = len(words)
    word_dictionary = {}

    # 반복문을 통해 word_dictionary에 단어 및 단어등장횟수 등록하기
    for word in words :
        if word in word_dictionary:
            # increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})
# .items() : 딕셔너리의 키와 값을 쌍으로 잘라서 보내줌

