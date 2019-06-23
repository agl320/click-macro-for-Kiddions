from tkinter import *
from pynput.keyboard import Key, Controller, Listener
import time

schedule = []
scheduleLoop = []
scheduleDelay = []

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    global choice
    choice = key
    return False

def getButton():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    
    print(choice)
   
    varChoice.set(str(choice))

    labelChoice.grid(row = 0, column = 2, sticky = W)

def addToSchedule():
    global schedule
    global scheduleLoop
    global scheduleDelay
    
    schedule.append(choice)
    a = choice
    
    if(entryLoop.get()):
        scheduleLoop.append(entryLoop.get())
        b = entryLoop.get()
    else:
        scheduleLoop.append('1')  
        b = 1
        
    if(entryDelay.get()):
        scheduleDelay.append(entryDelay.get())
        c = entryDelay.get()
    else:
        scheduleDelay.append('0')
        c = 0
    
    
    scheduleBox.insert(END, '{} looped {} delay {}s'.format(a,b,c))

def deleteFromSchedule():
    schedule.pop()
    scheduleLoop.pop()
    scheduleDelay.pop()
    
    scheduleBox.delete(END)

def startSchedule():
    print('Loop started')
    for i in range(len(schedule)):
        print('Schedule Key {}'.format(schedule[i]))
        for x in range(int(scheduleLoop[i])):
            print('delay = {}'.format(scheduleDelay[i]))
  
             
             
             
    


kb = Controller()

root = Tk()
root.title('NEClicker 0.01')    

root.geometry('300x400')
root.pack_propagate(0)
root.resizable(0,0)

#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side = BOTTOM)

#GUI

labelIntro = Label(root, text='Key to loop', font = 'Times') #Label
labelIntro.grid(row=0, sticky = W, padx = 20)

varChoice = StringVar() #Creates instance of the key display
varChoice.set('Null')
labelChoice = Label(root, textvariable = varChoice, font = 'Times')
labelChoice.grid(row = 0, column = 2, sticky = W)

listenB = Button(root,text='Get Key', command = getButton, font = 'Times', width = 7) #Button to collect key
listenB.grid(row = 0, column = 1, sticky = W, pady = 10)

labelLoop = Label(root, text = 'Number of loops', font = 'Times') #number of loops
entryLoop = Entry(root, font = 'Times', width = 8)
labelLoop.grid(row = 2, column = 0, sticky = W, padx = 20)
entryLoop.grid(row = 2, column = 1, sticky = W)

labelDelay = Label(root, text = 'Delay', font = 'Times') #delay
entryDelay = Entry(root, font = 'Times', width = 8)
labelDelay.grid(row = 3, column = 0, sticky = W, padx = 20)
entryDelay.grid(row = 3, column = 0, sticky = E, padx = 20)

infLoop = Checkbutton(root, text = 'Infinite Loop', font = 'Times') #Infinite loop
infLoop.grid(row = 4, sticky = W, padx = 20)

addB = Button(root, text = '+', command = addToSchedule, font = 'Times', width = 3)
addB.grid(row = 3, column = 1, sticky = W, pady = 10)

addB = Button(root, text = '-', command = deleteFromSchedule, font = 'Times', width = 3) #delete from schedule
addB.grid(row = 3, column = 1, sticky = E, pady = 10)

startB = Button(root, text = 'Start', font = 'Times', width = 7, command = startSchedule) #start button
startB.grid(row = 5, column = 1, sticky = N, pady = 45)

stopB = Button(root, text = 'Stop', font = 'Times', width = 7) #stop button
stopB.grid(row = 5, column = 1, sticky = S, pady = 45)

scheduleBox = Listbox(root, font = ('Times',8)) #box
scheduleBox.grid(row = 5,padx = 20, sticky = W)
scheduleBox.configure(justify=CENTER)


root.mainloop()
