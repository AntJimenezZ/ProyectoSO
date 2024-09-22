from flask import Flask, Response, request, abort, jsonify
from flask_cors import CORS  # Importar CORS
import os

app = Flask(__name__)
CORS(app)  # Configurar CORS

def get_range(request):
    range_header = request.headers.get('Range', None)
    if range_header is None:
        return None, None

    # Parse 'bytes=start-end'
    range_value = range_header.strip().split('=')[-1]
    range_start, range_end = range_value.split('-')

    try:
        start = int(range_start) if range_start else 0
        end = int(range_end) if range_end else None
    except ValueError:
        return None, None

    return start, end

def stream_file_with_range(file_path):
    file_size = os.path.getsize(file_path)
    start, end = get_range(request)

    if start is None:
        # Return the entire file if no range is provided
        return Response(open(file_path, 'rb'), mimetype="audio/mpeg", headers={
            "Content-Length": str(file_size)
        })

    # Set end to file size if it's not provided
    if end is None or end >= file_size:
        end = file_size - 1

    # If requested range is invalid
    if start >= file_size or start > end:
        abort(416, "Requested Range Not Satisfiable")

    chunk_size = end - start + 1
    with open(file_path, "rb") as f:
        f.seek(start)
        chunk = f.read(chunk_size)

    response = Response(chunk, status=206, mimetype="audio/mpeg", headers={
        "Content-Range": f"bytes {start}-{end}/{file_size}",
        "Accept-Ranges": "bytes",
        "Content-Length": str(chunk_size),
    })

    return response

@app.route('/sendVideo')
def song():
    video_name = request.args.get('name')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'videos', f"{video_name}")
    if not os.path.exists(file_path):
        abort(404, "File not found")
    else:
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
    for file in os.listdir('./videos'):
        if file.endswith('.mp3'):
            files.append(file)
    return files

if __name__ == '__main__':
    app.run(debug=True, port=8080)