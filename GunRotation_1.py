from tkinter import *
import time


class RotorGun:

    def __init__(self):

        self.root = Tk()
        """WINDOW center"""
        self.root.geometry("500x500+850+100")
        """Window right side"""
        self.root.title('RotorGun Bot'.center(100))
        self.frame = Canvas(bg='light green', width=580, height=580)
        self.frame.pack()
        self.agent = ()
        self.gun_1 = ()
        self.gun_2 = ()
        self.gun_3 = ()
        self.gun_4 = ()
        self.gun_5 = ()
        self.gun_6 = ()
        self.gun_7 = ()
        self.gun_8 = ()
        self.gun_9 = ()
        self.gun_10 = ()
        self.gun_11 = ()
        self.gun_12 = ()
        self.gun_13 = ()
        self.gun_14 = ()
        self.gun_15 = ()
        self.gun_16 = ()

    def bot(self):

        r = (220, 220, 250, 250)
        r1 = (219, 219, 226, 226)
        r2 = (225, 215, 232, 222)
        r3 = (232, 213, 239, 220)
        r4 = (238, 215, 245, 222)
        r5 = (244, 218, 251, 225)
        r6 = (248, 224, 255, 231)
        r7 = (250, 230, 257, 237)
        r8 = (249, 236, 256, 243)
        r9 = (247, 242, 254, 249)
        r10 = (241, 246, 248, 253)
        r11 = (234, 249, 241, 256)
        r12 = (227, 248, 234, 255)
        r13 = (221, 245, 228, 252)
        r14 = (216, 239, 223, 246)
        r15 = (215, 232, 222, 239)
        r16 = (215, 225, 222, 232)

        self.agent = self.frame.create_oval(r, fill='cyan')
        self.gun_1 = self.frame.create_oval(r1, fill='red')
        self.gun_2 = self.frame.create_oval(r2, fill='red')
        self.gun_3 = self.frame.create_oval(r3, fill='red')
        self.gun_4 = self.frame.create_oval(r4, fill='red')
        self.gun_5 = self.frame.create_oval(r5, fill='red')
        self.gun_6 = self.frame.create_oval(r6, fill='red')
        self.gun_7 = self.frame.create_oval(r7, fill='red')
        self.gun_8 = self.frame.create_oval(r8, fill='red')
        self.gun_9 = self.frame.create_oval(r9, fill='red')
        self.gun_10 = self.frame.create_oval(r10, fill='red')
        self.gun_11 = self.frame.create_oval(r11, fill='red')
        self.gun_12 = self.frame.create_oval(r12, fill='red')
        self.gun_13 = self.frame.create_oval(r13, fill='red')
        self.gun_14 = self.frame.create_oval(r14, fill='red')
        self.gun_15 = self.frame.create_oval(r15, fill='red')
        self.gun_16 = self.frame.create_oval(r16, fill='red')

        # self.root.mainloop()

    def delete_guns(self):

        self.frame.delete(self.agent)
        self.frame.delete(self.gun_1)
        self.frame.delete(self.gun_2)
        self.frame.delete(self.gun_3)
        self.frame.delete(self.gun_4)
        self.frame.delete(self.gun_5)
        self.frame.delete(self.gun_6)
        self.frame.delete(self.gun_7)
        self.frame.delete(self.gun_8)
        self.frame.delete(self.gun_9)
        self.frame.delete(self.gun_10)
        self.frame.delete(self.gun_11)
        self.frame.delete(self.gun_12)
        self.frame.delete(self.gun_13)
        self.frame.delete(self.gun_14)
        self.frame.delete(self.gun_15)
        self.frame.delete(self.gun_16)

    def gunrotor(self):

        self.bot()
        time.sleep(1)
        self.delete_guns()

        r = (220, 220, 250, 250)
        self.agent = self.frame.create_oval(r, fill='cyan')
        self.frame.update()

        gun_states = [[1, (219, 219, 226, 226) ], [2, (225, 215, 232, 222)], [3, (232, 213, 239, 220)],
                      [4, (238, 215, 245, 222)], [5, (244, 218, 251, 225)], [6, (248, 224, 255, 231)],
                      [7, (250, 230, 257, 237)], [8, (249, 236, 256, 243)],[9, (247, 242, 254, 249)],
                      [10, (241, 246, 248, 253)], [11, (234, 249, 241, 256)], [12, (227, 248, 234, 255)],
                      [13, (221, 245, 228, 252)], [14, (216, 239, 223, 246)], [15, (215, 232, 222, 239)],
                      [16, (215, 225, 222, 232)]]

        """call gunrotor by state"""

        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r1 = gun_states[0][1]
                print(r1)
                self.gun_1 = self.frame.create_oval(r1, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_1)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r2 = gun_states[1][1]
                print(r2)
                self.gun_2 = self.frame.create_oval(r2, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_2)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r3 = gun_states[2][1]
                print(r3)
                self.gun_3 = self.frame.create_oval(r3, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_3)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r4 = gun_states[3][1]
                print(r4)
                self.gun_4 = self.frame.create_oval(r4, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_4)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r5 = gun_states[4][1]
                print(r5)
                self.gun_5 = self.frame.create_oval(r5, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_5)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r6 = gun_states[5][1]
                print(r6)
                self.gun_6 = self.frame.create_oval(r6, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_6)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r7 = gun_states[6][1]
                print(r7)
                self.gun_7 = self.frame.create_oval(r7, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_7)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r8 = gun_states[7][1]
                print(r8)
                self.gun_8 = self.frame.create_oval(r8, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_8)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r9 = gun_states[8][1]
                print(r9)
                self.gun_9 = self.frame.create_oval(r9, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_9)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r10 = gun_states[9][1]
                print(r10)
                self.gun_10 = self.frame.create_oval(r10, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_10)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r11 = gun_states[10][1]
                print(r11)
                self.gun_11 = self.frame.create_oval(r11, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_11)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r12 = gun_states[11][1]
                print(r12)
                self.gun_12 = self.frame.create_oval(r12, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_12)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r13 = gun_states[12][1]
                print(r13)
                self.gun_13 = self.frame.create_oval(r13, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_13)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r14 = gun_states[13][1]
                print(r14)
                self.gun_14 = self.frame.create_oval(r14, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_14)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r15 = gun_states[14][1]
                print(r15)
                self.gun_15 = self.frame.create_oval(r15, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_15)
        for i in range(1, 3):
            time.sleep(0.1)
            if i == 1:
                r16 = gun_states[15][1]
                print(r16)
                self.gun_16 = self.frame.create_oval(r16, fill='red')
                self.frame.update()
        self.frame.delete(self.gun_16)

        self.frame.update()

        self.root.mainloop()

data = RotorGun()
# data.bot()
data.gunrotor()
