with open("learning_python") as file_object:  # open 是把文件打开，和一个对象关联起来
    learning_python_text = file_object.read()  # 把文件解码，然后储存起来。为了在外部可以使用
    print(file_object)  # <_io.TextIOWrapper name='learning_python' mode='r' encoding='UTF-8'>
    print(learning_python_text)
print(learning_python_text)  # 在with外部也能够调用

"""
逐行读，with内调用
"""
with open("learning_python") as file_object:
    for line in file_object:
        print(line)

"""
逐行读取，with外调用
"""
with open("learning_python") as file_object:
    list_article = []
    for line in file_object:
        list_article.append(line)
for line in list_article:
    print(line)

"""
读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。

"""
for line in list_article:
    print(line.replace('Python', 'C++'))


