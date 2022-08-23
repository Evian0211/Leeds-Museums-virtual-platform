from .models import Course_quiz_answer, Item, Evaluation, Evaluation_quiz_answer, Curriculum
from .text import CURRICULUM, EVALUATION_QUESTIONS, EVALUATION_TYPES, COURSE_ONE_FULL_MARK

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

    score = [0,0,0,0,0,0]
    if sorted_answers[0] == 0:
        score[0] += 1
        score[5] += 1
    elif sorted_answers[0] == 1:
        score[2] += 1
        score[5] += 1
    elif sorted_answers[0] == 2:
        score[4] += 1
        score[5] += 1
    elif sorted_answers[0] == 3:
        score[3] += 1
        score[5] += 1

    if sorted_answers[1] == 0:
        score[3] += 1
    elif sorted_answers[1] == 1:
        score[2] += 1
    elif sorted_answers[1] == 2:
        score[4] += 1
    elif sorted_answers[1] == 3:
        score[1] += 1

    if sorted_answers[2] == 0:
        score[0] += 1
    elif sorted_answers[2] == 1:
        score[1] += 1
    elif sorted_answers[2] == 2:
        score[2] += 1
    elif sorted_answers[2] == 3:
        score[4] += 1

    if sorted_answers[3] == 0:
        score[4] += 1
    elif sorted_answers[3] == 1:
        score[1] += 1
        score[4] += 1
        score[3] += 1
    elif sorted_answers[3] == 2:
        score[2] += 1
    elif sorted_answers[3] == 3:
        score[0] += 1

    if sorted_answers[4] == 0:
        score[0] += 1
        score[5] += 1
        score[4] += 1
        score[3] += 1
    elif sorted_answers[4] == 1:
        score[0] += 1
        score[5] += 1
    elif sorted_answers[4] == 2:
        score[2] += 1
        score[5] += 1
    elif sorted_answers[4] == 3:
        score[1] += 1
        score[4] += 1
        score[5] += 1

    print(score)
    max_interst = 0
    recommandation = ""
    for i in range(0,len(score)):
        if score[i] > max_interst:
            max_interst = score[i]
            recommandation = EVALUATION_TYPES[i]
    set_evaluation_result(user, recommandation)

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
    status_list = []
    for course in status:
        status_list.append((course.course, course.score))
    return status_list

def update_course_quiz_answer(user, course_number, q_number, answer):
    _, course, _, _ = CURRICULUM[course_number]
    try:
        answer = Course_quiz_answer.objects.get(user=user, course=course, question=q_number)
        answer.delete()
    except:
        pass

    answer = Course_quiz_answer(user=user, course=course, question=q_number, answer=answer)
    answer.save()

def clear_course_quiz_answers(user, course_number):
    _, course, _, _ = CURRICULUM[course_number]
    answers = Course_quiz_answer.objects.filter(user=user, course=course)
    for answer in answers:
        answer.delete()

def mark_course(user, course_number):
    _, course, _, _ = CURRICULUM[course_number]
    # TODO: Fill this logic
    score = 100

    try:
        old_result = Evaluation.objects.get(user=user, course=course)
        old_result.delete()
    except:
        pass
    result = Curriculum(user=user, course=course, score=score)
    result.save()

    return score

def get_item(user, course_number, score):
    # TODO: Fill this logic
    got_item = False
    if course_number == 0 and score == 100:
        try:
            item = Item.objects.get(user=user, name=COURSE_ONE_FULL_MARK)
        except:
            item = Item(user=user, name=COURSE_ONE_FULL_MARK)
            item.save()
            got_item = True

    return got_item