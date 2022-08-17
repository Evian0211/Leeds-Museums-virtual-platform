from .models import Item, Evaluation, Evaluation_quiz_answer, Curriculum
from .text import EVALUATION_QUESTIONS

def get_evaulation_result(user):
    try:
        evaluation = Evaluation.objects.get(user=user)
        evaluation = evaluation.result
    except:
        evaluation = None
    return evaluation

def update_evaluation_quiz_answer(user, q_number, answer):
    try:
        answer = Evaluation_quiz_answer.objects.get(user=user, q_number=q_number)
        answer.delete()
    except:
        pass

    answer = Evaluation_quiz_answer(user=user, q_number=q_number, answer=answer)
    answer.save()

def clear_evaluation_answers(user):
    answers = Evaluation_quiz_answer.objects.filter(user=user)
    for answer in answers:
        answer.delete()

def is_quiz_complete(user):
    if len(Evaluation_quiz_answer.objects.filter(user=user)) == len(EVALUATION_QUESTIONS):
        return True
    else:
        return False

def evaluate(user):
    answers = Evaluation_quiz_answer.objects.filter(user=user).order_by("q_number")
    sorted_answers = []
    for answer in answers:
        sorted_answers.append(answer.answer)
    # TODO: Fill this logic
    if sorted_answers[0] == 0 and sorted_answers[1] == 0:
        set_evaluation_result(user, "Type A")
    else:
        set_evaluation_result(user, "Type B")

def set_evaluation_result(user, result):
    try:
        old_evaluation = Evaluation.objects.get(user=user)
        old_evaluation.delete()
    except:
        pass
    evaluation = Evaluation(user=user, result=result)
    evaluation.save()

def get_all_items(user):
    items = Item.objects.filter(user=user)
    item_list = []
    for item in items:
        item_list.append(item.name)
    return item_list

def get_curriculum_status(user):
    status = Curriculum.objects.filter(user=user)
    status_dict = {}
    for course in status:
        status[course.name] = course.score
    return status_dict
