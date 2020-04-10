import logging


# 1. try...exception...finally
def test():
    print('方法开始')
    try:
        print("start try...")
        a = 1 / 0
        print('try end..., a is', a)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
        # 记录错误
        logging.exception(e)
    finally:
        print("finally...")
    print("方法结束")


if __name__ == '__main__':
    test()


# 常见错误类型及继承
# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
# +-- StopIteration
# +-- StopAsyncIteration
# +-- ArithmeticError
# |    +-- FloatingPointError
# |    +-- OverflowError
# |    +-- ZeroDivisionError
# +-- AssertionError
# +-- AttributeError
# +-- BufferError
# +-- EOFError
# +-- ImportError
# |    +-- ModuleNotFoundError
# +-- LookupError
# |    +-- IndexError
# |    +-- KeyError
# +-- MemoryError
# +-- NameError
# |    +-- UnboundLocalError
# +-- OSError
# |    +-- BlockingIOError
# |    +-- ChildProcessError
# |    +-- ConnectionError
# |    |    +-- BrokenPipeError
# |    |    +-- ConnectionAbortedError
# |    |    +-- ConnectionRefusedError
# |    |    +-- ConnectionResetError
# |    +-- FileExistsError
# |    +-- FileNotFoundError
# |    +-- InterruptedError
# |    +-- IsADirectoryError
# |    +-- NotADirectoryError
# |    +-- PermissionError
# |    +-- ProcessLookupError
# |    +-- TimeoutError
# +-- ReferenceError
# +-- RuntimeError
# |    +-- NotImplementedError
# |    +-- RecursionError
# +-- SyntaxError
# |    +-- IndentationError
# |         +-- TabError
# +-- SystemError
# +-- TypeError
# +-- ValueError
# |    +-- UnicodeError
# |         +-- UnicodeDecodeError
# |         +-- UnicodeEncodeError
# |         +-- UnicodeTranslateError
# +-- Warning
# +-- DeprecationWarning
# +-- PendingDeprecationWarning
# +-- RuntimeWarning
# +-- SyntaxWarning
# +-- UserWarning
# +-- FutureWarning
# +-- ImportWarning
# +-- UnicodeWarning
# +-- BytesWarning
# +-- ResourceWarning


# 2. 调用栈
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()
