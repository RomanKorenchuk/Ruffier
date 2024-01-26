from kivy.app import *
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.boxlayout import *
from kivy.uix.screenmanager import *
from kivy.uix.scrollview import *
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
from kivy.core.window import Window
from sits import Sits
from runner import Runner

Window.clearcolor = (0/255, 100/255, 0/255, 1)

age = 7
name = ""
p1, p2, p3 = 0, 0, 0
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", padding=8, spacing=8)
        instr = Label(text = txt_instruction)
        lbl1 = Label(text="Введіть ім'я:", halign="right")
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Введіть вік:", halign="right")
        self.in_age = TextInput(text="7", multiline=False)
        self.btn = Button(text="Почати",size_hint_y = 0.2, background_color = [.0, .50,.0, 1])
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        vl.add_widget(instr)
        vl.add_widget(line1)
        vl.add_widget(line2)
        vl.add_widget(self.btn)
        self.add_widget(vl)
    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)  
        instr = Label(text=txt_test1)
        lbl1 = Label(text='Рахуйте пульс')
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Введіть результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)  
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        self.btn = Button(text='Почати', size_hint_y=0.4,background_color = [.0, .50,.0, 1])
        self.btn.on_press = self.next
        vl.add_widget(instr)
        vl.add_widget(lbl1)
        vl.add_widget(self.lbl_sec)
        vl.add_widget(line)
        vl.add_widget(self.btn)
        self.add_widget(vl)
    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'

class SitsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vl2 = BoxLayout(orientation = "vertical")
        line = BoxLayout()
        vl1 = BoxLayout(orientation='vertical', size_hint=(0.3, 1))

        instr = Label(text=txt_sits)
        self.lbl_sits = Sits(30)
        self.run = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)

        vl1.add_widget(instr)
        vl1.add_widget(self.lbl_sits)
        line.add_widget(vl1)
        line.add_widget(self.run)

        self.btn = Button(text='Почати', size_hint_y= 0.2, background_color = [.0, .50,.0, 1])
        self.btn.on_press = self.next

        vl.add_widget(line)
        vl.add_widget(self.btn)
        self.add_widget(vl)

    def run_finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text = 'Продовжити'
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False
        self.stage = 0
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = Label(text='Рахуйте пульс')

        lbl_result1 = Label(text='Результат:', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result2 = Label(text='Результат після відпочинку:', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        self.btn = Button(text='Почати', size_hint_y = 0.5,background_color = [.0, .50,.0, 1])
        self.btn.on_press = self.next
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vl.add_widget(instr)
        vl.add_widget(self.lbl1)
        vl.add_widget(self.lbl_sec)
        vl.add_widget(line1)
        vl.add_widget(line2)
        vl.add_widget(self.btn)
        self.add_widget(vl)


    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl1.text = 'Відпочивайте'
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.text='Рахуйте пульс'
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершити'
                self.next_screen = True
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 == False:
                p2 = 0
                self.in_result1.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.in_result2.text = str(p3)
            else:
                self.manager.current = 'result'

class ResultsScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text = '')
        self.vl.add_widget(self.instr)
        self.add_widget(self.vl)
        self.on_enter = self.before
    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name = "instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(SitsScr(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(ResultsScr(name = "result"))
        return sm

app = HeartCheck()
app.run()
