import asyncio
from time import strftime


async def late(delay, msg):
    await asyncio.sleep(delay)  # sleep returns control to the main loop.
    print(msg)


async def main_loop():
    print(f"> {strftime('%X')}")
    await late(5, "One")
    print(f"> {strftime('%X')}")
    await late(10, "Two")
    print(f"> {strftime('%X')}")

    # create_task adds calls to a list.
    # the late(15, "Three") is "called" and asyncio.sleep says: go on.
    # the late(20, "Four") is "called" and asyncio.sleep says: go on.
    # as .sleep said go on => ~the same time of timer in sleep of both calls.
    # then await task3 and we wait for task3 to stop sleeping.
    # when then await task4, we only wait a delta time.
    # async != parallelism, only one process with a bunch of yield from calls.
    task3 = asyncio.create_task(late(15, "Three"))
    task4 = asyncio.create_task(late(20, "Four"))
    await task3
    print(f"> {strftime('%X')}")
    await task4
    print(f"> {strftime('%X')}")

asyncio.run(main_loop())
