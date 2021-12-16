import json
import os

def occupatonal_aptitude_original_read():
    json_file=open('static/occupational_aptitude/occupational_aptitude_origin/occupational_aptitude.json','r',encoding="utf-8_sig")
    data=json.load(json_file)
    return data['occupational_aptitude']

def occupational_aptitude_read(school_id,user_id):
    if os.path.isfile('static/occupational_aptitude/'+str(school_id)+'/occupational_aptitude_'+str(user_id)+'.json')==False:
        return 'データが登録されていません'
    else:
        json_file=open('static/occupational_aptitude/'+str(school_id)+'/occupational_aptitude_'+str(user_id)+'.json','r',encoding="utf-8_sig")
        data=json.load(json_file)
        return data

def occupational_aptitude_write(school_id,user_id,data):
    qr_data={}
    result_data=data
    qr_data['result']=result_data
    f=open('static/occupational_aptitude/'+str(school_id)+'/occupational_aptitude_'+str(user_id)+'.json','w',encoding="utf-8_sig")
    json.dump(qr_data,f,ensure_ascii=False,indent=4,separators=(',', ': '))