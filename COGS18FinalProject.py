#!/usr/bin/env python
# coding: utf-8

# # Project Description:
# 
#                                                         
# Goal of Project:     
# 
# The goal of this project is to create an ipod-like object with various methods that will analyze a comma-separated value file or data frame containing the top 100 songs on spotify in the year 2018. Not only does the data frame contain the artist and name of the songs, but it also introduces various traits like danceability, energy,key, speechiness, liveness, tempo and valence to further give them a unique rating for each trait. The methods created in this project would then aim to create a distinct playlist based on the specific rating constraints being requested. For instance, calling a specific method when looking for songs with a specific tempo or danceability rate would then give you a list of songs that apply to those given limit values. 
# 
#     
# Implementation of Project:
# 
# Creating this project had various challenges along the way; yet by being patient and googling most of my concerns and errors I was able to eventually accomplish what I actually wanted to do. First I had to learn about the functions and methods displayed in the pandas module in order to analyze a data frame and further work with it. Learning pandas was difficult in the beginning as much of the functions were hard to find, on the other hand, most of the task I wanted to do required if statements while pandas had its own way of processing those if conditions. Once I managed to learn a few built-in functions in pandas, I began to clean out the data frame and get rid of all the columns I did not want to work with. Deleting the columns was pretty easy as I just had to call the “drop” function on that specific column; further getting rid of the column and all its data. After deleting all the columns I did not want to work with, I had to find a way to then make my methods easier to execute. By calling the “round” function from pandas on my columns I was able to round all the values/ratings stored in each column; making it easier for the user to find songs that contained the same rate for danceability and other traits. Once I was done editing the columns, all I had to do was find a way to loop through them and find any songs with that expected value for that given trait.
#            

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


songs = pd.read_csv('top2018.csv')

# Dropping ID,mode,acousticness,duration_ms,instrumentalness, and time_signature columns:

songs = songs.drop(columns ='id').drop(columns='mode').drop(columns='acousticness').drop(columns='duration_ms').drop(columns='instrumentalness').drop(columns='time_signature').drop(columns='loudness')

# Data types within each column of the dataFrame:

songs.dtypes


# In[3]:


# Rounding/Truncating variables from few columns for better manipulation and control

songs['danceability'] = songs['danceability'].round(decimals = 1)

songs['energy'] = songs['energy'].round(decimals = 1)

songs['speechiness'] = songs['speechiness'].round(decimals = 1)

songs['liveness'] = songs['liveness'].round(decimals = 1)

songs['tempo'] = songs['tempo'].round(decimals = 1)

songs['valence'] = songs['valence'].round(decimals = 1)

print('Danceability, energy, speechiness, liveness, tempo and valence values are now being truncated..')


# In[4]:


# Refer back to when testing
songs


# In[25]:


