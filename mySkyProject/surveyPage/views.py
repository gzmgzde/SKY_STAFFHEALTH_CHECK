from django.shortcuts import render, redirect
from .models import Vote, HealthCard

def survey(request):
    return redirect('survey_question', question_number=1)

def survey_question(request, question_number):
    health_cards = HealthCard.objects.all().order_by('health_card_id')

    # If no health cards in DB, show an error page instead of looping redirects
    if not health_cards.exists():
        return render(request, 'no_health_cards.html')

    total_questions = health_cards.count()

    if question_number < 1 or question_number > total_questions:
        # Instead of redirecting infinitely, show first question or an error
        return redirect('survey_question', question_number=1)

    questions = [{'number': i+1, 'health_card': card} for i, card in enumerate(health_cards)]
    current_question = questions[question_number - 1]

    # For last question, render completion page
    if question_number == total_questions:
        template_name = 'surveyQ14.html'
        context = {
            'current_question': current_question,
            'question_number': question_number,
            'total_questions': total_questions
        }
        return render(request, template_name, context)

    # Handle form submission
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
        return redirect('survey_question', question_number=question_number + 1)

    # Render question template
    template_name = f'surveyQ{question_number}.html'
    context = {
        'current_question': current_question,
        'question_number': question_number,
        'total_questions': total_questions
    }
    return render(request, template_name, context)