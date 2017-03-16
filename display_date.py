import asyncio
import datetime
import random


# A coroutine function
async def display_date(num, interval, loop):
    end_time = loop.time() + interval
    while True:
        print("Coro ID: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(1, 4))


def result_callback(future):
    print("Got result: {}".format(future.result()))


loop = asyncio.get_event_loop()

# Create coroutine objects with coroutine function 'display_date'
coroObj1 = display_date(1, 50, loop)
coroObj2 = display_date(2, 50, loop)
coroObj3 = display_date(3, 30, loop)

# How to run coroutine with a event loop?
# 1. use 'asyncio.ensure_future' to add a coroutine object to the event loop
asyncio.ensure_future(coroObj1, loop)
# 2. use 'asyncio.ensure_future' to wrap a coroutine with Future, and use
# 3. use 'AbstractEventLoop.create_task'. This method returns a Task object
#    for 
task = loop.create_task(coroObj2)
