from flask import Flask
import os

app = Flask(__name__)

@app.route('/video-ended', methods=['GET'])
def video_ended():
    # Shutdown the PC
    os.system('shutdown /s /t 1')
    return 'Shutting down...', 200

if __name__ == '__main__':
    app.run(port=5000)
