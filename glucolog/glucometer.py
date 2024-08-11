import flet as ft

def main(page: ft.Page):
    # Configurar el color de fondo de la ventana
    page.bgcolor = "white"
    page.title = "Gluco log"
    
    # Crear el campo de texto de entrada
    text_input = ft.TextField(
        label="Nivel de azúcar",
        border_color="black",  # Color del borde del campo de texto
        border_width=1,        # Ancho del borde
        padding=10             # Espaciado interno
    )
    
    # Crear el área de texto para mostrar la salida
    text_output = ft.Text(
        color="black"           # Color del texto
    )
   
    # Definir la función para manejar el clic del botón
    def on_button_click(e):
        text_output.text = text_input.value
        page.update()  # Actualizar la interfaz de usuario

    # Crear el botón
    button = ft.ElevatedButton(
        text="Enviar", 
        on_click=on_button_click,
        color="black",            # Color del texto del botón
        bgcolor="lightgray"       # Color de fondo del botón
    )
    
    # Agregar los componentes a la página
    page.add(
        ft.Column([
            ft.Row([
                text_input,
                button
            ]),
            text_output
        ], alignment="center")  # Centrar los elementos verticalmente
    )

if __name__ == '__main__':
    ft.app(target=main, port=8550)