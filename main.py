import tkinter as tk
import ast

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    txt_result.delete(1.0,"end")
    txt_result.insert(1.0, calculation)


def calculation_equals_to():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0,result)
    except:
        clear_calculation()
        txt_result.insert(1.0,"Error")
        
        

def clear_calculation():
       global calculation
       calculation = ""
       txt_result.delete(1.0,"end")

    

main = tk.Tk()
main.geometry("330x240")
main.title("Calculator")
main.config(bg="white")
txt_result = tk.Text(main, height=2, width=22, font=("Arial", 25))
txt_result.grid(columnspan=5, pady=5)

btn_1 = tk.Button(main, text="1", command=lambda: add_to_calculation(1), width = 5, font=("arial", 15)) 
btn_1.grid(column=1, row = 2, columnspan=1)

btn_2 = tk.Button(main, text="2", command=lambda: add_to_calculation(2), width = 5, font=("arial", 15)) 
btn_2.grid(column=2, row = 2, columnspan=1)

btn_3 = tk.Button(main, text="3", command=lambda: add_to_calculation(3), width = 5, font=("arial", 15)) 
btn_3.grid(column=3, row = 2, columnspan=1)
btn_4 = tk.Button(main, text="4", command=lambda: add_to_calculation(4), width = 5, font=("arial", 15)) 
btn_4.grid(column=1, row = 3, columnspan=1)
btn_5 = tk.Button(main, text="5", command=lambda: add_to_calculation(5), width = 5, font=("arial", 15)) 
btn_5.grid(column=2, row = 3, columnspan=1)
btn_6 = tk.Button(main, text="6", command=lambda: add_to_calculation(6), width = 5, font=("arial", 15)) 
btn_6.grid(column=3, row = 3, columnspan=1)
btn_7 = tk.Button(main, text="7", command=lambda: add_to_calculation(7), width = 5, font=("arial", 15)) 
btn_7.grid(column=1, row = 4, columnspan=1)
btn_8 = tk.Button(main, text="8", command=lambda: add_to_calculation(8), width = 5, font=("arial", 15)) 
btn_8.grid(column=2, row = 4, columnspan=1)
btn_9 = tk.Button(main, text="9", command=lambda: add_to_calculation(9), width = 5, font=("arial", 15)) 
btn_9.grid(column=3, row = 4, columnspan=1)
btn_0 = tk.Button(main, text="0", command=lambda: add_to_calculation(0), width = 5, font=("arial", 15)) 
btn_0.grid(column=2, row = 5, columnspan=1)
btn_open_bracket = tk.Button(main, text="(", command=lambda: add_to_calculation("("), width = 5, font=("arial", 15)) 
btn_open_bracket.grid(column=1, row = 5, columnspan=1)
btn_close_bracket = tk.Button(main, text=")", command=lambda: add_to_calculation(")"), width = 5, font=("arial", 15)) 
btn_close_bracket.grid(column=3, row = 5, columnspan=1)
btn_add = tk.Button(main, text="+", command=lambda: add_to_calculation("+"), width = 5, font=("arial", 15)) 
btn_add.grid(column=4, row = 2, columnspan=1)
btn_minus = tk.Button(main, text="-", command=lambda: add_to_calculation("-"), width = 5, font=("arial", 15)) 
btn_minus.grid(column=4, row = 3, columnspan=1)
btn_multiply = tk.Button(main, text="*", command=lambda: add_to_calculation("*"), width = 5, font=("arial", 15)) 
btn_multiply.grid(column=4, row = 4, columnspan=1)
btn_div = tk.Button(main, text="/", command=lambda: add_to_calculation("/"), width = 5, font=("arial", 15)) 
btn_div.grid(column=4, row = 5, columnspan=1)
btn_equal = tk.Button(main, text="=", command= calculation_equals_to, width = 5, font=("arial", 15)) 
btn_equal.grid(column=4, row = 6, columnspan=1)
btn_AC = tk.Button(main, text="AC", command= clear_calculation, width =23, font=("arial", 15)) 
btn_AC.grid(column=1, row=6, columnspan=3, pady=5)

main.mainloop()
