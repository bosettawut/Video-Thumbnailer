#!/usr/bin/env python3
import time
from minio import Minio
import os,shutil,subprocess,logging,time
import redis
from db import make_db
from rq import Queue
red = redis.Redis(host='redis', port=6379)
simple_app = Queue(connection=red)
#Minio access
host = "host.docker.internal:9000"
access_key = "minio"
secret_key = "minio123"

minioClient = Minio(host, access_key=access_key, secret_key=secret_key, secure=False)

# for extract variables
current_directory = os.getcwd()
arr = os.listdir()
sleep_seconds = 2

def make_gif(name_video,id):
        
        print('Start Downloading Frames... ')
        
        simple_app.enqueue(make_db,id,"Making GIF process")
        # Downlode frames from Minio      
        objects = minioClient.list_objects("frames",recursive=True)
        for obj in objects:
                minioClient.fget_object("frames", obj.object_name, obj.object_name)
        
        # convert process
        print('Compiling to GIF...')
        r = subprocess.Popen(["convert","-delay","10","*.jpg",name_video+".gif"], cwd = current_directory+"/"+ name_video)
        r.wait()
        shutil.move(current_directory+"/"+ name_video+"/"+ name_video + ".gif",current_directory)
        # upload GIF to Minio  
        print('Uploading GIF to Minio...')  
        name_bucket_GIF = "gif"
        Create_bucket(name_bucket_GIF)       
        minioClient.fput_object(name_bucket_GIF,name_video+".gif",current_directory+"/"+name_video+".gif")

        
        ### delete file keep only gif file 
        subprocess.run(["rm",name_video+".mp4"])
        time.sleep(sleep_seconds)
        subprocess.run(["rm","-R","video"])
        time.sleep(sleep_seconds)
        subprocess.run(["rm","-R",name_video])
        

        # simple_app.enqueue(make_db,id,"DONE")
        if(red.get(id) == "A GIF is Made"):
                simple_app.enqueue(make_db,id,"Another GIF is Made")
        else:
                simple_app.enqueue(make_db,id,"A GIF is Made")
        
        return "FINISH !!"
       

   
def Create_bucket(name):
        
        if minioClient.bucket_exists(name):
                print("already exits!")
        else:
                minioClient.make_bucket(name)
                


             
            
            
    
            