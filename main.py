from ptpython.repl import embed
import settings

import asyncio

loop = asyncio.get_event_loop()
counter = [0]

async def print_counter():
    """
    Coroutine that prints counters and saves it in a global variable.
    """
    while True:
        print('Counter: %i' % counter[0])
        counter[0] += 1
        await asyncio.sleep(3)


@asyncio.coroutine
def interactive_shell():
    """
    Coroutine that starts a Python REPL from which we can access the global
    counter variable.
    """
    print('You should be able to read and update the "counter[0]" variable from this shell.')
    yield from embed(globals=globals(), return_asyncio_coroutine=True, patch_stdout=True)

    # Stop the loop when quitting the repl. (Ctrl-D press.)
    loop.stop()

from graphics import Window, draw_frame
def main():
    d = Window(width=800, height=600, caption='pyBoxelEngine', resizable=True)
    asyncio.async(draw_frame(d))
    asyncio.async(print_counter())
    asyncio.async(interactive_shell())

    loop.run_forever()
    loop.close()


if __name__ == '__main__':
    main()
