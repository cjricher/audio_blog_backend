from flask import Flask, jsonify, send_file, request, abort
from io import BytesIO
import os
from mutagen import File
from mutagen.mp4 import MP4
from datetime import datetime

app = Flask(__name__)

directory = './memos'


def get_memos() -> list:
    files = []
    for filename in os.listdir(directory):
        if filename.endswith('.m4a'):
            filepath = os.path.join(directory, filename)
            creation_time = os.path.getctime(filepath)
            modification_time = os.path.getmtime(filepath)
            metadata = None
            length = None
            try:
                audio_file = MP4(filepath)
                metadata = {
                    'bitrate': audio_file.info.bitrate,
                    'channels': audio_file.info.channels,
                    'sample_rate': audio_file.info.sample_rate,
                    'length': audio_file.info.length
                }
                length = audio_file.info.length
            except Exception as e:
                metadata = {'error': str(e)}

            file_info = {
                'filename': filename,
                'created': creation_time,
                'modified': modification_time,
                'metadata': metadata,
                'length': length
            }
            files.append(file_info)

    # Sort files by creation time
    files.sort(key=lambda x: x['created'])
    return files


@app.route('/memos', methods=['GET'])
def list_memos():
    memos = get_memos()
    response = [{
        'filename': memo['filename'],
        'created': datetime.fromtimestamp(memo['created']).isoformat(),
        'modified': datetime.fromtimestamp(memo['modified']).isoformat(),
        'metadata': memo['metadata'],
        'length': memo['length']
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
