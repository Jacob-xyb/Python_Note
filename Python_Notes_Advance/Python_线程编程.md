# Python 协程

## 从一个爬虫说起

```python
import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))
    
def main(urls):
    for url in urls:
        crawl_page(url)
        
%time main(['url_1', 'url_2', 'url_3', 'url_4'])

"""
crawling url_1
OK url_1
crawling url_2
OK url_2
crawling url_3
OK url_3
crawling url_4
OK url_4
CPU times: total: 0 ns
Wall time: 10 s
"""
```

注意：本节的主要目的是协程的基础概念，因此我们简化爬虫的 `scrawl_page` 函数为休眠数秒，休眠时间取决于 `url` 最后的那个数字。

这是一个很简单的爬虫，main() 函数执行时，调取 crawl_page() 函数进行网络通信，经过若干秒等待后收到结果，然后执行下一个。

看起来很简单，但你仔细一算，它也占用了不少时间，五个页面分别用了 1 秒到 4 秒的时间，加起来一共用了 10 秒。这显然效率低下，该怎么优化呢？

于是，一个很简单的思路出现了——我们这种爬取操作，完全可以并发化。我们就来看看使用协程怎么写。

```python
import asyncio
import time

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
async def main(urls):
    for url in urls:
        await crawl_page(url)
        
# jupyter
t1 = time.time()
await main(['url_1', 'url_2', 'url_3', 'url_4'])
t2 = time.time()
print(t2 -t1) 

# Ipython
# %time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

"""
crawling url_1
OK url_1
crawling url_2
OK url_2
crawling url_3
OK url_3
crawling url_4
OK url_4
10.015552520751953
"""
```

代码说明：

`import asyncio`，这个库包含了大部分实现协程所需的魔法工具

`async` 修饰词声明异步函数，于是，这里的 `crawl_page` 和 `main` 都变成了异步函数。而调用异步函数便可得到一个协程对象`（coroutine object）`。

例如：打印 `crawl_page('')` 并不会执行它，而是返回一个协程对象。

```python
print(crawl_page(''))	# <coroutine object crawl_page at 0x000001CF7E215540>
```

再来说说协程的执行。执行协程有多种方法，这里主要介绍一下常用的三种。

1. **await 调用**

首先可以通过 `await` 来调用。await 执行的效果，和 Python 正常执行是一样的，也就是说程序会阻塞在这里，进入被调用的协程函数，执行完毕返回后再继续，而这也是await 的字面意思。

代码中 `await asyncio.sleep(sleep_time)` 会在这里休息若干秒，`await crawl_page(url)` 则会执行 crawl_page() 函数。

2. **asyncio.create_task()**

通过 asyncio.create_task() 来创建任务

3. **asyncio.run()**

`asyncio.run()` 触发运行 ( Python 3.7 之后才有的特性 )。

可以让 Python 的协程接口变得非常简单，你不用去理会事件循环怎么定义和怎么使用的问题。一个非常好的编程规范是，`asyncio.run(main())` 作为主程序的入口函数，在程序运行周期内，只调用一次 asyncio.run。

---

这样，你就大概看懂了协程是怎么用的吧。不妨试着跑一下代码，欸，怎么还是 10 秒？

10 秒就对了，还记得上面所说的，**await 是同步调用**，因此， crawl_page(url) 在当前的调用结束之前，是不会触发下一次调用的。于是，这个代码效果就和上面完全一样了，相当于我们用 **异步接口写了个同步代码**。现在又该怎么办呢？

其实很简单，也正是我接下来要讲的协程中的一个重要概念，**任务（Task）**。老规矩，先看代码。

```python
import asyncio
import time

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task
        
# jupyter
t1 = time.time()
await main(['url_1', 'url_2', 'url_3', 'url_4'])
t2 = time.time()
print(t2 -t1) 

# Ipython
# %time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

"""
crawling url_1
crawling url_2
crawling url_3
crawling url_4
OK url_1
OK url_2
OK url_3
OK url_4
4.0193517208099365
"""
```

