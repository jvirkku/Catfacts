import tkinter as tk
import ttkbootstrap as ttk
import requests

       

def get_facts():
    factlist = []
    user_input  = entry_int.get()
    for i in range(1,user_input+1):
        response = requests.get(f'https://meowfacts.herokuapp.com/?count{i}')
        fact = response.json()['data'][0]
        factlist.append(fact)
    
    result = ""
    for i in range(user_input):
        result += f"Fact no {i+1}: {factlist[i]} \n"
        result += "\n"
    result +=  'I hope you learned something new today!'
    output_string.set(result)

        

window = ttk.Window(themename = 'minty')
window.title('Cat fact generator')
window.geometry('1000x500')


welcome_line = ttk.Label(master = window, text = 'Welcome to the cat fact generator!' + '\n' + '\n' + 'How many cat facts would you like to know today?',
                          font = 'Calibri 10')
welcome_line.pack(pady = 20)


input_box = tk.Frame(master = window, )
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_box, textvariable = entry_int, bootstyle = 'secondary')
button = ttk.Button(master = input_box, text = 'go!', command = get_facts, bootstyle = 'secondary')
entry.pack(side = 'left')
button.pack()
input_box.pack(pady = 20)

output_string = tk.StringVar()
output_print = ttk.Label(master = window, text = 'output', font = 'Calibri 10', textvariable = output_string )
output_print.pack()

window.mainloop()
