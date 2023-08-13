COURSES = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
MENTORS = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
DURATIONS = [14, 20, 12, 20]


def get_courses_list(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    return courses_list


def sort_duration_courses(courses, mentors, durations):
    courses_list = get_courses_list(courses, mentors, durations)
            
    durations_dict = {}

    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [])
        values = durations_dict.get(key)
        values.append(id)
        durations_dict[key] = values

    durations_dict = dict(sorted(durations_dict.items()))

    result = list()

    for key, values in durations_dict.items():
        for index in values:
            result.append(f'{courses_list[index]["title"]} - {key} месяцев')

    return '\n'.join(result)


def get_longest_and_shortest_course(courses, mentors, durations):
    courses_list = get_courses_list(courses, mentors, durations)

    min_dur = min(durations)
    max_dur = max(durations)

    maxes = []
    minis = []
    for i, value in enumerate(durations):
        if value == max_dur:
            maxes.append(i)
        elif value == min_dur:
            minis.append(i)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]["title"])
    for id in maxes:
        courses_max.append(courses_list[id]["title"])

    result = f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_dur} месяца(ев)\nСамый длинный курс(ы): {", ".join(courses_max)} - {max_dur} месяца(ев)'
    return result


def get_top3_popular_names(mentors):
    all_mentors = []
    for m in mentors:
        all_mentors += m
    all_names = []
    for mentor in all_mentors:
        all_names.append(mentor.split(" ")[0])

    unique_names = set(all_names)

    popular = []
    for name in unique_names:
        popular.append([name, all_names.count(name)])

    popular.sort(key=lambda x:x[1], reverse=True)

    top_3 = popular[0:3]
    res = ", ".join(f'{name}: {count} раз(а)' for name, count in top_3)
    return res


if __name__ == '__main__':
    print(get_longest_and_shortest_course(COURSES, MENTORS, DURATIONS))
    print('===============================')
    print(sort_duration_courses(COURSES, MENTORS, DURATIONS))
    print('===============================')
    print(get_top3_popular_names(MENTORS))