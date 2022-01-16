# Note: The maximum recording time is 20 minutes. This can be adjusted, it was just
# an arbitrary value chosen. After recording is done, it is cropped to the length
# of the recording session (expressed in seconds * sample rate), and saved to disk
# with the same name of file printed in the console.

# what we will want to do is begin the recording as soon as the "recording.html" page
# is loaded, and then stop it when the "Generate Composition" button is clicked.

import sounddevice as sd
import time
from scipy.io.wavfile import write

def startRecording(fs, seconds):
    start_time = time.time()
    myRecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    
    print()
    stop = input("To Stop Recording Press 's': ")

    if stop.lower() == 's':
        stopRecording()
        stop_time = time.time()

    recording_time = stop_time - start_time

    myRecording = myRecording[0 : int(recording_time * fs)]

    name = 'my_recording_' + str(int(stop_time)) + '.wav'

    write(name, fs, myRecording)  # Save as WAV file

    print()
    print('Saved to file: ' + name)

def stopRecording():
    myRecording = sd.stop()

def main():
    fs = 44100  # Sample rate
    seconds = 1200  # Duration of recording

    print()
    start = input("To Start Recording Press 's': ")

    if start.lower() == 's':
        print()
        startRecording(fs, seconds)

main()