你可以看到，我们有了协程对象后，便可以通过 `asyncio.create_task` 来创建任务。任务创建后很快就会被调度执行，这样，我们的代码也不会阻塞在任务这里。所以，我们要等所有任务都结束才行，用 `for task in tasks: await task` 即可。

这次，你就看到效果了吧，结果显示，运行总时长等于运行时间最长的爬虫。

当然，你也可以想一想，这里用多线程应该怎么写？而如果需要爬取的页面有上万个又该怎么办呢？再对比下协程的写法，谁更清晰自是一目了然。

其实，对于执行 tasks，还有另一种做法：

```python
import asyncio
import time

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)
        
# jupyter
t1 = time.time()
await main(['url_1', 'url_2', 'url_3', 'url_4'])
t2 = time.time()
print(t2 -t1) 

# Ipython
# %time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

"""
crawling url_1
crawling url_2
crawling url_3
crawling url_4
OK url_1
OK url_2
OK url_3
OK url_4
4.016194105148315
"""
```

这里的代码也很好理解。唯一要注意的是，*tasks 解包列表，将列表变成了函数的参数；与之对应的是， ** dict 将字典变成了函数的参数。

另外，`asyncio.create_task`，`asyncio.run` 这些函数都是 Python 3.7 以上的版本才提供的，自然，相比于旧接口它们也更容易理解和阅读。

## 解密协程运行时

举例两段代码来解密协程过程：

代码段1：

```python
import asyncio


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')
    
async def main():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')
    

# jupyter
t1 = time.time()
await main()
t2 = time.time()
print(t2 -t1) 
    
# Ipython
# %time asyncio.run(main())

"""
before await
worker_1 start
worker_1 done
awaited worker_1
worker_2 start
worker_2 done
awaited worker_2
3.020576000213623
"""
```

代码段2：

```python
import asyncio


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')
    
async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')
    

# jupyter
t1 = time.time()
await main()
t2 = time.time()
print(t2 -t1) 
    
# Ipython
# %time asyncio.run(main())

"""
before await
worker_1 start
worker_2 start
worker_1 done
awaited worker_1
worker_2 done
awaited worker_2
2.0118842124938965
"""
```

第一个代码很好理解，等待当前函数执行完后执行下一步，不过，第二个代码，到底发生了什么呢？

为了更详细了解到协程和线程的具体区别，这里将详细分析整个过程。

1. asyncio.run(main())，程序进入 main() 函数，事件循环开启；
2. task1 和 task2 任务被创建，并进入事件循环等待运行；运行到 print，输出 'before await'；
3. **`await task1` 执行，用户选择从当前的主任务中切出，事件调度器开始调度 worker_1**；
4. worker_1 开始运行，运行 print 输出 `worker_1 start`，然后运行到 await asyncio.sleep(1)，从当前任务切出，事件调度器开始调度 worker_2；

5. worker_2 开始运行，运行 print 输出 'worker_2 start'，然后运行 await asyncio.sleep(2) 从当前任务切出；
6. 以上所有事件的运行时间，都应该在 1ms 到 10ms 之间，甚至可能更短，事件调度器从这个时候开始暂停调度；
7. 一秒钟后，worker_1 的 sleep 完成，事件调度器将控制权重新传给 task_1，输出 'worker_1 done'，**task_1 完成任务**，从事件循环中退出；
8. await task1 完成，事件调度器将控制器传给主任务，输出 'awaited worker_1'，然后在 await task2 处继续等待；
9. 两秒钟后，worker_2 的 sleep 完成，事件调度器将控制权重新传给 task_2，输出 'worker_2 done'，task_2 完成任务，从事件循环中退出；
10. 主任务输出 'awaited worker_2'，协程全任务结束，事件循环结束。

### 加深解密协程运行流程

