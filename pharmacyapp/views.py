from django.shortcuts import render, redirect, get_object_or_404
from pharmacyapp.forms import BoardForm, ScoreForm
from pharmacyapp.models import Pharmacy, Score, Board
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required


# Create your views here.
def create_review(request, pharmacy_id):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = board_form.save()
            board.user = request.user
            board.pname_id = pharmacy_id
            board.save()
            return redirect('list_review')  # list에 맞게 수정
    else:
        board_form = BoardForm()
    return render(request, 'review_create.html', {'board_form': board_form})


def create_score(request, pharmacy_id):
    if request.method == 'POST':
        score_form = ScoreForm(request.POST)
        if score_form.is_valid():
            score = score_form.save(commit=False)
            score.user = request.user
            score.pharmacy_id = pharmacy_id
            score.save()
            return redirect('pharmacy_detail', pk=pharmacy_id)
    else:
        score_form = ScoreForm()
    return render(request, 'score_create.html', {'score_form': score_form})


#전체 게시글 조회
def review_list_view(request):
    reviews = Score.objects.all()
    paginator = Paginator(reviews, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'reviews':page_obj,

    }
    return render(request, 'review_list.html', context)

#개별 게시글 조회
def board_detail_view(request, pk):
    board = get_object_or_404(Board, pk=pk)  # 주어진 pk에 해당하는 Board 객체를 가져옵니다.

    context = {
        'board': board,  # 템플릿에 전달할 컨텍스트
    }

    return render(request, 'board_detail.html', context)  # 템플릿을 렌더링합니다.

@login_required
def delete_score(request, score_id):
    score = get_object_or_404(Score, id=score_id)
    if request.user == score.user:
        if request.method == 'POST':
            pharmacy_id = score.pharmacy.id
            score.delete()
            return redirect('pharmacy_detail', pk=pharmacy_id)
        return render(request, 'score_delete_confirm.html', {'score': score})
    else:
        return redirect('pharmacy_list')


def dashboard():
    return None


class SignUpView(View):
    pass