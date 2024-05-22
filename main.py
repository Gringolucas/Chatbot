from Usuario import Usuario
from Chatbot import Chatbot
import speech_recognition as sr
chatbot = Chatbot()
recognizer = sr.Recognizer()
def menu(usuario, chatbot):
    while True:
        print("\nOpciones disponibles\n1- Contar un chiste\n2- Hacer una pregunta\n3- Ver historial de conversacion\n4- Cerrar sesion\n")
        print("Diga chiste, pregunta, historial o cerrar.")

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            opcion = recognizer.recognize_google(audio, language='es-ES')
            print(f"\nUsted seleccionó la opción: {opcion}")

            if opcion == 'chiste':
                chiste = chatbot.contar_chiste()
                print(f"\nChatbot: {chiste}")
                chatbot.guardar_conversacion(usuario.nombre, "Chiste", chiste)

            elif opcion == 'pregunta':
                pregunta = input("\nIngrese su pregunta:\n")
                respuesta = chatbot.responder_pregunta(pregunta)
                print(f"\nChatbot: {respuesta}")
                chatbot.guardar_conversacion(usuario.nombre, "Pregunta y Respuesta", f"Pregunta: {pregunta} - Respuesta: {respuesta}")

            elif opcion == 'historial':
                print("\nHistorial de Conversacion")
                usuario.mostrar_historial()

            elif opcion == 'cerrar':
                print("\nSesion Cerrada!\n")
                break

            else:
                print("\nOpción inválida. Por favor, elija una opción válida.")

        except sr.UnknownValueError:
            print("\nNo se pudo entender la opción.")
        except sr.RequestError:
            print("\nError al conectar con el servicio de reconocimiento de voz.")


def main():
  while True:
      print("¡Bienvenido al Chatbot!\n")
      print("1- Registrarse\n2- Iniciar sesión\n3- Salir\n")
      print("Diga registrarse, iniciar o salir.")

      with sr.Microphone() as source:
          recognizer.adjust_for_ambient_noise(source)
          audio = recognizer.listen(source)

      try:
          opcion = recognizer.recognize_google(audio, language='es-ES')
          print(f"\nUsted seleccionó la opción: {opcion}")

          if opcion == 'registrarse':
              while True:
                  nombre = input("\nIngrese su nombre: ")
                  email = input("Ingrese su email: ")

                  usuario = Usuario(nombre, email)
                  if usuario.registrarse():
                      break

          elif opcion == 'iniciar':
              nombre = input("\nIngrese su nombre: ")
              email = input("Ingrese su email: ")

              if Usuario.iniciar_sesion(nombre, email):
                  print(f"\nBienvenido de nuevo, {nombre}!\n")
                  print(chatbot.saludar())
                  menu(Usuario(nombre, email), chatbot)

              else:
                  print("\nUsuario no registrado. Por favor, regístrese primero.\n")

          elif opcion == 'salir':
              print("\n¡Hasta luego!")
              break

          else:
              print("\nOpción inválida. Por favor, elija una opción válida.\n")

      except sr.UnknownValueError:
          print("\nNo se pudo entender la opción.")
      except sr.RequestError:
          print("\nError al conectar con el servicio de reconocimiento de voz.")


if __name__ == "__main__":
    main()