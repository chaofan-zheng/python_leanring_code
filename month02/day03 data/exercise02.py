"""
    单词本，每行一个单词
        单词和解释之间有空格
        后面的单词比前面的大
        编写一个函数，传入一个单词，返回单词的对应解释。
"""


#
# def vocabulary(target_word):
#     filename = "dict.txt"
#     # vocabulary_dict = {}
#     file_vocabulary = open(filename)
#     for line in file_vocabulary:
#         line_parts = line.split("   ")
#         # vocabulary_dict[line_parts[0]] = line_parts[-1]
#         if line_parts[0] == target_word:
#             return line_parts[-1]
#     return "没有这个单词"
#
#
# result = vocabulary("abet")
# print(result)


# def vocabulary(target_word: str) -> str:
#     filename = "dict.txt"
#     file_vocabulary = open(filename)
#     for line in file_vocabulary:
#         line_parts = line.split(" ")
#         if target_word in line_parts:
#             line_stripped = line.strip(" ").strip(target_word)
#             return "".join(line_stripped)
#     return "没有这个单词"
#
#
# print(vocabulary("acknowledgement"))
#
def vocabulary(target_word: str) -> str:
    filename = "dict.txt"
    file_vocabulary = open(filename)
    for line in file_vocabulary:
        line_parts = line.split(" ", 1)
        if line_parts[0] > target_word:
            break
        elif target_word == line_parts[0]:
            file_vocabulary.close()
            return line_parts[1].strip()
    file_vocabulary.close()
    return "没有这个单词"


print(vocabulary("acknowledgement"))
