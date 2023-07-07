import pickle
from collections import Counter

def load_pickle(filename):
    return pickle.load(open(filename, 'rb'), encoding='iso-8859-1')


def single_list(arr, target):
    return arr.count(target)

#large：把语料中的单候选和多候选分隔开
def data_large_processing(filepath, save_single_path, save_multiple_path):
    total_data = load_pickle(filepath)
    qids = [data[0][0] for data in total_data]
    result = Counter(qids)
    total_data_single = [data for data in total_data if result[data[0][0]] == 1]
    total_data_multiple = [data for data in total_data if result[data[0][0]] > 1]

    with open(save_single_path, 'wb') as f:
        pickle.dump(total_data_single, f)
    with open(save_multiple_path, 'wb') as f:
        pickle.dump(total_data_multiple, f)


#把单候选只保留其qid
def single_unlable2lable(path1,path2):
    total_data = load_pickle(path1)
    labels=[]

    for i in range(0,len(total_data)):
        labels.append([total_data[i][0],1])

    total_data_sort = sorted(labels, key=lambda x: (x[0], x[1]))
    f = open(path2, "w")
    f.write(str(total_data_sort))
    f.close()


if __name__ == "__main__":
    #将staqc_python中的单候选和多候选分开
    staqc_python_path = '../hnn_process/ulabel_data/python_staqc_qid2index_blocks_unlabeled.txt'
    staqc_python_sigle_save ='../hnn_process/ulabel_data/staqc/single/python_staqc_single.txt'
    staqc_python_multiple_save = '../hnn_process/ulabel_data/staqc/multiple/python_staqc_multiple.txt'

    #将staqc_sql中的单候选和多候选分开
    staqc_sql_path = '../hnn_process/ulabel_data/sql_staqc_qid2index_blocks_unlabeled.txt'
    staqc_sql_sigle_save = '../hnn_process/ulabel_data/staqc/single/sql_staqc_single.txt'
    staqc_sql_multiple_save = '../hnn_process/ulabel_data/staqc/multiple/sql_staqc_multiple.txt'

    #将large_python中的单候选和多候选分开
    large_python_path = '../hnn_process/ulabel_data/python_codedb_qid2index_blocks_unlabeled.pickle'
    large_python_single_save = '../hnn_process/ulabel_data/large_corpus/single/python_large_single.pickle'
    large_python_multiple_save ='../hnn_process/ulabel_data/large_corpus/multiple/python_large_multiple.pickle'
    data_large_processing(large_python_path, large_python_single_save, large_python_multiple_save)

    # 将large_sql中的单候选和多候选分开
    large_sql_path = '../hnn_process/ulabel_data/sql_codedb_qid2index_blocks_unlabeled.pickle'
    large_sql_single_save = '../hnn_process/ulabel_data/large_corpus/single/sql_large_single.pickle'
    large_sql_multiple_save = '../hnn_process/ulabel_data/large_corpus/multiple/sql_large_multiple.pickle'

    large_sql_single_label_save = '../hnn_process/ulabel_data/large_corpus/single/sql_large_single_label.txt'
    large_python_single_label_save = '../hnn_process/ulabel_data/large_corpus/single/python_large_single_label.txt'
