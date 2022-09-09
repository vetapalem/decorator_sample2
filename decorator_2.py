from functools import wraps as w 
import time as ds
def ti(ji):
    def calu():
        a=ds.time()
        print(f'the time is began is {a}')
        print(f'the time is finishing {ds.time() -a }')
        
    return calu()

# def indes(i):
def jkoin(ui):
    # @w(ui)
    def starter():
        
        print(f':the code is runng is ok...')
        print(f'the original name of the function is {ui.__name__}')
        c= ui()
        return c
    return starter()



def estimating_all():
    print(f"this is the new programmning lang....")

# jkoin(ti(estimating_all))
# print(estimating_all())
ti(jkoin(estimating_all))