"""
    Logs
"""
from instagrapi import Client
import pickle

#login to Instagram
def login(username, password):
    cl = Client()
    cl.login(username, password)
    return cl
#save Login in a file for later use
def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
#use saved file object for Instagram interaction
def getLogin(filePath):
    with open(filePath, 'rb') as f:
        data = pickle.load(f)
        return data