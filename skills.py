import datetime
import pywhatkit
#from app import speak_lexi

def get_current_time():
  time = datetime.datetime.now().strftime('%I:%M %p')
  return time

def get_current_date():
  dt = datetime.date.today().strftime('%A %d %B %Y')
  return dt


  
