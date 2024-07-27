from flask import Flask, jsonify, send_file, request, abort
from io import BytesIO
import os
from mutagen import File
from datetime import datetime

app = Flask(__name__)

directory = './memos'


def get_memos() -> list:
    files = []
    for filename in os.listdir(directory):
        if filename.endswith('.m4a'):
            filepath = os.path.join(directory, filename)
            file_info = {
                'filename': filename,
                'creation_time': os.path.getctime(filepath),
                'metadata': None
            }
            # Read metadata using mutagen
            try:
                audio_file = File(filepath)
                file_info['metadata'] = str(audio_file.info)  # Convert to string for JSON serialization
            except Exception as e:
                file_info['metadata'] = str(e)
            files.append(file_info)
    # Sort files by creation time
    files.sort(key=lambda x: x['creation_time'])
    # Return the specified range of files
    return files


@app.route('/memos', methods=['GET'])
def list_memos():
    memos = get_memos()
    response = [{
        'filename': memo['filename'],
        'creation_time': datetime.fromtimestamp(memo['creation_time']).isoformat(),
        'metadata': memo['metadata']
    } for memo in memos]
    return jsonify(response)


@app.route('/memo/<filename>', methods=['GET'])
def get_memo(filename):
    memos = get_memos()
    for memo in memos:
        if memo['filename'] == filename:
            filepath = os.path.join(directory, filename)
            return send_file(filepath,
                             mimetype='audio/mp4',
                             as_attachment=True,
                             download_name=filename)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
