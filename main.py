import re
from sudachipy import tokenizer
from sudachipy import dictionary
tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.B


kana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿ｡｢ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ$゙$゚ ゙ ゚ゝゞゟ"


with open("Collection/AnkiConnectCards.txt", mode='r', encoding='utf-8') as f:
    deck = f.read()
    print("This is the deck from the file:\n" + deck)

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
        if kanji not in kana:
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

for kk, wv in kanji_dict.items():
    print(f"{kk}: {wv}.\n")
# print(kanji_dict)
