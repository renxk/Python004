# _*_ encoding:utf-8 _*_
# Author: renxk
# date: 2020/10/19 3:46 下午


# 哲学家进餐：使用条件变量
from time import sleep
import threading
import queue

import random
class DiningPhilosophers(threading.Thread):
    def __init__(self, id, forks, eat_num, out_queue):
        threading.Thread.__init__(self)
        self.id = id
        self.forks = forks
        self.eat_num = eat_num
        self.out_queue = out_queue

        self.current_eat_num = 0

    def run(self) -> None:
        self.thread_run()

        if self.current_eat_num < self.eat_num:
            sleep(1)
            self.run()


    def thread_run(self):
        try:
            left_fork = self.forks[self.id]
            right_fork = self.forks[(self.id + 1) % len(self.forks)]
            if left_fork.acquire(False):
                self.pickLeftFork()
                if right_fork.acquire(False):
                    self.pickRightFork()
                    self.eat()
                    self.putLeftFork()
                    self.putRightFork()

                    left_fork.release()
                    right_fork.release()
                else:
                    self.putLeftFork()
                    left_fork.release()



        except Exception as error:
            print(error)





    def pickLeftFork(self):
        print(f'哲学家{self.id}: 拿起左边叉子。')
        self.out_queue.put(f'[{self.id}, 1, 1]')

    def pickRightFork(self):
        print(f'哲学家{self.id}: 拿起右边叉子。')
        self.out_queue.put(f'[{self.id}, 2, 1]')

    def eat(self):
        print(f'哲学家{self.id}: 进餐中……')
        self.out_queue.put(f'[{self.id}, 0, 3]')
        sleep(random.uniform(2, 6))
        self.current_eat_num += 1

    def putLeftFork(self):
        print(f'哲学家{self.id}: 放下左边叉子。')
        self.out_queue.put(f'[{self.id}, 1, 2]')

    def putRightFork(self):
        print(f'哲学家{self.id}: 放下右边叉子。')
        self.out_queue.put(f'[{self.id}, 2, 2]')
def get_eat_number():
    while True:
        result = input('请输入哲学家进餐次数:')
        try:
            num = int(result)
            if num <= 0:
                print('请输入正整数')
            else:
                return num
        except Exception as error:
            print('输入数据类型错误，请输入正整数')




def main():
    philosopher = 5

    eat_num = get_eat_number()

    out_queue = queue.Queue(3000)

    forks = []
    threads = []
    for i in range(philosopher):
        forks.append(threading.RLock())

    for i in range(philosopher):
        threads.append((DiningPhilosophers(id=i, forks=forks, eat_num=eat_num, out_queue=out_queue)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('=' * 20)
    print('进餐结束:')
    result = []
    while not out_queue.empty():
        result.append(out_queue.get())
    print(result)

if __name__ == '__main__':
    main()
