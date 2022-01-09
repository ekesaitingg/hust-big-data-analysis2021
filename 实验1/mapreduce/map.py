#!/usr/bin/env python3
import sys
import threading
import time


def read_input(file):
    for line in file:
        line = line.strip()
        yield line.split(', ')


def mapper(readfile, writefile):
    file = open(readfile)
    write = open(writefile, 'w')
    lines = read_input(file)
    with write as f:
        for words in lines:
            for word in words:
                f.write("{},{}\n".format(word, 1))


if __name__ == '__main__':
    t1 = threading.Thread(target=mapper('source01', 'map1'), args=("t1",))
    t2 = threading.Thread(target=mapper('source02', 'map2'), args=("t2",))
    t3 = threading.Thread(target=mapper('source03', 'map3'), args=("t3",))
    t4 = threading.Thread(target=mapper('source04', 'map4'), args=("t4",))
    t5 = threading.Thread(target=mapper('source05', 'map5'), args=("t5",))
    t6 = threading.Thread(target=mapper('source06', 'map6'), args=("t6",))
    t7 = threading.Thread(target=mapper('source07', 'map7'), args=("t7",))
    t8 = threading.Thread(target=mapper('source08', 'map8'), args=("t8",))
    t9 = threading.Thread(target=mapper('source09', 'map9'), args=("t9",))
    start = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t1.join()
    print("t1: %s s" % (time.perf_counter() - start))
    t2.join()
    print("t2: %s s" % (time.perf_counter() - start))
    t3.join()
    print("t3: %s s" % (time.perf_counter() - start))
    t4.join()
    print("t4: %s s" % (time.perf_counter() - start))
    t5.join()
    print("t5: %s s" % (time.perf_counter() - start))
    t6.join()
    print("t6: %s s" % (time.perf_counter() - start))
    t7.join()
    print("t7: %s s" % (time.perf_counter() - start))
    t8.join()
    print("t8: %s s" % (time.perf_counter() - start))
    t9.join()
    print("t9: %s s" % (time.perf_counter() - start))
