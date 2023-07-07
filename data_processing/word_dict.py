import pickle

def get_vocab(corpus1, corpus2):
    word_vocab = set()

    # 遍历两个语料库
    for corpus in [corpus1, corpus2]:
        for element in corpus:
            for sublist in element[1]:
                word_vocab.update(sublist)  # 将子列表中的单词添加到词汇表中
            for sublist in element[2]:
                word_vocab.update(sublist)  # 将子列表中的单词添加到词汇表中
            word_vocab.update(element[3])  # 将单个单词添加到词汇表中

    print(len(word_vocab))  # 打印词汇表的大小
    return word_vocab


def load_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f, encoding='iso-8859-1')  # 从 pickle 文件中加载对象


# 根据给定的语料库构建词汇表
def vocab_processing(filepath1, filepath2, save_path):
    with open(filepath1, 'r') as f:
        total_data1 = eval(f.read())  # 从文件中读取内容并将其解析为 Python 对象

    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())  # 从文件中读取内容并将其解析为 Python 对象

    x1 = get_vocab(total_data1, total_data2)  # 获取词汇表
    with open(save_path, "w") as f:
        f.write(str(x1))  # 将词汇表写入文件


# 最终词汇表处理
def final_vocab_processing(filepath1, filepath2, save_path):
    word_set = set()

    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))  # 从文件中读取内容并将其解析为 Python 对象

    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())  # 从文件中读取内容并将其解析为 Python 对象

    total_data1 = list(total_data1)
    unique_words = get_vocab(total_data1, total_data2)  # 获取词汇表

    for word in unique_words:
        if word in total_data1:
            continue
        else:
            word_set.add(word)

    print(len(total_data1))
    print(len(word_set))

    with open(save_path, "w") as f:
        f.write(str(word_set))  # 将单词集合写入文件


if __name__ == "__main__":
    # 获取 staqc 的词语集合
    python_hnn = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/python_hnn_data_teacher.txt'
    python_staqc = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/staqc/python_staqc_data.txt'
    python_word_dict = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/sql_hnn_data_teacher.txt'
    sql_staqc = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/staqc/sql_staqc_data.txt'
    sql_word_dict = '/home/gpu/RenQ/stqac/data_processing/hnn_process/data/word_dict/sql_word_vocab_dict.txt'

    # 获取最后大语料的词语集合的词语集合
    new_sql_staqc = '../hnn_process/ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    new_sql_large = '../hnn_process/ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'
    large_word_dict_sql = '../hnn_process/ulabel_data/sql_word_dict.txt'
    final_vocab_processing(sql_word_dict, new_sql_large, large_word_dict_sql)

    new_python_staqc = '../hnn_process/ulabel_data/staqc/python_staqc_unlabled_data.txt'
    new_python_large = '../hnn_process/ulabel_data/large_corpus/multiple/python_large_multiple_unlable.txt'
    large_word_dict_python = '../hnn_process/ulabel_data/python_word_dict.txt'
