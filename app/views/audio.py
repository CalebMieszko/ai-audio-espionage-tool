from flask import Blueprint, render_template, request, redirect, url_for
import os

audio_blueprint = Blueprint(
    'audio', __name__, template_folder='../templates', static_folder='../static')


@audio_blueprint.route('/')
def index():
    return render_template('index.html', title="Voice Clone Detector", header_text="Welcome to the Voice Clone Detector | So Say We All", audio_files=os.listdir('app/static/audio/'), current_year=2023)


@audio_blueprint.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio_file' in request.files:
        audio_file = request.files['audio_file']
        audio_file.save(os.path.join('app/static/audio', audio_file.filename))
    return redirect(url_for('audio.index'))


@audio_blueprint.route('/detect_voice_clone', methods=['POST'])
def detect_voice_clone():
    # Implement voice clone detection logic here
    return redirect(url_for('audio.index'))
