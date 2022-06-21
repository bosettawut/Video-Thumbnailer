from flask import Flask, request, jsonify
import redis
from rq import Queue
from minio import Minio
from db import make_db, generate_id
from extract import extract_file_all, extract_file
from flask_cors import CORS
import os
import base64

app = Flask(__name__)
app.config.from_object(__name__)
# Redis
red = redis.Redis(host='redis', port=6379)
simple_app = Queue(connection=red)

current_directory = os.getcwd()
CORS(app,resources={r"/*":{'origin':"*"}})
CORS(app,resources={r"/*":{'origin':'http://localhost:8080',"allow_headings":"Access-Control-Allow-Origin"}})
# Minio access
host = "host.docker.internal:9000"
access_key = "minio"
secret_key = "minio123"

minioClient = Minio(host, 
                    access_key=access_key, 
                    secret_key=secret_key, 
                    secure=False)


<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/main

@app.route('/get_all_buckets', methods=['GET'])
def get_all_buckets():
    buckets = minioClient.list_buckets()
    list_buckets = []
    for bucket in buckets:
        st = str(bucket)
        list_buckets.append({"bucket":st})
    return  jsonify({"bucket_list":list_buckets})


@app.route('/list_videos',methods=['GET'])
def list_videos():
    objects = minioClient.list_objects("video",recursive=True)
    list_VID = []
    for obj in objects:
        fiv = ""
        a = minioClient.fget_object("video", obj.object_name, obj.object_name)
        strn = fiv.join(str(a.object_name.encode('utf-8')).split("b'"))
        le = len(strn)-1
        list_VID.append(strn[:le])

    return  jsonify({"All_Videos":list_VID})



@app.route('/list_gifs',methods=['GET'])
def list_gifs():

    objects = minioClient.list_objects("gif",recursive=True)
    list_GIF = []
    for obj in objects:
        fiv = ""
        a = minioClient.fget_object("gif", obj.object_name, obj.object_name)

        with open(current_directory + "/"+ a.object_name, "rb") as image_file :
            image = base64.b64encode(image_file.read())

        index = len(str(image))-1
        final = str(image)[2:index]

        list_GIF.append(final)


    return  jsonify({"All_GIF":list_GIF})


@app.route('/make_gif',methods=['POST'])
def make_gif():
    input = request.json
    job = simple_app.enqueue(generate_id)
    simple_app.enqueue(make_db,job.id,"Start Extracting")
    simple_app.enqueue(extract_file ,input['video'],job.id)

    return f"Task ({job.id}) added to queue."



@app.route('/make_all_gif',methods=['POST'])
def make_all():

    job = simple_app.enqueue(generate_id)
    simple_app.enqueue(make_db,job.id,"Start Extracting")
    simple_app.enqueue(extract_file_all,job.id)

    return f"Task({job.id}) added to queue."

@app.route('/get_status',methods=['GET'])
def get_status():
    input = request.json
    r = red.get(input['id'])
    return r

@app.route('/delete_gif',methods=['GET'])
def delete(): 
    objects_to_delete = minioClient.list_objects("gif", recursive=True)
    for obj in objects_to_delete:
        minioClient.remove_object("gif", obj.object_name)
    minioClient.remove_bucket("gif")
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
