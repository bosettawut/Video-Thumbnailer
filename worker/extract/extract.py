#!/usr/bin/env python3
import time
from minio import Minio
import redis
import os,shutil,subprocess,logging,time
from rq import Queue
from db import make_db
from gif import make_gif


LOG =logging

red = redis.Redis(host='redis', port=6379)
simple_app = Queue(connection=red)


#Minio access
host = "host.docker.internal:9000"
access_key = "minio"
secret_key = "minio123"

minioClient = Minio(host, access_key=access_key, secret_key=secret_key, secure=False)

# for extract variables
sleep_seconds = 2
current_directory = os.getcwd()
arr = os.listdir()


def extract_file_all(id):
        videos = minioClient.list_objects("video", recursive=True)
        simple_app.enqueue(make_db,id,"Extracting process")
        for video in videos:
                extract(video.object_name,id)
        return "DONE_LOOP!!!"

def extract_file(video,id):
        print('Got Request - Start Downloading... ')
        # put the function that extract specific video to frames and add this to minio
        minioClient.fget_object("video",video,"./video/"+video)
        shutil.move(current_directory+"/video/"+video , current_directory)
        print('Object downloaded')
        
        simple_app.enqueue(make_db,id,"Extracting process")
        # # Make 2 directories for keeping the frames and all files
        name_frames = str(video).split(".mp4")
        name_frames2 = ""
        name_frames3 = name_frames2.join(name_frames)
        
        subprocess.run(["mkdir","ffmpeg"])
        subprocess.run(["mkdir",name_frames3]) # create frames(saitama, cat,timer)
        
 
        #current_directory + /frames(saitama)
        name_frames_dir = current_directory+"/"+name_frames3
        #current_directory+ /video.mp4
        saitama = current_directory+"/"+ video
        #current_directory+ /ffmpeg(include all files inside)
        c = current_directory+"/ffmpeg" 
        
        output = name_frames3+"1"+".mp4" # saitama1.mp4 / timer1.out
        

        shutil.copy(saitama, c) # move saitama.mp4 to ffmpeg directory
        shutil.move(name_frames_dir, c) #move frames(saitama) to ffmpeg directory
        
        print('Extracting to frames...')
        subprocess.run(["ffmpeg","-t","10", "-i", video, "-s" ,"480x360" ,"-c:a" ,"copy", output],cwd = c)
        time.sleep(sleep_seconds)
        subprocess.run(["ffmpeg", "-i", output , name_frames3+"/image%04d.jpg"],cwd = c)
        time.sleep(sleep_seconds)
  
        #move folder frames to current directory
        shutil.move(current_directory+"/ffmpeg/"+ name_frames3, current_directory)
        
        subprocess.run(["rm",video], check = True,cwd = c) # remove saitama.mp4
        time.sleep(sleep_seconds)
        subprocess.run(["rm",output], check = True,cwd = c) # remove saitama1.mp4
        time.sleep(sleep_seconds)
        subprocess.run(["rm","-R","ffmpeg"], check = True,cwd = current_directory) #remove ffmpeg
        time.sleep(sleep_seconds)
        
        # /app/saitama(frames inside)
        directory = current_directory+"/"+name_frames3
        # for loop inside to upload frames to object store(Minio)
        print('Frames extracted')
        print('Uploading frames to Minio...')
        
        Create_bucket("frames")       
     
        fr2 = os.scandir(directory)
        
        for filename in fr2:
                if filename.is_file():
                        minioClient.fput_object("frames", name_frames3 +"/"+ filename.name, filename.path)
                        print(filename.name)
        print('Done extracting')
       
        simple_app.enqueue(make_gif, "".join(str(video).split(".mp4")),id)
        return "Done Extracting"



# def extract_file_helper(video):
#         # make unique folder in frame(bucket) and put all frames of that video in the unique folder 
#         return None            


def extract(video,id):
        
        print('Start Downloading... video from minio ')
        # put the function that extract specific video to frames and add this to minio
        minioClient.fget_object("video",video,"./video/"+video)
        shutil.move(current_directory+"/video/"+video , current_directory)
        
        print('video downloaded')
        
        # # Make 2 directories for keeping the frames and all files
        name_frames = str(video).split(".mp4")
        name_frames2 = ""
        name_frames3 = name_frames2.join(name_frames)
        
        subprocess.run(["mkdir","ffmpeg"])
        subprocess.run(["mkdir",name_frames3]) # create frames(saitama, cat,timer)
        
 
        #current_directory + /frames(saitama)
        name_frames_dir = current_directory+"/"+name_frames3
        #current_directory+ /video.mp4
        saitama = current_directory+"/"+ video
        #current_directory+ /ffmpeg(include all files inside)
        c = current_directory+"/ffmpeg" 
        
        output = name_frames3+"1"+".mp4" # saitama1.mp4 / timer1.out
        

        shutil.copy(saitama, c) # move saitama.mp4 to ffmpeg directory
        shutil.move(name_frames_dir, c) #move frames(saitama) to ffmpeg directory
        
        print('Extracting to frames...')
        subprocess.run(["ffmpeg","-t","10", "-i", video, "-s" ,"480x360" ,"-c:a" ,"copy", output],cwd = c)
        time.sleep(sleep_seconds)
        subprocess.run(["ffmpeg", "-i", output , name_frames3+"/image%04d.jpg"],cwd = c)
        time.sleep(sleep_seconds)
  
        #move folder frames to current directory
        shutil.move(current_directory+"/ffmpeg/"+ name_frames3, current_directory)
        
        subprocess.run(["rm",video], check = True,cwd = c) # remove saitama.mp4
        time.sleep(sleep_seconds)
        subprocess.run(["rm",output], check = True,cwd = c) # remove saitama1.mp4
        time.sleep(sleep_seconds)
        subprocess.run(["rm","-R","ffmpeg"], check = True,cwd = current_directory) #remove ffmpeg
        time.sleep(sleep_seconds)
        
        # /app/saitama(frames inside)
        directory = current_directory+"/"+name_frames3
        # for loop inside to upload frames to object store(Minio)
        print('Frames extracted')
        
        print('Uploading frames to Minio...')
        
        Create_bucket("frames")       
     
        fr2 = os.scandir(directory)
        
        for filename in fr2:
                if filename.is_file():
                        minioClient.fput_object("frames", name_frames3 +"/"+ filename.name, filename.path)
                        print(filename.name)
        print('Done extracting')
       
        simple_app.enqueue(make_gif, "".join(str(video).split(".mp4")),id)
        len(simple_app)
        
        return "Done Extracting"
           
          
def Create_bucket(name):
        
        if minioClient.bucket_exists(name):
                print("already exits!")
        else:
                minioClient.make_bucket(name)
                