class Ipod():
    
    
    # Artist
    
    def list_by_artist(self,artist):  
        """" Loops through artists column to list all songs that match input string.
        
        Parameters
        -----------
        artist: string
            artist name in string form to search for in artists column, songs
        Returns
        -----------
        artist_list: list
            list of songs that match input name
        """
        
        print('Now Sorting Playlist By Artist...')
        
        artist_list = []                                                   # Creates empty list which will append output songs
        artist_list.append(songs.loc[songs['artists'] == artist])          # If input artist in artists col, artist_list appends song                                                                        
        
        return artist_list                                                # Return arist_list 
    
    
    # Song
    
    def play_song(self,name_of_song):
        """" Loops through name column to list any songs that match the given name.
        
        Parameters
        -----------
        name_of_song : string
            name of song in string form to search for in name column, songs
        Returns
        -----------
        specific_song: list
            list that appends any matches that correlate with the input/song name
        """
        
        print('Now Playing...')
        
        specific_song = []                                                     # Creates empty list that will append output
        specific_song.append(songs.loc[songs['name'] == name_of_song])         # If name_of song matches in name col, list appends
        
        return specific_song                                                   # Return specific_song with output song in it 
    
    
    # Danceability of song
    
    def lower_danceability(self,rating):
        """" Loops through danceability column to find all songs that have a
            danceability rating below the rating input to further append them to a new list
        
        Parameters
        -----------
        rating: int/float value
            integer that lowers the scope value to shorten the search and output
            list by a given # constraint
        
        Returns
        -----------
        by_lower_danceability: list
            list that contains all songs that have a danceability rating lower than the given value
        """""
        
        print('Now Sorting Playlist By Lower Danceability Values...')
        
        by_lower_danceability = []                                     # Creates empty list which will append songs
        danceabilityy = songs[songs.danceability < rating]             # danceabilityy == all songs w/ danceability val < rating
        by_lower_danceability.append(danceabilityy)                    # by_lower_danceability appends songs from danceabilityy
        
        return by_lower_danceability                                   # Return by_lower_danceability                            
    
    
    def same_danceability(self,rating):
        """ Loops through danceability column in songs and creates a list that appends 
        all songs with a danceability rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with a danceability
           rating thats equal to the given value
           
        Returns
        -----------
        by_equal_danceability: list
            list that appends all songs that have a danceability rating thats equal to the given value
        """
        
        print('Now Sorting Playlist By Similar Danceability Values...')
        
        by_equal_danceability = []                                       # Creates empty list called by_equal_danceability
        danceabilityy = songs[songs.danceability == rating]              # danceabilityy == any songs in the danceability column with a value == rating
        by_equal_danceability.append(danceabilityy)                      # by_equal_danceability appends danceabilityy
        
        return by_equal_danceability                                     # Returns by_equal_danceability
    
    
    def higher_danceability(self,rating):
        """ Loops through danceability column in songs and creates a list that appends 
        all songs with a danceability rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with a
           danceability rating thats higher than the given value
           
        Returns
        -----------
        by_higher_danceability: list
            list that appends all songs that have a danceability rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Danceability Values...')
        
        by_higher_danceability = []                                     # Empty list called by_higher_danceability created
        danceabilityy = songs[songs.danceability > rating]              # danceabilityy == all songs in danceability column w/ danceability value > rating
        by_higher_danceability.append(danceabilityy)                    # by_higher_danceability appends danceabilityy
        
        return by_higher_danceability                                   # Returns by_higher_danceability
    

    ## All methods below consist of the same structure and work the same as the ones above, just different trait
    
    # Overall energy or 'hype' of song
    
    def lower_energy(self,rating):
        """ Loops through energy column in songs and creates a list that appends 
        all songs with an energy rating lower than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song thats energy rating
           is lower than the given value
           
        Returns
        -----------
        by_lower_energy: list
            list that appends all songs that have an energy value thats lower than the given rating
        """
        
        print('Now Sorting Playlist By Lower Energy Values...')
        
        by_lower_energy = []
        turnt_down = songs[songs.energy < rating]
        by_lower_energy.append(turnt_down)
        
        return by_lower_energy
    
    
    def same_energy(self,rating):
        """ Loops through energy column in songs and creates a list that appends 
        all songs with an energy rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song thats
           energy rating is equal to the given value
           
        Returns
        -----------
        by_equal_energy: list
            list that appends all songs that have an energy rating thats equal to the given value
        """
         
        print('Now Sorting Playlist By Similar Energy Values...')
        
        by_equal_energy = []                            
        how_turnt = songs[songs.energy == rating]       
        by_equal_energy.append(how_turnt)              
        
        return by_equal_energy                          
    
    
    def more_energy(self,rating):
        """ Loops through energy column in songs and creates a list that appends 
        all songs with an energy rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           an energy rating thats higher than the given value
           
        Returns
        -----------
        by_higher_energy: list
            list that appends all songs that have an energy rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Energy Values...')
        
        by_higher_energy = []
        turnt = songs[songs.energy > rating]
        by_higher_energy.append(turnt)
        
        return by_higher_energy
    
    
    # Average/consistent key value of song
    
    def lower_key(self,rating):
        """ Loops through key column in songs and creates a list that appends 
        all songs with a key rating lower than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a key rating thats lower than the given value
           
        Returns
        -----------
        low_key: list
            list that appends all songs that have a key rating thats lower than the given value
        """
        
        print('Now Sorting Playlist By Lower Key Values...')
        
        low_key = []
        keys = songs[songs.key < rating]
        low_key.append(keys)
        
        return low_key
    
    
    def same_key(self,rating):
        """ Loops through key column in songs and creates a list that appends 
        all songs with a key rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a key rating thats equal to the given value
           
        Returns
        -----------
        equal_key: list
            list that appends all songs that have a key rating thats equal to the given value
        """
        
        print('Now Sorting Playlist By Similar Key Values...')
        
        equal_key = []
        keys = songs[songs.key == rating]
        equal_key.append(keys)
        
        return equal_key
    
    
    def higher_key(self,rating):
        """ Loops through key column in songs and creates a list that appends 
        all songs with a key rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a key rating thats higher than the given value
           
        Returns
        -----------
        high_key: list
            list that appends all songs that have a key rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Key Values...')
        high_key = []
        keys = songs[songs.key > rating]
        high_key.append(keys)
        return high_key
    
    # Overall speechiness of song
    
    def lower_speechiness(self,rating):
        """ Loops through speechiness column in songs and creates a list that appends 
        all songs with a speech rating lower than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a speech rating thats lower than the given value
           
        Returns
        -----------
        speechiness: list
            list that appends all songs that have a speech rating thats lower than the given value
        """
        
        print('Now Sorting Playlist By Lower Speech Values...')
        
        speechiness = []
        speech = songs[songs.speechiness < rating]
        speechiness.append(speech)
        
        return speechiness
    
    
    def same_speechiness(self,rating):
        """ Loops through speechiness column in songs and creates a list that appends 
        all songs with a speech rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a speech rating thats equal to the given value
           
        Returns
        -----------
        speechiness: list
            list that appends all songs that have a speech rating thats equal to the given value
        """
        
        print('Now Sorting Playlist By Similar Speech Values...')
        
        speechiness = []
        speech = songs[songs.speechiness == rating]
        speechiness.append(speech)
        
        return speechiness
    
    
    def higher_speechiness(self,rating):
        """ Loops through speechiness column in songs and creates a list that appends 
        all songs with a speech rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a speech rating thats higher than the given value
           
        Returns
        -----------
        speechiness: list
            list that appends all songs that have a speech rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Speech Values...')
        
        speechiness = []
        speech = songs[songs.speechiness > rating]
        speechiness.append(speech)
        
        return speechiness
    
    
    # Overall liveliness of song
    
    def lower_liveness(self,rating):
        """ Loops through liveness column in songs and creates a list that appends 
        all songs with a liveness rating lower than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a liveness rating thats lower than the given value
           
        Returns
        -----------
        liveness: list
            list that appends all songs that have a liveness rating thats lower than the given value
        """
        
        print('Now Sorting Playlist By Lower Liveliness Values...')
        
        liveliness = []
        how_live = songs[songs.liveness < rating]
        liveliness.append(how_live)
        
        return liveliness
    
    
    def same_liveness(self,rating):
        """ Loops through liveness column in songs and creates a list that appends 
        all songs with a liveness rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a liveness rating thats equal to the given value
           
        Returns
        -----------
        liveness: list
            list that appends all songs that have a liveness rating thats equal to the given value
        """
        
        print('Now Sorting Playlist By Similar Liveliness Values...')
        
        liveliness = []
        how_live = songs[songs.liveness == rating]
        liveliness.append(how_live)
        
        return liveliness
    
    
    def higher_liveness(self,rating):
        """ Loops through liveness column in songs and creates a list that appends 
        all songs with a liveness rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a liveness rating thats higher than the given value
           
        Returns
        -----------
        liveness: list
            list that appends all songs that have a liveness rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Liveliness Values...')
        liveliness = []
        how_live = songs[songs.liveness > rating]
        liveliness.append(how_live)
        return liveliness
    
    
    # Overall valence of song
    
    def lower_valence(self,rating):
        """ Loops through valence column in songs and creates a list that appends 
        all songs with a valence rating lower than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a valence rating thats lower than the given value
           
        Returns
        -----------
        valence: list
            list that appends all songs that have a valence rating thats lower than the given value
        """
        
        print('Now Sorting Playlist By Lower Valence Values...')
        
        valence = []
        vibes = songs[songs.valence < rating]
        valence.append(vibes)
        
        return valence
    
    
    def same_valence(self,rating):
        """ Loops through valence column in songs and creates a list that appends 
        all songs with a valence rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a valence rating thats equal to the given value
           
        Returns
        -----------
        valence: list
            list that appends all songs that have a valence rating thats equal to the given value
        """
        
        print('Now Sorting Playlist By Similar Valence Values...')
        
        valence = []
        vibes = songs[songs.valence == rating]
        valence.append(vibes)
        return valence
    
    
    def higher_valence(self,rating):
        """ Loops through valence column in songs and creates a list that appends 
        all songs with a valence rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a valence rating thats higher than the given value
           
        Returns
        -----------
        valence: list
            list that appends all songs that have a valence rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Valence Values...')
        
        valence = []
        vibes = songs[songs.valence > rating]
        valence.append(vibes)
        
        return valence
    
    # Overall tempo of song
    
    def lower_tempo(self,rating):
        """ Loops through tempo column in songs and creates a list that appends 
        all songs with a tempo rating lower than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a tempo rating thats lower than the given value
           
        Returns
        -----------
        tempo: list
            list that appends all songs that have a tempo rating thats lower than the given value
        """
        
        print('Now Sorting Playlist By Lower Tempo Values...')
        
        tempo = []
        temps = songs[songs.tempo < rating]
        tempo.append(temps)
        
        return tempo
    
    
    def same_tempo(self,rating):
        """ Loops through tempo column in songs and creates a list that appends 
        all songs with a tempo rating equal to the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a tempo rating thats equal to the given value
           
        Returns
        -----------
        tempo: list
            list that appends all songs that have a tempo rating thats equal to the given value
        """
        
        print('Now Sorting Playlist By Similar Tempo Values...')
        
        tempo = []
        temps = songs[songs.tempo == rating]
        tempo.append(temps)
        
        return tempo
    
    
    def higher_tempo(self,rating):
        """ Loops through tempo column in songs and creates a list that appends 
        all songs with a tempo rating higher than the given value.
        
        Parameters
        -----------
        rating: float
           float value that sets a limit to a given output, selecting every song with
           a tempo rating thats higher than the given value
           
        Returns
        -----------
        tempo: list
            list that appends all songs that have a tempo rating thats higher than the given value
        """
        
        print('Now Sorting Playlist By Higher Tempo Values...')
        
        tempo = []
        temps = songs[songs.tempo > rating]
        tempo.append(temps)
        
        return tempo
    


