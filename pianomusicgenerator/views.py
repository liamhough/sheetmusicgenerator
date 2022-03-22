import sys        
sys.path.append('C:/wamp64/www/sheetmusicgenerator/RSE')       
import transcribe   
 
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import sounddevice as sd
import time
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 1200  # Duration of recording

start_time = 0
stop_time = 0
counter = 0
my_recording = 0
is_recording = False

def index(request):
    template = loader.get_template('home.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


def composition(request):
    template = loader.get_template('composition.html')
    name = request.GET['name']
    context = {
        "name": name
    }
    from pprint import pprint
    import os
    from urllib.request import urlopen
    import urllib.error

    import flat_api
    from flat_api.rest import ApiException
    import base64

    midiFileName = name + ".mid"

    with open(midiFileName, "rb") as f:
        midiFile = base64.b64encode(f.read()).decode("utf-8")

    configuration = flat_api.Configuration()
    configuration.access_token = "77597d6bf10b76ca0a641ede8e14c053dc7eb7f37b9fc15c31db5bca7feec0fdbb56e2b8a116c984912a875811843ea25fe12fde655fef3c289057c6f792b715"
    flat_api_client = flat_api.ApiClient(configuration)

    new_score = flat_api.ScoreCreation(
        title= name + " Import",
        privacy= 'public',
        data = midiFile,
        data_encoding= 'base64'
    )

    response = flat_api.ScoreApi(flat_api_client).create_score(new_score)

    print(response)

    return HttpResponse(template.render(context, request))


def recording(request):
    global counter
    global is_recording
    global my_recording

    template = loader.get_template('recording.html')
    name = request.GET['name']
    context = {
        "name": name
    }

    counterIncrement()

    if counter % 2 == 1:
        is_recording = True
        setStartTime()
        my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

    if counter % 2 == 0:
        is_recording = False
        setStopTime()
        write_to_file = True

    while is_recording == True:
        continue

    if write_to_file == True:
        recording_time = stop_time - start_time
        my_recording = my_recording[0 : int(recording_time * fs)]
        wave_name = name + '.wav'
        write(wave_name, fs, my_recording)  # Save as WAV file
        counter = 0
        my_recording = 0

        wav_path = 'C:/wamp64/www/sheetmusicgenerator/' + wave_name

        print("jkfevnboqjefnvijqbeifvbqwonvnoenfvoinwefvnoiqefnvoiqenfovnqefovnqeoffvnoiqenovinqeoifrfvnoqerniern")
        transcribe.main(wav_path)

    return HttpResponse(template.render(context, request)) 

def setStartTime():
    global start_time
    start_time = time.time()

def setStopTime():
    global stop_time
    stop_time = time.time()

def counterIncrement():
    global counter
    counter = counter + 1