#question 1

import simpy 
def customer(env,server):
    arrive=env.now
    with server.request()as reg:
        yield reg
        print("waiting time:", env.now-arrive)
        yield env.timeout(3)

env=simpy.Environment()
server=simpy.Resource(env,capacity=1)
for i in range(5):
    env.process(customer(env,server))
    env.run()

#question2
import simpy 
def customer(env,server):
    arrive=env.now
    with server.request() as reg:
        yield reg
        print("wait:", env.now-arrive)
        yield env.timeout

env=simpy.Environment()
server=simpy.Resource(env,capacity=2)
for i in range(5):
    env.process(customer(env,server))

    env.run()

#question3
import simpy
def customer(env,server):
    with server.request() as reg:
        yield reg
        yield env.timeout(2)
def arrival(env,server):
    for i in range(5):
        env.process(customer(env,server))
        yield env.timeout(1)
env=simpy.Environment()
server=simpy.Resource(env,capacity=1)
env.process(arrival(env,server))
env.run()

#question4
wait=[1,2,3,4]
average =sum(wait)/len(wait)
print(("average waiting time:",average))