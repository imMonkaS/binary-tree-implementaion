from tests import *

from utils import randomly_generate_tree_and_subtree_files
"""
TODO:
Статистика
Function random_insertion for 2 mil Took 25180.882 ms or 25.180882 s
Function read_tree for 2 mil Took 34106.576 ms or 34.106576 s

заполнение слишком медленное, нужно подумать как быстрее инсёртить, и как быстрее считывать файлы
идея для файлов: можно избавиться от кортежей в виде ключа, тогда время для огромного кол-ва данных 100%
уменьшится
идея имеет право на существование тк из-за того что для каждого родителя прописаны дети,
их значения и так легко получить, в таком случае у родителей достаточно писать идшник
Замечание: для рута нужно как-то прописывать значение, потому что по схеме, приведенной
сверху значение для рута не будет нигде прописано (он сирота xD)

При этом сам алгоритма поиска работает не плохо:
2 миллиона данных за +- полсекунды

Если решить проблему с заполнением то лабу можно считать завершенной

Стоит просмотреть код ещё раз, и возможно провести некий рефакторинг

"""


def main():
    # randomly_generate_tree_and_subtree_files(
    #     10,
    #     3,
    #     SOURCES_PATH + 'report/10nodes/tree.txt',
    #     SOURCES_PATH + 'report/10nodes/subtree.txt',
    #     SOURCES_PATH + 'report/10nodes/tree.png',
    #     SOURCES_PATH + 'report/10nodes/subtree.png',
    # )

    ultimate_test(
        SOURCES_PATH + 'report/10nodes/tree.txt',
        SOURCES_PATH + 'report/10nodes/subtree.txt',
        SOURCES_PATH + 'report/10nodes/output.txt',
        SOURCES_PATH + 'report/10nodes/time.txt'
    )


if __name__ == '__main__':
    main()
