"""
并行分词
"""

import pickle
# 解析结构
from python_structured import *
from sqlang_structured import *
# 多进程
from multiprocessing import Pool as ThreadPool

#python解析
def multipro_python_query(data_list):
    result=[python_query_parse(line) for line in data_list]
    return result

def multipro_python_code(data_list):
    result = [python_code_parse(line) for line in data_list]
    return result

def multipro_python_context(data_list):
    result = []
    for line in data_list:
        if (line == '-10000'):
            result.append(['-10000'])
        else:
            result.append(python_context_parse(line))
    return result


#sql解析
def multipro_sqlang_query(data_list):
    result=[sqlang_query_parse(line) for line in data_list]
    return result

def multipro_sqlang_code(data_list):
    result = [sqlang_code_parse(line) for line in data_list]
    return result

def multipro_sqlang_context(data_list):
    result = []
    for line in data_list:
        if (line == '-10000'):
            result.append(['-10000'])
        else:
            result.append(sqlang_context_parse(line))
    return result

def parse_data(python_list, split_num):
    def process_data(data, split_func):
        split_list = [data[i:i + split_num] for i in range(0, len(data), split_num)]
        pool = ThreadPool(10)
        result_list = pool.map(split_func, split_list)
        pool.close()
        pool.join()
        cut_data = []
        for p in result_list:
            cut_data += p
        return cut_data

    acont1_data = [i[1][0][0] for i in python_list]
    acont2_data = [i[1][1][0] for i in python_list]
    query_data = [i[3][0] for i in python_list]
    code_data = [i[2][0][0] for i in python_list]

    acont1_cut = process_data(acont1_data, multipro_python_context)
    acont2_cut = process_data(acont2_data, multipro_python_context)
    query_cut = process_data(query_data, multipro_python_query)
    code_cut = process_data(code_data, multipro_python_code)
    qids = [i[0] for i in python_list]

    return acont1_cut, acont2_cut, query_cut, code_cut, qids

def main(lang_type,split_num,source_path,save_path):
    total_data = []
    with open(source_path, "rb") as f:
        #  存储为字典 有序
        corpus_lis  = pickle.load(f) #pickle

        # [(id, index),[[si]，[si+1]] 文本块，[[c]] 代码，[q] 查询, [qcont] 查询上下文, 块长度，标签]

        if lang_type=='python':

            parse_acont1, parse_acont2,parse_query, parse_code,qids  = parse_data(corpus_lis,split_num)
            for i in range(0,len(qids)):
                total_data.append([qids[i],[parse_acont1[i],parse_acont2[i]],[parse_code[i]],parse_query[i]])

        if lang_type == 'sql':

            parse_acont1,parse_acont2,parse_query, parse_code,qids = parse_data(corpus_lis, split_num)
            for i in range(0,len(qids)):
                total_data.append([qids[i],[parse_acont1[i],parse_acont2[i]],[parse_code[i]],parse_query[i]])


    f = open(save_path, "w")
    f.write(str(total_data))
    f.close()

python_type= 'python'
sqlang_type ='sql'

words_top = 100

split_num = 1000
def test(path1,path2):
    with open(path1, "rb") as f:
        #  存储为字典 有序
        corpus_lis1  = pickle.load(f) #pickle
    with open(path2, "rb") as f:
        corpus_lis2 = eval(f.read()) #txt

    print(corpus_lis1[10])
    print(corpus_lis2[10])
if __name__ == '__main__':
    staqc_python_path = '../hnn_process/ulabel_data/python_staqc_qid2index_blocks_unlabeled.txt'
    staqc_python_save ='../hnn_process/ulabel_data/staqc/python_staqc_unlabled_data.txt'

    staqc_sql_path = '../hnn_process/ulabel_data/sql_staqc_qid2index_blocks_unlabeled.txt'
    staqc_sql_save = '../hnn_process/ulabel_data/staqc/sql_staqc_unlabled_data.txt'

    large_python_path='../hnn_process/ulabel_data/large_corpus/multiple/python_large_multiple.pickle'
    large_python_save='../hnn_process/ulabel_data/large_corpus/multiple/python_large_multiple_unlable.txt'

    large_sql_path='../hnn_process/ulabel_data/large_corpus/multiple/sql_large_multiple.pickle'
    large_sql_save='../hnn_process/ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'

    main(python_type, split_num, large_python_path, large_python_save)