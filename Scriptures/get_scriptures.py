import requests
import json
import argparse
import pyaudio
import wave
import speech_recognition as sr

parser = argparse.ArgumentParser(description="Get bible verse for the preacher")
parser.add_argument('book', help="Enter Bible book abbreviated or full name")
parser.add_argument('chapter', type=str, help="Enter Bible chapter")
parser.add_argument('verse', type=str, help="Enter verse or verses")

args = parser.parse_args()
book = args.book
chapter = args.chapter
verse = args.verse 


def main():
    # chunk = 1024  # Record in chunks of 1024 samples
    # sample_format = pyaudio.paInt16  # 16 bits per sample
    # channels = 2
    # fs = 44100  # Record at 44100 samples per second
    # seconds = 3
    # filename = "output.wav"
    # p = pyaudio.PyAudio()

    # print('Recording...')

    # stream = p.open(format=sample_format,
    #                 channels=channels,
    #                 rate=fs,
    #                 frames_per_buffer=chunk,
    #                 input=True)
    
    # frames = []  # Initialize array to store frames

    # # Store data in chunks for 3 seconds
    # for i in range(0, int(fs / chunk * seconds)):
    #     data = stream.read(chunk)
    #     frames.append(data)

    # # Stop and close the stream 
    # stream.stop_stream()
    # stream.close()
    # # Terminate the PortAudio interface
    # p.terminate()

    # print('Finished recording')

    # # Save the recorded data as a WAV file
    # wf = wave.open(filename, 'wb')
    # wf.setnchannels(channels)
    # wf.setsampwidth(p.get_sample_size(sample_format))
    # wf.setframerate(fs)
    # wf.writeframes(b''.join(frames))
    # wf.close()

    # r = sr.Recognizer()
    # with sr.AudioFile('output.wav') as source:
    #     audio = r.record(source)
    #     print('You said {}'.format(r.recognize_google(audio)))

    url = 'https://bible-api.com/'
    bible_book = book
    bible_chapter= chapter
    bible_scripture = verse

    full_url = f'{url}{bible_book}{bible_chapter}:{bible_scripture}?translation=kjv'

    r = requests.get(full_url)

    response_dict = json.loads(r.text)
    print(response_dict["text"])




    """
    Purposes for Regeneration:
    That we would be adopted into God's Family - Romans 8:15
    That we would receive a new nature - Colassians 3:10
    That we would enter the kingdom of God -
    That we would have confidences    - 1Peter 1:3-4 
    That we would be joint airs of Christ -Romans 8:15
    That we may be James 1:18
    That God's Spirit will be able to produce in and through our lives. Titus 3:2,3,6 Ephesians 2:10 1 Corithians 6:9-11

    Evidence of Regeneration:
    Lifestyle characterized by righteousness



"""
if __name__ =='__main__':
    main()