# In[26]:


speaker = Ipod()


# In[27]:


# Test Here vvv

## 1. Artist
    # print(speaker.list_by_artist('Post Malone'))

## 2. Song
    # print(speaker.play_song('In My Feelings'))

## 3. Danceability
    # print(speaker.lower_danceability(0.7))

    # print(speaker.same_danceability(0.6))

    # print(speaker.higher_danceability(0.5))

## 4. Energy
    # print(speaker.lower_energy(0.8))

    # print(speaker.same_energy(0.726))

    # print(speaker.more_energy(0.5))

## 5. Key
    # print(speaker.lower_key(2.0))

    # print(speaker.same_key(8.0))

    # print(speaker.higher_key(1.6))

## 6. Speechiness
    # print(speaker.lower_speechiness(0.8))

    # print(speaker.same_speechiness(0.2))
    
    # print(speaker.higher_speechiness(0.5))

## 7. Liveness
    # print(speaker.lower_liveness(.8))

    # print(speaker.same_liveness(.3))

    # print(speaker.higher_liveness(0.5))

## 8. Valence
    # print(speaker.lower_valence(0.8))

    # print(speaker.same_valence(0.7))

    # print(speaker.higher_valence(0.5))


## 9. Tempo
    # print(speaker.lower_tempo(100))

    # print(speaker.same_tempo(94.9))

    # print(speaker.higher_tempo(73))
