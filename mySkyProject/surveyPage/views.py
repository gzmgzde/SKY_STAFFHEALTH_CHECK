from django.shortcuts import render, redirect
from .models import Vote, HealthCard


def survey(request):
    return redirect('survey_question', question_number=1)

def survey_question(request, question_number):
    if question_number < 1 or question_number > 14:
        return redirect('survey')

    # Get health card for the current question
    health_cards = HealthCard.objects.all().order_by('health_card_id')
    questions = [{'number': i+1, 'health_card': card} for i, card in enumerate(health_cards)]
    
    try:
        current_question = next(q for q in questions if q['number'] == question_number)
    except StopIteration:
        return redirect('survey')

    # For question 14, render completion page (surveyQ14.html) without form processing
    if question_number == 14:
        template_name = 'surveyQ14.html'
        context = {
            'current_question': current_question,
            'question_number': question_number,
            'total_questions': 14
        }
        return render(request, template_name, context)

    # Handle form submission for questions 1-13
    if request.method == 'POST':
        vote_value = request.POST.get('vote_value')
        vote_comment = request.POST.get('vote_comment')
        health_card_id = request.POST.get('health_card_id')
        user_id = request.POST.get('user_id')  # Replace with request.user.id in production
        if vote_value and health_card_id and user_id:
            Vote.objects.create(
                vote_value=int(vote_value),
                vote_comment=vote_comment,
                health_card_id=health_card_id,
                user_id=user_id
            )
        # Redirect to next question (or question 14 for completion)
        return redirect('survey_question', question_number=question_number + 1)

    # Render question template for questions 1-13
    template_name = f'surveyQ{question_number}.html'
    context = {
        'current_question': current_question,
        'question_number': question_number,
        'total_questions': 14
    }
    return render(request, template_name, context)