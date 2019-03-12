import sys


def tracefoo(function_to_trace):
    def tracefunc(frame, event, arg):
        if event == "return" and frame.f_code.co_name == function_to_trace.__name__:
            print("function:", frame.f_code.co_name, ", local vars:", list(frame.f_locals.keys()))
        return tracefunc
    sys.settrace(tracefunc)


def bim():
    p = "Privet"
    print(p)

def bom ():
    print ('hahaha')


tracefoo(bim)
bom()
bom()
bim()
bom()
bim()