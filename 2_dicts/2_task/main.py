import re


def top_10_most_common_words(text: str) -> dict[str, int]:
    dict, dict_most_common = {}, {}
    count = 0
    pattern = r'[.,;:!? -''"()\n    ]'
    correct_list = [i.lower() for i in re.split(pattern, text) if len(i) >= 3]
    for key in correct_list:
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1
    tuple_most_common = sorted(dict.items(), key=lambda x: (x[1]), reverse=True)
    tuple_most_common.sort(key=lambda x: (-x[1],x[0]))
    for tuple in tuple_most_common:
        dict_most_common[tuple[0]] = int(tuple[1])
        count += 1
        if count == 10:
            break
    return dict_most_common