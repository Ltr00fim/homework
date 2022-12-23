import json


# конвертирование текста json из файла
def load_candidates(file):
    with open(file, encoding='UTF-8') as f:
        text = json.load(f)
    return text


# список всех имен
def get_all_names():
    global candidates
    names = []
    for candidate in candidates:
        names.append(candidate['name'])
    return names


# возвращается кандидат по номеру
def get_by_pk(pk):
    global candidates
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    else:
        return f"Не существует кандидата с номером {pk}"


# возвращает список кандидатов по навыку
def get_by_skill(skill_name):
    global candidates
    candidates_skill = []
    for candidate in candidates:
        candidate_skill = [i.lower() for i in candidate['skills'].split(', ')]
        if skill_name in candidate_skill:
            candidates_skill.append(candidate)
    return candidates_skill


candidates = load_candidates('candidates.json')
