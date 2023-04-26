from pymystem3 import Mystem


def street_analysis(street="улица 51-й Гвардейской дивизии"):
    white_list = {"улица", "переулок", "бульвар", "проспект"}
    removal_list = ["улица", "улица ", "переулок ", "переулок", "бульвар ", "бульвар", "проспект ", "проспект",
                    "имени ", "имени", "им. ", "им.",
                    "-й", "-я", "-ая", "-а", "-",
                    "1 ", "1", "2 ", "2", "3 ", "3", "4", "4 ", "5", "5 ", "6", "6 ", "7", "7 ", "8", "8 ", "9 ", "9",
                    "0 ", "0", ]
    street = street.lower()
    str_set = set(street.split())
    if str_set & white_list:
        # print(str_set & white_list)
        for word in removal_list:
            street = street.replace(word, "")
        #print(street)
        return street
    else:
        return ""


def main_lem(list_):
    data_upd = []
    for i in list_:
        data_upd.append(street_analysis(i))

    my_stem = Mystem()
    data = my_stem.lemmatize('\n'.join(data_upd))
    print(data)
    return data


if __name__ == "__main__":
    with open('Test.txt', 'r', encoding='utf-8') as file:
        text = file.read().split("\n")
    text_upd = main_lem(text)
    print(''.join(text_upd))
