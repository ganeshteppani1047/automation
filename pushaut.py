import time, commands
global totalTime
def ganTe():
  startTime = time.time()
  time.sleep(6)
  endTime = time.time()
  global totalTime
  totalTime = round(endTime - startTime)
  while int(totalTime) > 5:
    x= commands.getoutput("git add . https://ganeshteppani1047:ganesh123@github.com/ganeshteppani1047/rep.git")
    x= commands.getoutput("git commit -m jf https://ganeshteppani1047:ganesh123@github.com/ganeshteppani1047/rep.git")
    x= commands.getoutput("git push https://ganeshteppani1047:ganesh123@github.com/ganeshteppani1047/rep.git")
    
    print(x)
    ganTe()
    break
ganTe()
