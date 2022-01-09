import sys
import threading
import time


def run(readfile):
    file = open(readfile)
    write1 = open('shuffle1', 'a')
    write2 = open('shuffle2', 'a')
    write3 = open('shuffle3', 'a')
    for line in file:
        line = line.strip()
        word, count = line.split(',', 1)
        if word[0] == 'a' or word[0] == 'A' or word[0] == 'b' or word[0] == 'B' or word[0] == 'c' or word[0] == 'C':
            write1.write("{},{}\n".format(word, count))
        elif word[0] == 'd' or word[0] == 'D' or word[0] == 'e' or word[0] == 'E' or word[0] == 'f' or word[0] == 'F':
            write1.write("{},{}\n".format(word, count))
        elif word[0] == 'g' or word[0] == 'G':
            write1.write("{},{}\n".format(word, count))
        elif word[0] == 'j' or word[0] == 'J' or word[0] == 'k' or word[0] == 'K' or word[0] == 'l' or word[0] == 'L':
            write2.write("{},{}\n".format(word, count))
        elif word[0] == 'm' or word[0] == 'M' or word[0] == 'n' or word[0] == 'N' or word[0] == 'o' or word[0] == 'O':
            write2.write("{},{}\n".format(word, count))
        elif word[0] == 'p' or word[0] == 'P' or word[0] == 'q' or word[0] == 'Q' or word[0] == 'r' or word[0] == 'R':
            write2.write("{},{}\n".format(word, count))
        else:
            write3.write("{},{}\n".format(word, count))


if __name__ == '__main__':
    t1 = threading.Thread(target=run('combine1'), args=("t1",))
    t2 = threading.Thread(target=run('combine2'), args=("t2",))
    t3 = threading.Thread(target=run('combine3'), args=("t3",))
    t4 = threading.Thread(target=run('combine4'), args=("t4",))
    t5 = threading.Thread(target=run('combine5'), args=("t5",))
    t6 = threading.Thread(target=run('combine6'), args=("t6",))
    t7 = threading.Thread(target=run('combine7'), args=("t7",))
    t8 = threading.Thread(target=run('combine8'), args=("t8",))
    t9 = threading.Thread(target=run('combine9'), args=("t9",))
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