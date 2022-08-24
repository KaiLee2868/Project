import os
import sys
import requests
import json
import urllib.request

class Unit:
    global names
    def find_face():        

        client_id = "11HJJdO0rpz89p6pwoBO"
        client_secret = "tnXn17cb4W"
        url_face = "https://openapi.naver.com/v1/vision/face" 
        url_celebrity = "https://openapi.naver.com/v1/vision/celebrity"  
        
        file_name = "star.jpg"

        files = {'image': open(file_name, 'rb')}
        headers = {'X-Naver-Client-Id': client_id,
                'X-Naver-Client-Secret': client_secret}
        response = requests.post(url_celebrity,  files=files, headers=headers)
        rescode = response.status_code


        if(rescode == 200):
            # print(response.text)
            data = json.loads(response.text)
            print(type(data))
            encText = urllib.parse.quote(data["faces"][0]["celebrity"]["value"])
            url_trans_name = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText 
            request = urllib.request.Request(url_trans_name)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            response_body = response.read()
            json_dict = json.loads(response_body.decode('utf-8'))
            result = json_dict['aResult'][0]
            print(json_dict['aResult'])
            name_items = result['aItems']
            global names
            names = [name_item['name'] for name_item in name_items]
            print(f'FaceCount = {data["info"]["faceCount"]}, Name = {names[0]}, Confidence = {data["faces"][0]["celebrity"]["confidence"]}')

        else:
            print("Error Code:" + rescode)



        files = {'image': open(file_name, 'rb')}
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url_face,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode==200 ):   
            data2 = json.loads(response.text)    
            print(f'Gender = {data2["faces"][0]["gender"]["value"]}, Emotion = {data2["faces"][0]["emotion"]["value"]}')
        else:
            print("Error Code:" + rescode)

    

    def result_face():
        return names[0]            