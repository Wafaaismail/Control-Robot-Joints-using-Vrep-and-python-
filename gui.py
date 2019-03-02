from tkinter import *
import vrep-main as vp
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 1
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn['text'] = "Total Clicks: 0"
        self.bttn['command'] = (self.callback)
        self.bttn.grid()

    def callback(self):
        self.bttn['text'] = "increase: " + str(self.bttn_clicks)
        if (bttn_clicks == 1):
            vp.inc_joint_pos(1,1)
            self.bttn_clicks+=1
        elif (bttn_clicks == 2):
            vp.inc_joint_pos(1,2)
            self.bttn_clicks+=1
        elif (bttn_clicks == 3):
            vp.inc_joint_pos(1,3)
            self.bttn_clicks+=1
        elif (bttn_clicks == 4):
            vp.inc_joint_pos(1,4)
            self.bttn_clicks+=1
        elif (bttn_clicks == 5):
            vp.inc_joint_pos(1,5)
            self.bttn_clicks+=1
        elif (bttn_clicks == 6):
            vp.inc_joint_pos(1,6)
            self.bttn_clicks =1



root = Tk()
root.title("Click Counter")
root.geometry('200x50')

app = Application(root)

root.mainloop()
