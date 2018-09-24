from tkinter import *
import TestBase
import sys
import inspect
import ChargingTest
import TestManager


testmanager = TestManager.test_manager()

def clicked():

    classinstances = []
    for checkbox in allcheckboxes:
        module = __import__(checkbox.MODULE)
        instance = getattr(module,
                           checkbox.CLASSNAME)
        classinstances.append(instance)
        print(instance)
    testmanager.run_all_tests_passed_from_ui(classinstances)



window = Tk()
window.title("python is for kindergardeners and losers")
label = Label(window,text="labelboye")
label.grid(column=0,row=0)
window.geometry('350x200')
button = Button(window,
    command=clicked,
    text="Run Tests", bg="orange", fg="black")
button.grid(column=1,row=3)


rowrow = 0
allcheckboxes = []
for childclass in TestBase.test_base.__subclasses__():
    check_state = BooleanVar()
    check_state.set(False)
    checkbox = Checkbutton(window,text=childclass.__name__,
            var=check_state)
    rowrow += 1
    checkbox.grid(column= 0, row=rowrow)
    checkbox.checkstate = True
    checkbox.MODULE = childclass.__module__
    checkbox.CLASSNAME = childclass.__name__
    allcheckboxes.append(checkbox)


window.mainloop()



