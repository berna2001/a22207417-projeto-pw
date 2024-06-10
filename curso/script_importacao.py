import json
from curso.models import Curso, Disciplina, AreaCientifica

def importar_curso(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    course_flat_plan = data['courseFlatPlan']
    for unit in course_flat_plan:
        area_cientifica, created = AreaCientifica.objects.get_or_create(
            nome=unit['curricularBranchName']
        )

        Disciplina.objects.update_or_create(
            nome=unit['curricularUnitName'],
            defaults={
                'ano': unit['curricularYear'],
                'semestre': unit['semester'],
                'ects': unit['ects'],
                'curricular_unit_readable_code': unit['curricularIUnitReadableCode'],
                'area_cientifica': area_cientifica
            }
        )

    print('Dados importados com sucesso!')

