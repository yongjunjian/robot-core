#encoding=utf8
from Queue import *
from ear import *
from mouth import *
from eye import *
from brain import *
class RobotCore:
    def __init__(self):
        self.audio_in = Queue()
        self.audio_slice = Queue()
        self.video_in = Queue()
        self.frame = Queue()
        self.audio_out = Queue()
        self.words_out = Queue()
    def wakeup(self):
        self.ear = Ear(self.audio_in, self.audio_slice); 
        self.eye = Eye(self.video_in, self.frame); 
        self.brain = Brain(self.audio_slice, self.frame, self.words_out);
        self.mouth =  Mouth(self.words_out, self.audio_out)
        self.ear.start_listen()
        self.eye.start_watch()
        self.brain.start_process()
        self.mouth.start_speak()
    def echo(self):
        self.audio_in.put("audio")
        self.video_in.put("video")
    def sleep():
        pass

robot = RobotCore()
robot.wakeup()
robot.echo()
