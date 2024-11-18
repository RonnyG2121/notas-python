import google.generativeai as genai
import os
import PIL.Image

try:
    ruta = os.path.join(os.getcwd(), "ejercicios", "gemini")
    if os.path.exists(ruta):
        os.chdir(ruta)
except Exception as e:
    print(e)

mi_api = os.environ["GEMINI_API"]

genai.configure(api_key=mi_api)
model = genai.GenerativeModel("gemini-1.5-flash")

image = PIL.Image.open("arbol_de_mangos_noble-academy.jpeg")

response = model.generate_content(
    ["Descríbeme esta imagen en español", image], stream=True)
response.resolve()
print(response.text)