# Can also even do this:
    # speaker.lower_danceability(1) and speaker.lower_energy(.7)


# # Information regarding my testing code and process
#     
# How my code works:
#     My testing process consist of me picking one specific method and then turning it into a function; pretty much using the same code, just not within a class. However, I do happen to change one little detail. I decided to switch from creating a playlist and appending it to a list, to rather creating a playlist then further updating an empty dictionary with it. By using a dictionary instead of a list, I was able to turn my dictionary to a dataframe much easier while managing to keep my data from looking messy. I did not do this in my original code as my return output playlist would be out of order if I had used a dictionary. 
#  
# Implementing the testing code:
# 
#    Pandas does not really allow me to flexibly use if, in, assert, along with many other key advantages in python. Yet by creating two distinct playlist, one using my function and the other using simple pandas methods like "head()" which simply display the first few rows of a dataframe, I was able to compare them and test out my function. By creating my playlist using dictionaries and then turning them into dataframes, I was able to use the "isin" pandas method to check if both my playlist had any row in common. My test would then work as I created those two playlist in unique ways, one using my built-in function and the other one using regular pandas methods; both playlist managed to have a song in common even though my function specifically searched for songs with a certain energy range. This then proves that my function works as the playlist created demonstrated only songs with a lower enegy rating than .5 and managed to match only in one song, the one I used as a test to see if the only similarity in these dataframes actually popped up. When you test the "isin" method on both my playlist, only one row evaluates as true.
#    

# In[28]:


# New changed lower_energy method, now a function w/ exact same code; just dictionary and not list

def lower_energy(rating):
    not_energetic = {}
    turnt_down = songs[songs.energy < rating]
    not_energetic.update(turnt_down)
    return not_energetic

# Test Function

def test_lower_energy():
    """ Function to test the lower_energy method I created. This functions creates two distinct playlist, 
    one using my built-in function and one using simple pandas methods, to further turn them into dataframes.
    By using the 'isin' pandas method, it checks if both dataframes have a song in common, which happens to be
    only one song that purposely comes out in the playlist I created using my built-in function. 
    
    ** I changed part of the original code; instead of appending the playlist to a list, I updated an
    empty dictionary **
    
    """
    
    lst = songs.head(5)
    data_f = pd.DataFrame(lst)
    
    lstt = lower_energy(.5)
    dfe = pd.DataFrame(lstt)
       
    data_f.isin(dfe)


# In[29]:


# Test my testing function

test_lower_energy()

# Or if you don't think calling my function proves my original function works, try this, proves the same song theory.

lst = songs.head(5)
data_f = pd.DataFrame(lst)
    
lstt = lower_energy(.5)
dfe = pd.DataFrame(lstt)
       

data_f.isin(dfe)


# In[30]:


# speaker.list_by_artist('Drake')
speaker.list_by_artist('Drake')


# # The End

# In[ ]:




