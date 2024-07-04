from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from flask_cors import CORS
from models import *
import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES
from collections import Counter
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transcription.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

r = sr.Recognizer()

translator = Translator()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return 'Welcome to Speech Recognition and Translation App!'


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'error': 'Username, password, and email are required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.password = password
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'error': 'Invalid username or password'}), 401


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/record', methods=['GET', 'POST'])
@login_required
def record_and_translate():
    user_id = current_user.id

    try:
        with sr.Microphone() as source2:
            print("Silence Please, Calibrating, Wait for 1 second ...")
            r.adjust_for_ambient_noise(source2, duration=1)
            SpeakTest("Now Speak....")

            audio = r.listen(source2)
            Mytext = r.recognize_google(audio)
            print("Recognized : ", Mytext)

        detected_lang = translator.detect(Mytext)
        lang_code = detected_lang.lang
        print(
            f"Detected Language: {LANGUAGES.get(lang_code, 'Unknown')} (Confidence: {detected_lang.confidence})")

        translation = translator.translate(Mytext, src=lang_code, dest='en')
        translated_text = translation.text
        print(
            f"Translated ({LANGUAGES[lang_code]} to English): {translated_text}")

        transcription = Transcription(
            text=Mytext, language=lang_code, user_id=user_id)
        db.session.add(transcription)
        db.session.commit()
        print("Transcription stored successfully.")

        SpeakTest(
            f"You said: {Mytext}. Translated to English: {translated_text}")
        return jsonify({"recognized": Mytext, "translated": translated_text})

    except sr.UnknownValueError:
        SpeakTest("I couldn't understand what you said. Please speak again.")
        return jsonify({"error": "Could not understand audio"}), 400

    except sr.RequestError as e:
        SpeakTest(
            "Speech recognition service is unavailable. Please try again later.")
        return jsonify({"error": "Speech recognition service unavailable"}), 500

    except Exception as e:
        SpeakTest("An error occurred. Please speak again.")
        return jsonify({"error": str(e)}), 500


@app.route('/word-frequencies', methods=['GET'])
@login_required
def word_frequencies():
    user_id = current_user.id

    user_transcriptions = Transcription.query.filter_by(user_id=user_id).all()
    all_transcriptions = Transcription.query.all()

    user_words = ' '.join([t.text for t in user_transcriptions]).split()
    all_words = ' '.join([t.text for t in all_transcriptions]).split()

    user_word_count = Counter(user_words)
    all_word_count = Counter(all_words)

    user_word_freq = {word: count for word, count in user_word_count.items()}
    all_word_freq = {word: count for word, count in all_word_count.items()}

    current_username = current_user.username

    return jsonify({
        "user_word_freq": user_word_freq,
        "all_word_freq": all_word_freq,
        "currentUser": current_username
    })


@app.route('/top-3-phrases', methods=['GET'])
@login_required
def top_3_phrases():
    user_id = current_user.id

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    user_transcriptions = Transcription.query.filter_by(user_id=user_id).all()

    user_phrases = [t.text for t in user_transcriptions]

    phrase_counts = Counter(user_phrases)

    top_3_phrases = phrase_counts.most_common(3)

    return jsonify({"top_3_phrases": top_3_phrases})


def SpeakTest(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