```python
import asyncio


async def worker_1():
    print('worker_1 start')
#     await asyncio.sleep(1)
    time.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')


# jupyter
t1 = time.time()
await main()
t2 = time.time()
print(t2 - t1)

# Ipython
# %time asyncio.run(main())

"""
before await
worker_1 start
worker_1 done
worker_2 start
awaited worker_1
worker_2 done
awaited worker_2
3.015061378479004
"""
```

如果只是简单的 `time.sleep(1)` 就不会在调度 worker_1 时切换到 worker_2，先执行完 `worker_1 `  后直接切换到 `worker_2` 然后 `await task1` 完成，一直运行到 `await task2` 直到 `worker_2` 执行完。

```python
import asyncio


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task2
    print('awaited worker_2')
    await task1
    print('awaited worker_1')


# jupyter
t1 = time.time()
await main()
t2 = time.time()
print(t2 - t1)

# Ipython
# %time asyncio.run(main())

"""
before await
worker_1 start
worker_2 start
worker_1 done
worker_2 done
awaited worker_2
awaited worker_1
2.027482032775879
"""
```

`asyncio.create_task()` 的顺序是在调用时就固定了的，与 `await` 调用的对象无关。

## 限定协程任务时长

进阶一下，如果我们想给某些协程任务限定运行时间，一旦超时就取消，又该怎么做呢？再进一步，如果某些协程运行时出现错误，又该怎么处理呢？同样的，来看代码。

```python
import asyncio
import time

async def worker_1():
    await asyncio.sleep(1)
    print('worker_1 done')
    return 1


async def worker_2():
    await asyncio.sleep(2)
    print('worker_2 done')
    return 2 / 0


async def worker_3():
    await asyncio.sleep(3)
    return 3

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    task3 = asyncio.create_task(worker_3())
    
    await asyncio.sleep(2)
    task3.cancel()
    
    res = await asyncio.gather(task1, task2, task3, return_exceptions=True)
    print(res)


# jupyter
t1 = time.time()
await main()
t2 = time.time()
print(t2 - t1)

# Ipython
# %time asyncio.run(main())

"""
worker_1 done
worker_2 done
[1, ZeroDivisionError('division by zero'), CancelledError()]
1.9989843368530273
"""
```

可以看到，worker_1 正常运行，worker_2 运行中出现错误，worker_3 执行时间过长被我们 cancel 掉了，这些信息会全部体现在最终的返回结果 res 中。

不过要注意return_exceptions=True这行代码。如果不设置这个参数，错误就会完整地 throw 到我们这个执行层，从而需要 try except 来捕捉，这也就意味着其他还没被执行的任务会被全部取消掉。为了避免这个局面，我们将return_exceptions 设置为 True 即可。

到这里，其实已经发现，线程能实现的，协程都能做到。

# Python 并发编程

## 区分并发和并行

并发应用场景：通过并发实现对低速io访问的延迟隐藏（一般是网络I/O或磁盘I/O），以及防止界面的阻塞。典型场景，多线程下载，后台打印等等。

并行应用场景：当系统上有超过1个CPU的时候，通过并行算法让每个处理器执行计算任务的一部分，共同完成计算来提高速度。

---

在我们学习并发编程时，常常同时听到并发（Concurrency）和并行（Parallelism）这两个术语，这两者经常一起使用，导致很多人以为它们是一个意思，其实不然。

首先你要辨别一个误区，在 Python 中，并发并不是指同一时刻有多个操作（thread、task）同时进行。相反，某个特定的时刻，它只允许有一个操作发生，只不过线程 / 任务之间会互相切换，直到完成。我们来看下面这张图：

