import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

def sync_calc_fib(n):
    if n in [1, 2]:
        return 1
    return sync_calc_fib(n - 1) + sync_calc_fib(n - 2)


def calc_fib(n):
    result = sync_calc_fib(n)
    print(f'第 {n} 项计算完成，结果是：{result}')
    return result

async def request(i):
    # asyncio.sleep(i)
    print(f'第 {i} 项请求')

async def main():
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks_list = [
            loop.run_in_executor(executor, calc_fib, 10),
            asyncio.create_task(request(5))
        ]
        await asyncio.gather(*tasks_list)
        end = time.perf_counter()
        print(f'总计耗时：{end - start}')


asyncio.run(main())