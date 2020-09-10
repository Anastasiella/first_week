import statistics

school = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '6a', 'scores': [2,3,5,2,1]},
    {'school_class': '3b', 'scores': [2,5,4,5,5]}
]

def total_mean_score(school):
    lists = []
    for i in school:
        lists.extend(i['scores'])
    print(f"Средняя оценка по школе: = {round(statistics.mean(lists), 2)} баллов.")

total_mean_score(school)

def mean_score(school):
    for i in school:
        print(f"Средняя оценка по {i['school_class']} классу: = {statistics.mean(i['scores'])} балла.")
        
mean_score(school)