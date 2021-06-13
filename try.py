# from furigana.furigana import print_html
from sudachipy import tokenizer
from sudachipy import dictionary
tokenizer_obj = dictionary.Dictionary().create()
# tokenizer_obj = dictionary.Dictionary().create()
# import re
# # import WordsListTestSmall
# v = '格好[かっこう;h]'
# listw = ['格好[かっこう;h]', '穿[は,はく;h]く', '宜[よろ,よろしい;k3,h]しい', '慎[つつし;h,o]み', 'ズボン[;n2,a]', '考案[こうあん;h]', '負[ま,まける;h]ける', '見た目[みため;a]', '体裁[ていさい;h]', '曲解[きょっかい;h]', '古[ふる,いにしえ;h]', '貰[もら,もらう;h]う', '生産[せいさん;h]', '科[とが;a]', 'ふーん', '焜炉[こんろ;a]', '打[ぶ,うつ;h]つかる', '火傷[やけど;h]', '困[こま,こまる;k2]る', 'し[,する;h] 足[た,たりる;h]りない', '何[なん;n4]となく', '察[さつ,さっす;k1] す', '万が一[まんがいち;a,ao]', '配慮[はいりょ;a]', '堪能[たんのう;h,n3]',
#          '勤労[きんろう;h]', '意欲[いよく;a]', '一々[いちいち;n2]', '言い方[いいかた;h]', '見え透[みえす,みえすく;h,k3]く', '凍[こご,こごえる;h,k3]える', '恨[うら,うらむ;k2]む', '色付[いろづ,いろづく;k3]く', '繋[つな,つなぐ;h]ぐ', '望み通[のぞみどお;n4]り', '雨上[あめあ;n3]がり', '虹[にじ;h]', '仰[あお,あおぐ;k2]ぐ', '刻[きざ,きざむ;h]む', '煌 く[,くい;k1]', '突き刺[つきさ,つきささる;k4]さる', '低気圧[ていきあつ;n3]', '頭痛[ずつう;h]', '静寂[せいじゃく;h]', '流星[りゅうせい;h]', '釣[つられ,つられる;h]られる', '偶然[ぐうぜん;h]', '必然[ひつぜん;h]', '握[にぎ,にぎる;h]る']
#
# # pattern = re.compile(r"(.+)(\[.+\])(.+)?")
# pattern = re.compile(r"[\(\[].*?[\)\]]")
# # pattern = re.compile(r"[^格好]")
# # matches = pattern.finditer(v)
#
# for word in listw:
#     # matches_subed = pattern.sub(r'\1\3', word)
#     matches_subed = pattern.sub("", word)
#     print(matches_subed)

# for match in matches:
#     print(match)
#
# word = "好"
# kanji = "格"
#
# if kanji in word:
#     print(f"{kanji} is in {word}")
# else:
#     print(f"{kanji} is not in {word}")
mode = tokenizer.Tokenizer.SplitMode.C
[m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode)]
# => ['国家公務員']

mode = tokenizer.Tokenizer.SplitMode.B
[m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode)]
# => ['国家', '公務員']

mode = tokenizer.Tokenizer.SplitMode.A
[m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode)]
# => ['国家', '公務', '員']

# print(tagger.parse("pythonが大好きです"))
m = tokenizer_obj.tokenize("食べ", mode)[0]

m.surface()  # => '食べ'
m.dictionary_form()  # => '食べる'
print(f"<ruby><rb>食べ</rb><rp>(</rp><rt>{m.reading_form()}</rt><rp>)</rp></ruby>")  # => 'タベ'
print(f"食べ(たべ)")  # => 'タベ'
m.part_of_speech()  # => ['動詞', '一般', '*', '*', '下一段-バ行', '連用形-一般']

# print("<ruby><rb>{0}</rb><rt>{1}</rt></ruby>".
# print_html('澱んだ街角で僕らは出会った')
# {食べ}(たべ)
