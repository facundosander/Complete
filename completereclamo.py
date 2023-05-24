import tkinter as tk
import pyautogui
import time


def on_enter(event):
    cargar_informacion()

def cargar_informacion():
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"-             Razon Social: {txt_razon_social.get()}\n")
    output.insert(tk.END, f"-                            Rut: {txt_rut.get()}\n")
    output.insert(tk.END, f"-                   Contacto: {txt_contacto.get()}\n")
    output.insert(tk.END, f"-                   Direccion: {txt_direccion.get()}\n")
    output.insert(tk.END, f"-                    Telefono: {txt_telefono.get()}\n")
    output.insert(tk.END, f"-                           Caja: {txt_caja.get()}\n")
    output.insert(tk.END, f"-       Codigo Comercio: {txt_codigo_comercio.get()}\n")
    output.insert(tk.END, f"-                    Terminal: {txt_terminal.get()}\n")
    output.insert(tk.END, f"-                         Error: {txt_descripcion.get()}\n")


    # Copia el texto generado al portapapeles
    root.clipboard_clear()
    root.clipboard_append(output.get("1.0", tk.END))

    # Abre el programa de gestión de tickets utilizando las coordenadas del clic del mouse
    pyautogui.click(x=217, y=1053)
    time.sleep(3)

    # Navega hasta la ventana o campo de texto donde se debe pegar el texto generado
    pyautogui.click(x=202, y=813)

    # Pega el texto generado en el cuadro de texto
    
    pyautogui.hotkey("ctrl", "v")

    # Carga la info al titulo
    titulo : str = f"{txt_descripcion.get()} / {txt_razon_social.get()}  "

    # Navega hasta la ventana o campo de texto donde se debe pegar el texto generado
    pyautogui.click(x=202, y=781)
    pyautogui.typewrite(titulo) 
    for char in txt_descripcion.get():
        if char == ',':
            break
        pyautogui.typewrite(char) 
    
    #Navegar para enviar mail
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.click(x=765, y=403)
    time.sleep(0.2)
    pyautogui.click(x=806, y=446)
    time.sleep(0.2)
    pyautogui.click(x=847, y=674)
    time.sleep(2)
    mail : str = f"Buenas tardes, Buenos días,\n \n RUT: {txt_rut.get()}\n Razón Social: {txt_razon_social.get()}\n Dirección: {txt_direccion.get()}\n Terminal: {txt_terminal.get()}\n Código de comercio: {txt_codigo_comercio.get()}\n \nGracias y Saludos! "
    pyautogui.click(x=179, y=463)
    time.sleep(0.2)
    pyautogui.typewrite(mail)

    txt_razon_social.delete(0, tk.END)
    txt_rut.delete(0, tk.END)
    txt_codigo_comercio.delete(0, tk.END)
    txt_caja.delete(0, tk.END)
    txt_contacto.delete(0, tk.END)
    txt_direccion.delete(0, tk.END)
    txt_telefono.delete(0, tk.END)
    txt_terminal.delete(0, tk.END)
    txt_descripcion.delete(0, tk.END)

def crear_ticket():
    # Abre el programa de gestión de tickets utilizando las coordenadas del clic del mouse
    pyautogui.click(x=217, y=1053)
    time.sleep(3)

    # Navega hasta la ventana o campo de texto donde se debe pegar el texto generado
    pyautogui.click(x=202, y=813)

    pyautogui.hotkey("ctrl", "t")
    time.sleep(3)
    pyautogui.click(x=569, y=172)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.click(x=564, y=267)
    time.sleep(0.2)
    pyautogui.click(x=589, y=584)
    time.sleep(0.2)
    pyautogui.click(x=816, y=679)
    time.sleep(0.2)
    pyautogui.click(x=1062, y=503)
    time.sleep(0.2)
    pyautogui.click(x=1326, y=389)
    time.sleep(0.2)
    pyautogui.click(x=916, y=215)
    time.sleep(0.2)
    pyautogui.click(x=611, y=297)
    time.sleep(0.2)
    pyautogui.click(x=839, y=285)
    time.sleep(0.2)
    pyautogui.click(x=917, y=244)
    time.sleep(0.2)
    pyautogui.click(x=917, y=244)
    time.sleep(0.2)
    pyautogui.click(x=786, y=506)
    time.sleep(0.2)
    #pyautogui.click(x=1512, y=125)

# Crear la ventana principal
root = tk.Tk()
root.title("AutoCompleteTransAct")

# Crear y agregar widgets (etiquetas, campos de texto, botones, etc.)
label_razon_social = tk.Label(root, text="Razon Social:")
label_razon_social.pack()
txt_razon_social = tk.Entry(root)
txt_razon_social.pack()

label_rut = tk.Label(root, text="Rut:")
label_rut.pack()
txt_rut = tk.Entry(root)
txt_rut.pack()

label_contacto = tk.Label(root, text="contacto:")
label_contacto.pack()
txt_contacto = tk.Entry(root)
txt_contacto.pack()

label_direccion = tk.Label(root, text="contacto:")
label_direccion.pack()
txt_direccion = tk.Entry(root)
txt_direccion.pack()

label_telefono = tk.Label(root, text="telefono:")
label_telefono.pack()
txt_telefono = tk.Entry(root)
txt_telefono.pack()

label_caja = tk.Label(root, text="caja:")
label_caja.pack()
txt_caja = tk.Entry(root)
txt_caja.pack()

label_codigo_comercio = tk.Label(root, text="Codigo de Comercio:")
label_codigo_comercio.pack()
txt_codigo_comercio = tk.Entry(root)
txt_codigo_comercio.pack()

label_terminal = tk.Label(root, text="terminal:")
label_terminal.pack()
txt_terminal = tk.Entry(root)
txt_terminal.pack()

label_descripcion = tk.Label(root, text="descripcion:")
label_descripcion.pack()
txt_descripcion = tk.Entry(root)
txt_descripcion.pack()

# Crear el botón "Cargar información" y asociarlo a la función cargar_informacion
btn_cargar = tk.Button(root, text="Cargar información", command=cargar_informacion)
btn_cargar.pack()

# Crear el botón "Cargar ticket" y asociarlo a la función cargar_informacion
btn_ticket = tk.Button(root, text="Crear ticket", command=crear_ticket)
btn_ticket.pack()

#Crea output y titulo
output = tk.Text(root, wrap=tk.WORD)
output.pack()

# Vincular la tecla Enter al botón "Cargar información"
root.bind('<Return>', on_enter)

# Ejecutar el bucle principal de eventos
root.mainloop()