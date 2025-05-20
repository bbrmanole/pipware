from pyaudio import *
from wave import *
import threading

import random



class AudioPlayer:
    audioPlayer = PyAudio() 
    chunk = 1024
    station1 = ["assets\\Radio\CyberRadio\\I Really Want to Stay at Your House.wav",
                "assets\\Radio\CyberRadio\\Let You Down.wav",
                "assets\\Radio\CyberRadio\\Major Crimes.wav",
                "assets\\Radio\CyberRadio\\Never Fade Away (SAMURAI Cover).wav",
                "assets\\Radio\CyberRadio\\Nightcall.wav",
                "assets\\Radio\CyberRadio\\Phantom Liberty.wav",
                "assets\\Radio\CyberRadio\\Roller Mobster.wav",
                "assets\\Radio\CyberRadio\\Turbo Killer.wav"]
    

    def ToggleRadio(self):    
        currentFile = Wave_read("assets\\Radio\\menu\\menuMusic.wav")   
        mmThread = threading.Thread(target=self.playmmAudio,args=(self,self.audioPlayer,currentFile),name="AudioPlayer")
        mmThread.start()



    def StartStation(self):
        musicThread = threading.Thread(target=self.playRadioStation,args=(self,self.audioPlayer,self.station1))
        musicThread.start()


    
    def playmmAudio(self,audioPlayer,currentFile):
        stream = audioPlayer.open(format= audioPlayer.get_format_from_width(currentFile.getsampwidth()),
                        channels= currentFile.getnchannels(),
                        rate=currentFile.getframerate(),
                        output=True)
        data = currentFile.readframes(self.chunk)
        while data:
            stream.write(data)
            data = currentFile.readframes(self.chunk)
        
        stream.stop_stream()
        stream.close()



    def playRadioStation(self,audioPlayer, radStation):        
        for songs in radStation:
            songToPlay = Wave_read(songs)
            stream = audioPlayer.open(format= audioPlayer.get_format_from_width(songToPlay.getsampwidth()),
                                      channels= songToPlay.getnchannels(),
                                      rate=songToPlay.getframerate(),
                                      output=True)
            data = songToPlay.readframes(self.chunk)
            while data:
                stream.write(data)
                data = songToPlay.readframes(self.chunk)
        stream.stop_stream()
        stream.close()

    


    
    
   

    

    

