from flask import Flask, Response, request, abort
from flask_cors import CORS  # Importar CORS
import os

app = Flask(__name__)
CORS(app)  # Configurar CORS

def get_range(request):
    # Implementación de la función
    pass

def stream_file_with_range(file_path):
    # Implementación de la función
    pass

@app.route('/sendVideo')
def song():
    file_path = "./videos/Jhay Cortez, Anuel AA, J. Balvin - Medusa (Official Video).mp4"
    return stream_file_with_range(file_path)

@app.route('/allVideos')
def get_all_files():
    files = []
    for file in os.listdir('./videos'):
        if file.endswith('.mp4'):
            files.append(file)
    return files

@app.route('/allSongs')
def get_all_songs():
    files = []
    for file in os.listdir('./songs'):
        if file.endswith('.mp3'):
            files.append(file)
    return files

if __name__ == '__main__':
    app.run(debug=True, port=8080)