from threading import Thread, Lock, RLock
import time

outside_var = [0]

def func1(var, lock):
    while True:
        if lock.acquire():
            print("func1's lock is acquired.")
            if var[0] >= 100:
                lock.release()
                print("func1 end.")
                break
            
            for i in range(5):
                var[0] +=1
                print("func1", var[0])
                time.sleep(0.2)

            print("func1's lock is released.")
            lock.release()
        time.sleep(0.2)
                
def func2(var, lock):
    while True:
        if lock.acquire():
            print("func2's lock is acquired.")
            if var[0] >= 100:
                lock.release()
                print("func2 end.")
                break

            for i in range(10):
                var[0] +=1
                print("func2", var[0])
                time.sleep(0.2)

            print("func2's lock is released.")
            lock.release()
        time.sleep(0.2)
            
if __name__ == "__main__":
    func_lock = Lock()

    t1 = Thread(target=func1, args=(outside_var, func_lock))
    t2 = Thread(target=func2, args=(outside_var, func_lock))

    t1.start()
    t2.start()