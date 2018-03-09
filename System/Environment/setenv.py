import os
print('setenv...',end=' ')
print(os.environ['user'])
os.environ['user']='Brian'
os.system('python echoenv.py')
os.environ['user']='Arthur'
os.system('pyton echoenv.py')
os.environ['user']=input('?')
print(os.popen('pthon echonv.py').read())