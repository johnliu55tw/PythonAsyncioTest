import asyncio


async def slow_operation():
    print("This is slow operation...")
    await asyncio.sleep(1)
    print("Slow operation done!")
    return 'Future is done!'


def got_result(future):
    print(future.result())


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(slow_operation(), loop=loop)

loop.run_forever()
