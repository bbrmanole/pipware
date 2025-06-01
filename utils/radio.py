#from pyaudio import *
#from wave import *
import threading
#import random
import pygame
import time



class AudioPlayer:
    '''
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

    def pauseMusic(self):
        self.audioPlayer.Stream.stop_stream(self)
    
    def resumeMusic(self):
        self.audioPlayer.Stream.start_stream(self)
        '''
    
class Audio2:
    soundPlayer = pygame.mixer
    station1 = ["assets\\Radio\CyberRadio\\I Really Want to Stay at Your House.wav",
                "assets\\Radio\CyberRadio\\Let You Down.wav",
                "assets\\Radio\CyberRadio\\Major Crimes.wav",
                "assets\\Radio\CyberRadio\\Never Fade Away (SAMURAI Cover).wav",
                "assets\\Radio\CyberRadio\\Nightcall.wav",
                "assets\\Radio\CyberRadio\\Phantom Liberty.wav",
                "assets\\Radio\CyberRadio\\Roller Mobster.wav",
                "assets\\Radio\CyberRadio\\Turbo Killer.wav"]
    station2 = ["assets\\Radio\\Eighties\\Paranoid (2009 Remaster).wav",
                "assets\\Radio\\Eighties\\Highway to Hell.wav",
                "assets\\Radio\\Eighties\\Hold the Line.wav",
                "assets\\Radio\\Eighties\\In The Army Now.wav",
                "assets\\Radio\\Eighties\\Money For Nothing (Remastered 1996).wav",
                "assets\\Radio\\Eighties\\Sultans Of Swing.wav",
                "assets\\Radio\\Eighties\\The Road to Hell Part 2.wav",
                "assets\\Radio\\Eighties\\You Give Love A Bad Name.wav"]
    
    stationList = [station2,station1]
    
    currentStation = 0
    currentSong = 0

    def initSystem(self):
        self.soundPlayer.init()
        self.soundPlayer.set_num_channels(1)
        sound = self.soundPlayer.Sound("assets\\Radio\\menu\\menuMusic.wav")
        sound.set_volume(0.2)
        sound.play()

    def pauseSong(self):
        sound = self.soundPlayer
        sound.pause()

    def resumeSong(self):
        sound = self.soundPlayer
        sound.unpause()

    def startListening(self):
        sound = self.soundPlayer
        sound.fadeout(3000)
        soundThread = threading.Thread(target=self.queueSystem,args=(self,))
        soundThread.start()
        
    
    def queueSystem(self):       
        playlist = self.stationList
        busychk = self.soundPlayer  
        station = self.currentStation
        song = self.currentSong
        while True:
            if busychk.get_busy() == False:
                if song < len(playlist[station]):
                    player = busychk.Sound(playlist[station][song])
                    player.play()
                    song +=1
                else:
                    station += 1
                    song +=1
             
  
                    
           
            
        
            
                
                
