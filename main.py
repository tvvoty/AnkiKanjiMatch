import re
import os
from sudachipy import tokenizer
from sudachipy import dictionary
tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.B
exept_simbols = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿ｡｢ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ$゙$゚ ゙ ゚ゝゞゟAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-123456789"


def migaku_question(migaku_input):
    if migaku_input == "y":
        return migaku_input
    elif migaku_input == "n":
        return migaku_input
    return None


def furigana_question(furigana_input):
    if furigana_input == "y":
        return furigana_input
    elif furigana_input == "n":
        return furigana_input
    return None


while (foo := furigana_question(input('Do you want to have furigana for kanji? Print "y" for yes or "n" for no into the console: '))) == None:
    print("Invalid input, lets try once again: ")
else:
    if foo == "y":
        furigana = True
    else:
        furigana = False


while True:
    path_to_deck = input("Plese input path to the deck file: ")
    try:
        # path_to_deck = "Collection/Old/AnkiConnect.txt"
        with open(path_to_deck, mode='r', encoding='utf-8') as f:
            deck = f.read()
            print("This is the deck from the file:\n" + deck)
        break
    except Exception as e:
        print(
            f"Something wrong with your file or file path: \n{e}\n Lets try inputing path one more time")


while (foo := migaku_question(input('If you have [] brakets from migaku you should probably delete them - delete migaku brakets? Print "y" for yes or "n" for no into the console:'))) == None:
    print("Invalid input, lets try once again: ")
else:
    if foo == "y":
        delete_migaku = True
    else:
        delete_migaku = False


deck_splitted = deck.split('\n')
print("This is the deck splitted by new lines:\n")
print(deck_splitted)
words_list = []


pattern = re.compile(r"[\(\[].*?[\)\]]")  # A Pattern for deleting brakets from migaku

for deck_entry in deck_splitted:
    deck_entry_splitted = deck_entry.split('\t')
    print("This is a deck entry splitted by tabs:\n")
    print(deck_entry_splitted)
    word_from_the_splitted_entry = deck_entry_splitted[0]
    print("This is a deck entry splitted by tabs's first element 'word':\n" + word_from_the_splitted_entry)
    word_no_migaku = pattern.sub("", word_from_the_splitted_entry)
    print(f"The word without migaku is:\n {word_no_migaku}")
    print(f"Appending the word {word_no_migaku} to the words_list")
    words_list.append(word_no_migaku)

print("This is a completed words list:\n")
print(words_list)

kanji_dict = {}
print("Kanji dict is created and equals to:")
print(kanji_dict)

for word in words_list:
    print(f"The word being processed is: {word}")
    for kanji in word:
        print(f"The kanji being processed is: {kanji}")
        if kanji not in exept_simbols:
            kanji_dict[kanji] = []
            print(f"Kanji dict was updated with {kanji} and equals to:")
            # print(kanji_dict)
        print("Kanji dict was not updated and equals to:")
        # print(kanji_dict)
print(f"The amount of kanji is {len(kanji_dict)}")

# print(f"Here is your kanji dictionary:\n{kanji_dict}")

for kanji_key, words_values in kanji_dict.items():
    print(f"Kanji is {kanji_key} and its values are {words_values}")
    for word in words_list:
        # print(f"The word is {word}")
        if kanji_key in word:
            m = tokenizer_obj.tokenize(word, mode)[0]
            kanji_dict[kanji_key].append(f"{word}({m.reading_form()})")

sorted_kanji_dict = sorted(kanji_dict.items(), key=lambda pair: len(pair[1]), reverse=True)

# for kk, wv in kanji_dict.items():
#     print(f"{kk}: {wv}.\n")

for x in sorted_kanji_dict:
    print(f"{x}\n")

with open(path_to_deck, mode='r', encoding='utf-8') as f:
    deck = f.read()
    print("This is the deck from the file:\n" + deck)
break
except Exception as e:
print(
    f"Something wrong with your file or file path: \n{e}\n Lets try inputing path one more time")
