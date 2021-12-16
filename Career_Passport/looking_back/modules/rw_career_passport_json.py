import json
import os

def career_passport_original_read(school_id,year,semester,se):
    json_file=open('static/career_passport/'+str(school_id)+'/career_passport_origin/career_passport.json','r',encoding="utf-8_sig")
    data=json.load(json_file)
    return data['career_passport'][year-1][semester-1]['question'][0]['question_'+str(se)]

def career_passport_edit(school_id,year,semester,student_id,form_data,se):
    try:
        qr_data={}
        semester_data={}
        qr_data['question']=[]
        qr_data['result']=[]
        qr_data['question'].append({})
        qr_data['result'].append({})
        
        json_file=open('static/career_passport/'+str(school_id)+'/career_passport_origin/career_passport.json','r',encoding="utf-8_sig")
        data=json.load(json_file)

        if os.path.isfile('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json')==False:
            f=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','w',encoding="utf-8_sig")
            result_data={}
        else:
            stu_json_file=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
            result_data=json.load(stu_json_file)

        if 'student_career_passport_'+str(year) in result_data:
            if 'semester_'+str(semester) in result_data['student_career_passport_'+str(year)]:
                if se=='e':
                    if 'question_s' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['question'][0]:
                        qr_data['question'][0]['question_s']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['question'][0]['question_s']
                        qr_data['result'][0]['result_s']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['result'][0]['result_s']
                qr_data['question'][0]['question_'+str(se)]=data['career_passport'][year-1][semester-1]['question'][0]['question_'+str(se)]
                qr_data['result'][0]['result_'+str(se)]=form_data
                if se=='s':
                    if 'question_e' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['question'][0]:
                        qr_data['question'][0]['question_e']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['question'][0]['question_e']
                        qr_data['result'][0]['result_e']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['result'][0]['result_e']    
            else:
                qr_data['question'][0]['question_'+str(se)]=data['career_passport'][year-1][semester-1]['question'][0]['question_'+str(se)]
                qr_data['result'][0]['result_'+str(se)]=form_data
            
            if 'analize' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]:
                qr_data['analize']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['analize']
            if 'comment' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]:
                qr_data['comment']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['comment']

            semester_data['semester_'+str(semester)]=qr_data
            result_data['student_career_passport_'+str(year)].update(semester_data)
        else:
            qr_data['question'][0]['question_'+str(se)]=data['career_passport'][year-1][semester-1]['question'][0]['question_'+str(se)]
            qr_data['result'][0]['result_'+str(se)]=form_data
            semester_data['semester_'+str(semester)]=qr_data
            result_data['student_career_passport_'+str(year)]=semester_data

        f=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','w',encoding="utf-8_sig")
        json.dump(result_data,f,ensure_ascii=False,indent=4,separators=(',', ': '))
        #f=open(str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
        #data=json.load(f)
        return '成功しました'
    except:
        return '失敗しました'

def get_career_passport(school_id,student_id):
    f=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
    data=json.load(f)
    return data

def select_career_passport(school_id,year,semester,student_id):
    f=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
    data=json.load(f)
    if 'student_career_passport_'+str(year) in data:
        if 'semester_'+str(semester) in data['student_career_passport_'+str(year)]:
            return data['student_career_passport_'+str(year)]['semester_'+str(semester)]
        else:
            return 'データがありません'
    else:
        return 'データがありません'
        

def career_passport_add_comment(school_id,year,semester,student_id,comment,se):
    try:
        qr_data={}
        semester_data={}

        stu_json_file=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
        result_data=json.load(stu_json_file)

        qr_data['question']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['question']
        qr_data['result']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['result']
        qr_data['analize']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['analize']
        qr_data['comment']=[]
        qr_data['comment'].append({})
        
        if 'comment' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]:
            if se=='e':
                if 'comment_s' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['comment'][0]:
                    qr_data['comment'][0]['comment_s']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['comment'][0]['comment_s']
            qr_data['comment'][0]['comment_'+str(se)]=comment
            if se=='s':
                if 'comment_e' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['comment'][0]:
                    qr_data['comment'][0]['comment_e']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['comment'][0]['comment_e']
        else:
            qr_data['comment'][0]['comment_'+str(se)]=comment

        semester_data['semester_'+str(semester)]=qr_data
        result_data['student_career_passport_'+str(year)].update(semester_data)

        f=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','w',encoding="utf-8_sig")
        json.dump(result_data,f,ensure_ascii=False,indent=4,separators=(',', ': '))
        return '成功しました'
    except:
        return '失敗しました'
    #f=open(str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
    #data=json.load(f)

def read_book_data(word):
    if os.path.isfile('static/profession_book/profession_json/'+word+'.json'):
        f=open('static/profession_book/profession_json/'+word+'.json','r',encoding="utf-8_sig")
        data=json.load(f)
        return data
    else:
        return 0