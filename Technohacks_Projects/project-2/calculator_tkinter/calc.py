import tkinter as tk
from tkinter import ttk

LIGHT_BLUE="#CCEDFF"
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GRAY = "#F5F5F5"
LABLE_COLOR = "#25265E"
WHITE="#FFFFFF"
DEFALUT_FONT_STYLE=("Arail",20)
OFF_WHITE="#F8FAFF"
DIGITS_FONT_STYLE=("Arial",24,'bold')

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("375x667")
        self.resizable(0, 0)
        self.title("")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()

        self.display_button = self.create_display_button()

        self.total_lable , self.lable = self.create_display_lables()

        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
            ".": (4, 1),
        }

        self.opreations={
            "/":"\u00F7" ,
            "*":"\u00D7",
            "-":"-",
            "+":"+"
        }

        self.create_digit_buttons()
        self.create_opretator()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.bind_keys()
        self.display_button.rowconfigure(0,weight=1)


        for x in range(1,5):
            self.display_button.rowconfigure(x,weight=1)
            self.display_button.columnconfigure(x,weight=1)
        
        
        
        self.mainloop()


    def bind_keys(self):
        self.bind("<Return>",lambda event:self.evaluate())

        for key in self.digits:
            self.bind(str(key),lambda event,digit=key:self.add_to_expression(digit))
        
        for key in self.opreations:
            self.bind(key,lambda event,operation=key:self.append_operator(operation))

    def create_display_lables(self):
        total_lable = tk.Label(
            self.display_frame,
            text=self.total_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABLE_COLOR,
            padx=24,
            font=SMALL_FONT_STYLE,    
        )

        total_lable.pack(expand=True, fill="both")

        lable = tk.Label(
            self.display_frame,
            text=self.total_expression,
            anchor=tk.E,
            bg=LIGHT_GRAY,
            fg=LABLE_COLOR,
            padx=24,
            font=LARGE_FONT_STYLE,
        )

        lable.pack(expand=True, fill="both")

        return total_lable,lable

    def create_display_frame(self):
        frame = tk.Frame(self, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")

        return frame


    def create_digit_buttons(self):
       for digit,grid_val in self.digits.items():
            button=tk.Button(self.display_button,text=f'{digit}',bg=WHITE,fg=LABLE_COLOR,font=DIGITS_FONT_STYLE,borderwidth=0,command=lambda x=digit :self.add_to_expression(x))
            
            button.grid(row=grid_val[0],column=grid_val[1],sticky='nsew')

    def append_operator(self,operator):
        self.current_expression +=operator
        self.total_expression += self.current_expression
        self.current_expression=""
        self.update_lable()
        self.update_total_lable()



    def create_opretator(self):
        i=0
        for operator,symbol in self.opreations.items():
            button=tk.Button(self.display_button,text=symbol,bg=OFF_WHITE,fg=LABLE_COLOR,font=DEFALUT_FONT_STYLE, borderwidth=0,command=lambda x=operator:self.append_operator(x))

            button.grid(row=i,column=4,sticky='nsew')
            i+=1

    def clear(self):
        self.total_expression=""
        self.current_expression=""
        self.update_lable()
        self.update_total_lable()


    def create_clear_button(self):
        button=tk.Button(self.display_button,text="C",bg=OFF_WHITE,fg=LABLE_COLOR,font=DEFALUT_FONT_STYLE,borderwidth=0,command=self.clear)

        button.grid(row=0,column=1,sticky='nsew')
    def square(self):
        self.current_expression =str(eval(f"{self.current_expression}**2"))
        self.update_lable()

    def create_square_button(self):
        button=tk.Button(self.display_button,text="x\u00b2",bg=OFF_WHITE,fg=LABLE_COLOR,font=DEFALUT_FONT_STYLE,borderwidth=0,command=self.square)

        button.grid(row=0,column=2,sticky='nsew')
    def sqrt(self):
        self.current_expression =str(eval(f"{self.current_expression}**.5"))
        self.update_lable()

    def create_sqrt_button(self):
        button=tk.Button(self.display_button,text="\u221ax",bg=OFF_WHITE,fg=LABLE_COLOR,font=DEFALUT_FONT_STYLE,borderwidth=0,command=self.sqrt)

        button.grid(row=0,column=3,sticky='nsew')

    def evaluate(self):
        self.total_expression += self.current_expression

        
        self.update_total_lable()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression= ""
        except Exception as a:
            self.current_expression="Error"
            if self.current_expression=="Error":
                self.total_expression= ""

        
        finally:
            self.update_lable()


    def create_equal_button(self):
        button=tk.Button(self.display_button,text="=",bg=LIGHT_BLUE ,fg=LABLE_COLOR,font=DEFALUT_FONT_STYLE,borderwidth=0,command=self.evaluate)

        button.grid(row=4,column=3,columnspan=2,sticky='nsew')
    
    def create_display_button(self):
        frame = tk.Frame(self)
        frame.pack(expand=True, fill="both")
        return frame
    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_lable()
    
    def update_lable(self):
        self.lable.config (text=self.current_expression[:11])

    def update_total_lable(self):
        expression=self.total_expression
        for operator,symbol in self.opreations.items():
            expression=expression.replace(operator,f' {symbol} ')

        self.total_lable.config(text=expression)



if __name__ == "__main__":
    Calculator()
