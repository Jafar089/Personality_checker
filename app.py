from flask import Flask, render_template, request
import pyttsx3
import speech_recognition as sr
import time

app = Flask(__name__)

# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text) 
    engine.runAndWait()

listener = sr.Recognizer()

@app.route('/api/index')
def index():
    return render_template('index.html')  # A simple form for input

@app.route('/api/process', methods=['POST'])
def process():
    name = request.form['name']
    a = request.form['extrovert_introvert']
    b = request.form['sensing_intuitive']
    c = request.form['thinking_feeling']
    d = request.form['judging_perceiving']
    
    personality_type = a + b + c + d
    description = get_description(personality_type)
    talk(description)
    return render_template('result.html', name=name, personality_type=personality_type, description=description)

def get_description(ptype):
    descriptions = {
        'istj': 'You are responsible, sincere, analytical, reserved, realistic, systematic...',
        'isfj': 'You are Warm, considerate, gentle, responsible, pragmatic, thorough...',
        'istp': 'You are Action-oriented, logical, analytical, spontaneous, reserved, independent.Enjoy adventure, skilled at understanding how machanical things work.',
        'isfp': 'You are Gentle, sensitive, nurturing, helpful, flexible, realistic. Seek to create a personal environment that is both beautiful and practical.',
        'estp': 'You are Outgoing, realistic, action-oriented,curious,verstile,spontaneous.Pragmatic problem solvers and skillful negotiators.',
        'esfp': 'You are Playful, enthusiastic, friendly, spontaneous, tactful, flexible. Have strong common sense, enjoy helping people in tangible ways.',
        'esfj': 'You are Friendly, outgoing, reliable, conscientious, organized, practical. Seek to be helpful and please others , enjoy being active and productive.',
        'estj': 'You are Efficient,outgoing,analytical,syestematic,dependable,realistic.Like to run the show and get things done in an orderly fashion.',
        'infj': 'You are Idealistic, organized, insighful, dependable, compassionate, gentle. Seek harmony and cooperation, enjoy intellectual stimulation.',
        'intj': 'You are Innovative , independent, strategic, logical, reserved, insightful. Driven by their own orignal ideas to achieve improvements.',
        'infp': 'You are Sensitive, creative, idealistic, perceptive, caring, loyal. Value inner  harmony and personal growth ,focus on dreams and possibilities.',
        'intp': 'You are Intellectual,logical,precise,reserved,flexible,imaginative.Original thinkers who enjoy speculation and creative problem solving.',
        'enfp': 'You are Enthusiastic, creative , spontaneous, optimistic, supportive playful. Values inspiration, enjoy starting new projects see potential in others.',
        'entp': 'You are Intentive, enthusiastic, strategic, enterprisng, inquisitive, versatile. Enjoy new ideas and challenges , value inspiration.',
        'enfj': 'You are Caring, enthusiastic, idealistic, organized, diplomatic, responsible. Skilled communicators who value connection with people.',
        'entj': 'you are Strategical, logical, efficient, outgoing, ambitious, independent. Effective organizers of people and long-range planners.'
        # Add all the other personality types here
    }
    return descriptions.get(ptype.lower(), "No description available for this type.")

if __name__ == '__main__':
    app.run(debug=True)