![image-20220808162850088](https://s2.loli.net/2022/08/08/7mOTYfFSdM4i2s3.png)

图中出现了 thread 和 task 两种切换顺序的不同方式，分别对应 Python 中并发的两种形式——threading 和 asyncio。

对于 threading，操作系统知道每个线程的所有信息，因此它会做主在适当的时候做线程切换。很显然，这样的好处是代码容易书写，因为程序员不需要做任何切换操作的处理；但是切换线程的操作，也有可能出现在一个语句执行的过程中（比如 x += 1），这样就容易出现 race condition 的情况。

而对于 asyncio，主程序想要切换任务时，必须得到此任务可以被切换的通知，这样一来也就可以避免刚刚提到的 race condition 的情况。

至于所谓的并行，指的才是同一时刻、同时发生。Python 中的 multi-processing 便是这个意思，对于 multi-processing，你可以简单地这么理解：比如你的电脑是 6 核处理器，那么在运行程序时，就可以强制 Python 开 6 个进程，同时执行，以加快运行速度，它的原理示意图如下：

![image-20220808163010096](https://s2.loli.net/2022/08/08/YnjLPy6DXUOTWlo.png)

对比看来，并发通常应用于 I/O 操作频繁的场景，比如你要从网站上下载多个文件，I/O 操作的时间可能会比 CPU 运行处理的时间长得多。

而并行则更多应用于 CPU heavy 的场景，比如 MapReduce 中的并行计算，为了加快运行速度，一般会用多台机器、多个处理器来完成。

## Futures

### 单线程与多线程性能比较

通过具体实例来比较性能

假设我们有一个任务，是下载一些网站的内容并打印。如果用单线程的方式，它的代码实现如下所示（为了简化代码，突出主题，此处我忽略了异常处理）：

```python
import requests
import time

def download_one(url):
	resp = requests.get(url)
	print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
	for site in sites:
		download_one(site)
        
def main():
    sites = [
		'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
	]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
	main()
    
# 输出
"""
...
Download 15 sites in 2.464231112999869 seconds
"""
```

这种方式应该是最直接也最简单的：先是遍历存储网站的列表；然后对当前网站执行下载操作；等到当前操作完成后，再对下一个网站进行同样的操作，一直到结束。

我们可以看到总共耗时约 2.4s。单线程的优点是简单明了，但是明显效率低下，因为上述程序的绝大多数时间，都浪费在了 I/O 等待上。程序每次对一个网站执行下载操作，都必须等到前一个网站下载完成后才能开始。如果放在实际生产环境中，我们需要下载的网站数量至少是以万为单位的，不难想象，这种方案根本行不通。

多线程版本的代码实现：

```python
import requests
import concurrent.futures
import threading
import time

def download_one(url):
	resp = requests.get(url)
	print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)
        
def main():
    sites = [
		'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
	]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
	main()
    
# 输出
"""
...
Download 15 sites in 0.19936635800002023 seconds
"""
```

非常明显，总耗时是 0.2s 左右，效率一下子提升了 10 倍多。

我们具体来看这段代码，它是多线程版本和单线程版的主要区别所在：

```python
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)
```

这里我们创建了一个线程池，总共有 5 个线程可以分配使用。**executer.map() 与前面所讲的 Python 内置的 map() 函数类似，表示对 sites 中的每一个元素，并发地调用函数 download_one()。**

顺便提一下，在 download_one() 函数中，我们使用的 requests.get() 方法是线程安全的（thread-safe），因此在多线程的环境下，它也可以安全使用，并不会出现 race condition 的情况。

另外，虽然线程的数量可以自己定义，但是线程数并不是越多越好，因为线程的创建、维护和删除也会有一定的开销。所以如果你设置的很大，反而可能会导致速度变慢。我们往往需要根据实际的需求做一些测试，来寻找最优的线程数量。

当然，我们也可以用并行的方式去提高程序运行效率。你只需要在 download_all() 函数中，做出下面的变化即可：

```python
with futures.ThreadPoolExecutor(workers) as executor
=>
with futures.ProcessPoolExecutor() as executor:
```

在需要修改的这部分代码中，函数 ProcessPoolExecutor() 表示创建进程池，使用多个进程并行的执行程序。不过，这里我们通常省略参数 workers，因为系统会自动返回 CPU 的数量作为可以调用的进程数。

我刚刚提到过，并行的方式一般用在 CPU heavy 的场景中，因为对于 I/O heavy 的操作，多数时间都会用于等待，相比于多线程，使用多进程并不会提升效率。反而很多时候，因为CPU 数量的限制，会导致其执行效率不如多线程版本。

### 到底什么是 Futures ？

Python 中的 Futures 模块，位于 concurrent.futures 和 asyncio 中，它们都表示带有延迟的操作。Futures 会将处于等待状态的操作包裹起来放到队列中，这些操作的状态随时可以查询，当然，它们的结果或是异常，也能够在操作完成后被获取。

通常来说，作为用户，我们不用考虑如何去创建 Futures，这些 Futures 底层都会帮我们处理好。我们要做的，实际上是去 schedule 这些 Futures 的执行。

比如，Futures 中的 Executor 类，当我们执行 executor.submit(func) 时，它便会安排里面的 func() 函数执行，并返回创建好的 future 实例，以便你之后查询调用。

这里再介绍一些常用的函数。Futures 中的方法 done()，表示相对应的操作是否完成——True 表示完成，False 表示没有完成。不过，要注意，done() 是 non-blocking 的，会立即返回结果。相对应的 add_done_callback(fn)，则表示 Futures 完成后，相对应的参数函数 fn，会被通知并执行调用。

Futures 中还有一个重要的函数 result()，它表示当 future 完成后，返回其对应的结果或异常。而 as_completed(fs)，则是针对给定的 future 迭代器 fs，在其完成后，返回完成后的迭代器。

所以，上述例子也可以写成下面的形式：

```python
import requests
import concurrent.futures
import threading
import time

def download_one(url):
	resp = requests.get(url)
	print('Read {} from {}'.format(len(resp.content), url))

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            future.result()
        
def main():
    sites = [
		'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
	]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
	main()
```

这里，我们首先调用 executor.submit()，将下载每一个网站的内容都放进 future 队列 to_do，等待执行。然后是 as_completed() 函数，在 future 完成后，便输出结果。

不过，这里要注意，future 列表中每个 future 完成的顺序，和它在列表中的顺序并不一定完全一致。到底哪个先完成、哪个后完成，取决于系统的调度和每个 future 的执行时间。

### 为什么多线程每次只能有一个线程执行？
前面我说过，同一时刻，Python 主程序只允许有一个线程执行，所以 Python 的并发，是通过多线程的切换完成的。你可能会疑惑这到底是为什么呢？

这里我简单提一下全局解释器锁的概念，具体内容后面会讲到。

事实上，Python 的解释器并不是线程安全的，为了解决由此带来的 race condition 等问题，Python 便引入了全局解释器锁，也就是同一时刻，只允许一个线程执行。当然，在执行 I/O 操作时，如果一个线程被 block 了，全局解释器锁便会被释放，从而让另一个线程能够继续执行。

# 并发编程之Asyncio

Python 并发编程的一种实现是多线程，另一种实现方式是 `Asyncio`。

诚然，多线程有诸多优点且应用广泛，但也存在一定的局限性：

	比如，多线程运行过程容易被打断，因此有可能出现 race condition 的情况；
	
	再如，线程切换本身存在一定的损耗，线程数不能无限增加，因此，如果你的 I/O 操作
非常 heavy，多线程很有可能满足不了高效率、高质量的需求

正是为了解决这些问题，Asyncio 应运而生。

## 什么是 Asyncio

### Sync VS Async

Sync（同步）和 Async（异步）:

	所谓 Sync，是指操作一个接一个地执行，下一个操作必须等上一个操作完成后才能执行。
	
	而 Async 是指不同操作间可以相互交替执行，如果其中的某个操作被 block 了，程序并不会等待，而是会找出可执行的操作继续执行。

### Asyncio 工作原理

事实上，Asyncio 和其他 Python 程序一样，是单线程的，它只有一个主线程，但是可以进行多个不同的任务（task），这里的任务，就是特殊的 future 对象。这些不同的任务，被一个叫做 event loop 的对象所控制。你可以把这里的任务，类比成多线程版本里的多个线程。

### TODO

# 全局解释器锁

## TODO