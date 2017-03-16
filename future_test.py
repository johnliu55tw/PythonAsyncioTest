import asyncio
import random


async def slow_operation(future):
    sleepTime = random.randint(1, 3)
    print("This slow_operation will sleep for {}".format(sleepTime))
    await asyncio.sleep(sleepTime)
    future.set_result('Future is done after sleep {}!'.format(sleepTime))


def resultCallback(future):
    print("Got result: {}".format(future.result()))


loop = asyncio.get_event_loop()
futures = [asyncio.Future() for _ in range(4)]
print(futures)
for future in futures:
    future.add_done_callback(resultCallback)
    asyncio.ensure_future(slow_operation(future))

print("Entering loop")
loop.run_forever()

print(futures)
loop.close()
