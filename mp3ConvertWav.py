#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importingm all liabraries that we need

import os
from pydub import AudioSegment
import glob


# In[ ]:


# creating class

class con:
    def convert (data_file):
        
        # importing data
        path = (data_file)

        #Change working directory
        os.chdir(path)

        # creatig list
        audio_files = os.listdir()

        for file in audio_files:
            #spliting the file into the name and the extension
            wav = os.path.splitext(file)[0]+ '.wav'
            mp3_sound = AudioSegment.from_mp3(file)

            #rename them using the old name + ".wav"
            mp3_sound.export(wav, format="wav")
        print ("mp3 converted into wav");

    def cut (data_file):
        
        # importing data
        path = (data_file)

        #Change working directory
        os.chdir(path)

        # creatig list
        audio_files = os.listdir()

        for file in audio_files:
            #spliting the file into the name and the extension
            wav = os.path.splitext(file)[0] + '.wav'
            mp3_sound = AudioSegment.from_mp3(file)
            #rename them using the old name + ".wav"
            mp3_sound.export(wav, format="wav")
            os.remove(file)
            print(wav)
        print ("The files successfully converted and previous files deleted!")
        


# In[ ]:





# In[ ]:




