import tkinter as tk
import pyautogui
import time


def on_enter(event):
    cargar_informacion()

def cargar_informacion():

    #Carga la info al output
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"-  Requiere habilitacion: {txt_habilitacion.get()}\n")
    output.insert(tk.END, f"-      Ultima transaccion: {txt_ultima.get()}\n")
    output.insert(tk.END, f"-               Empresa / RUT: {txt_empresa.get()}\n")
    output.insert(tk.END, f"-                    Contacto: {txt_contacto.get()}\n")
    output.insert(tk.END, f"-                   Direccion: {txt_direccion.get()}\n")
    output.insert(tk.END, f"-                    Telefono: {txt_telefono.get()}\n")
    output.insert(tk.END, f"-                          Serie: {txt_serie.get()}\n")
    output.insert(tk.END, f"-                    Producto: Transact\n")
    output.insert(tk.END, f"-                      Modelo: {txt_modelo.get()}\n")
    output.insert(tk.END, f"-                      Version: {txt_version.get()}\n")
    output.insert(tk.END, f"-                    Terminal: {txt_terminal.get()}\n")
    output.insert(tk.END, f"-                  Integrador: {txt_integrador.get()}\n")
    output.insert(tk.END, f"- Detalle del problema: {txt_descripcion.get()}\n")

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
    titulo : str = f"{txt_modelo.get()} / {txt_serie.get()} / "

    # Navega hasta la ventana o campo de texto donde se debe pegar el texto generado
    pyautogui.click(x=202, y=781)
    pyautogui.typewrite(titulo) 
    for char in txt_descripcion.get():
        if char == ',':
            break
        pyautogui.typewrite(char) 
    
    #Navegar para enviar mail a Fede
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.click(x=678, y=381)
    time.sleep(0.2)
    pyautogui.click(x=744, y=614)
    time.sleep(0.2)
    pyautogui.hotkey("f")
    time.sleep(0.2)
    pyautogui.hotkey("f")
    time.sleep(0.2)
    pyautogui.click(x=1163, y=330)
    time.sleep(2)
    #pyautogui.click(x=384, y=195)

    txt_habilitacion.delete(0, tk.END)
    txt_ultima.delete(0, tk.END)
    txt_empresa.delete(0, tk.END)
    txt_contacto.delete(0, tk.END)
    txt_direccion.delete(0, tk.END)
    txt_telefono.delete(0, tk.END)
    txt_serie.delete(0, tk.END)
    txt_modelo.delete(0, tk.END)
    txt_version.delete(0, tk.END)
    txt_terminal.delete(0, tk.END)
    txt_integrador.delete(0, tk.END)
    txt_descripcion.delete(0, tk.END)

def crear_ticket():
    # Abre el programa de gestión de tickets utilizando las coordenadas del clic del mouse
    pyautogui.click(x=217, y=1053)
    time.sleep(3)

    # Navega hasta la ventana o campo de texto donde se debe pegar el texto generado
    pyautogui.click(x=202, y=813)

    pyautogui.hotkey("ctrl", "t")
    time.sleep(5)
    pyautogui.click(x=569, y=172)
    time.sleep(0.2)
    pyautogui.press('enter')
    pyautogui.click(x=564, y=267)
    time.sleep(0.2)
    pyautogui.click(x=616, y=588)
    time.sleep(0.2)
    pyautogui.click(x=820, y=698)
    time.sleep(0.2)
    pyautogui.click(x=1108, y=546)
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
label_habilitacion = tk.Label(root, text="Requiere habilitacion:")
label_habilitacion.pack()
txt_habilitacion = tk.Entry(root)
txt_habilitacion.pack()

label_ultima = tk.Label(root, text="Ultima transaccion:")
label_ultima.pack()
txt_ultima = tk.Entry(root)
txt_ultima.pack()

label_empresa = tk.Label(root, text="Empresa:")
label_empresa.pack()
txt_empresa = tk.Entry(root)
txt_empresa.pack()

label_contacto = tk.Label(root, text="contacto:")
label_contacto.pack()
txt_contacto = tk.Entry(root)
txt_contacto.pack()

label_direccion = tk.Label(root, text="direccion:")
label_direccion.pack()
txt_direccion = tk.Entry(root)
txt_direccion.pack()

label_telefono = tk.Label(root, text="telefono:")
label_telefono.pack()
txt_telefono = tk.Entry(root)
txt_telefono.pack()

label_serie = tk.Label(root, text="serie:")
label_serie.pack()
txt_serie = tk.Entry(root)
txt_serie.pack()

label_modelo = tk.Label(root, text="modelo:")
label_modelo.pack()
txt_modelo = tk.Entry(root)
txt_modelo.pack()

label_version = tk.Label(root, text="version:")
label_version.pack()
txt_version = tk.Entry(root)
txt_version.pack()


label_terminal = tk.Label(root, text="terminal:")
label_terminal.pack()
txt_terminal = tk.Entry(root)
txt_terminal.pack()

label_integrador = tk.Label(root, text="integrador:")
label_integrador.pack()
txt_integrador = tk.Entry(root)
txt_integrador.pack()

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