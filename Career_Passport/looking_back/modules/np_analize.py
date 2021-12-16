from janome.tokenizer import Tokenizer
import csv
import re
import emoji
import nagisa
import unicodedata
import json

dict_data={}
csv_file=open('static/dict/dict.csv', 'r',encoding="utf-8")
data=csv.reader(csv_file)
for row in data:
    if row[0]!='':
        dict_data[row[0]]=row[1]

noun_dict_data={}
csv_file=open('static/dict/dict_trim.csv', 'r',encoding="utf-8")
data_noun=csv.reader(csv_file)
for row in data_noun:
    if row[0]!='':
        noun_dict_data[row[0]]=row[1]

reverse_dict_data={}
csv_file=open('static/dict/reverse_dict.csv','r',encoding="utf-8")
data_reverse=csv.reader(csv_file)
for row in data_reverse:
    if row[0]!='':
        reverse_dict_data[row[0]]=row[1]

def modify(text):
    text=re.sub(emoji.get_emoji_regexp(), '', text)
    text = unicodedata.normalize('NFKC', text)
    text=text.replace(' ','')
    text=text.replace('　','')
    text = unicodedata.normalize('NFKC', text)
    results=nagisa.extract(text, extract_postags=['補助記号'])
    symbol=results.words
    kaomoji=[i for i, w in enumerate(symbol) if len(w) >= 2]
    for i in kaomoji:
        text=text.replace(symbol[i],'')
    remove_marks_regex=re.compile("[,\.\(\)\[\]\（\）\*:;]|<.*?>")
    remove_symbol=re.compile('[■-♯]')
    text_without_url=re.compile("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    text=text.lower()
    text=text_without_url.sub("",text)
    text=remove_marks_regex.sub(" ",text)
    text=remove_symbol.sub(" ",text)
    #print(text)
    return text


def judge_np(text):
    text=modify(text)
    stop_word=["私","彼","彼女","僕","自分"]
    tokenizer=Tokenizer('static/dict/user_dict.csv',udic_type='simpledic',udic_enc='utf8')
    tokens=list(tokenizer.tokenize(text))
    np_val=0
    count=0
    for number in range(len(tokens)):
        reverse=1
        limit=0
        #print(tokens[number])
        word=tokens[number].surface
        pos = tokens[number].part_of_speech.split(',')[0]
        origin=tokens[number].base_form

        if word in stop_word or tokens[number].part_of_speech[2]=="人名" or tokens[number].part_of_speech.split(',')[0]=='助詞' or tokens[number].part_of_speech.split(',')[0]=='助動詞' or tokens[number].part_of_speech.split(',')[0]=='カスタム連語':
            continue
        else:
            if pos=='名詞' or pos=='カスタム名詞':
                if word in noun_dict_data:
                    if number<len(tokens)-1:
                        if tokens[number+1].part_of_speech.split(',')[0]=='カスタム連語':
                            if tokens[number+1].surface in reverse_dict_data:
                                reverse=reverse_dict_data[tokens[number+1].surface]
                    np_val=np_val+(int(noun_dict_data[word])*int(reverse))
                    count+=1
                    limit+=1
                
            if limit==0:
                if word in dict_data:
                    if number<len(tokens)-1:
                        if tokens[number+1].part_of_speech.split(',')[0]=='カスタム連語':
                            if tokens[number+1].surface in reverse_dict_data:
                                reverse=reverse_dict_data[tokens[number+1].surface]
                    np_val=np_val+(int(dict_data[word])*int(reverse))
                    count+=1
                else:
                    if origin in dict_data:
                        if number<len(tokens)-1:
                            if tokens[number+1].part_of_speech.split(',')[0]=='カスタム連語':
                                if tokens[number+1].surface in reverse_dict_data:
                                    reverse=reverse_dict_data[tokens[number+1].surface]
                        np_val=np_val+(int(dict_data[origin])*int(reverse))
                        count+=1

    if -count<=np_val and np_val<-count/6:
        return ['negative',np_val]
    elif -count/6<=np_val and np_val<=count/6:
        return ['neutral',np_val]
    elif count/6<np_val and np_val<=count:
        return ['positive',np_val]

def judge_np_occupational_aptitude(text):
    text=modify(text)
    stop_word=["私","彼","彼女","僕","自分"]
    tokenizer=Tokenizer('static/dict/user_dict.csv',udic_type='simpledic',udic_enc='utf8')
    tokens=list(tokenizer.tokenize(text))
    np_val=0
    count=0
    for number in range(len(tokens)):
        reverse=1
        limit=0
        #print(tokens[number])
        word=tokens[number].surface
        pos = tokens[number].part_of_speech.split(',')[0]
        origin=tokens[number].base_form

        if word in stop_word or tokens[number].part_of_speech[2]=="人名" or tokens[number].part_of_speech.split(',')[0]=='助詞' or tokens[number].part_of_speech.split(',')[0]=='助動詞' or tokens[number].part_of_speech.split(',')[0]=='カスタム連語':
            continue
        else:
            if pos=='名詞' or pos=='カスタム名詞':
                if word in noun_dict_data:
                    if number<len(tokens)-1:
                        if tokens[number+1].part_of_speech.split(',')[0]=='カスタム連語':
                            if tokens[number+1].surface in reverse_dict_data:
                                reverse=reverse_dict_data[tokens[number+1].surface]
                    np_val=np_val+(int(noun_dict_data[word])*int(reverse))
                    count+=1
                    limit+=1
                
            if limit==0:
                if word in dict_data:
                    if number<len(tokens)-1:
                        if tokens[number+1].part_of_speech.split(',')[0]=='カスタム連語':
                            if tokens[number+1].surface in reverse_dict_data:
                                reverse=reverse_dict_data[tokens[number+1].surface]
                    np_val=np_val+(int(dict_data[word])*int(reverse))
                    count+=1
                else:
                    if origin in dict_data:
                        if number<len(tokens)-1:
                            if tokens[number+1].part_of_speech.split(',')[0]=='カスタム連語':
                                if tokens[number+1].surface in reverse_dict_data:
                                    reverse=reverse_dict_data[tokens[number+1].surface]
                        np_val=np_val+(int(dict_data[origin])*int(reverse))
                        count+=1

    if -count<=np_val and np_val<-count/6:
        return ['negative',five_score(np_val,count),np_val]
    elif -count/6<=np_val and np_val<=count/6:
        return ['neutral',five_score(np_val,count),np_val]
    elif count/6<np_val and np_val<=count:
        return ['positive',five_score(np_val,count),np_val]

def five_score(np_val,count):
    if -count<=np_val and np_val<-count*3/10:
        return 1
    elif -count*3/10<=np_val and np_val<count*1/10:
        return 2
    elif -count*1/10<=np_val and np_val<=count*1/10:
        return 3
    elif count*1/10<np_val and np_val<=count*3/10:
        return 4
    elif count*3/10<np_val and np_val<=count:
        return 5

def register(school_id,year,semester,student_id,data_list,se):
    try:
        qr_data={}
        semester_data={}

        stu_json_file=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','r',encoding="utf-8_sig")
        result_data=json.load(stu_json_file)

        qr_data['question']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['question']
        qr_data['result']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['result']
        qr_data['analize']=[]
        qr_data['analize'].append({})
            
        if 'comment' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]:
            qr_data['comment']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['comment']

        if 'analize' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]:
            if se=='e':
                if 'analize_s' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['analize'][0]:
                    qr_data['analize'][0]['analize_s']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['analize'][0]['analize_s']
            qr_data['analize'][0]['analize_'+str(se)]=data_list
            if se=='s':
                if 'analize_e' in result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['analize'][0]:
                    qr_data['analize'][0]['analize_e']=result_data['student_career_passport_'+str(year)]['semester_'+str(semester)]['analize'][0]['analize_e']
        else:
            qr_data['analize'][0]['analize_'+str(se)]=data_list

        semester_data['semester_'+str(semester)]=qr_data
        result_data['student_career_passport_'+str(year)].update(semester_data)

        f=open('static/career_passport/'+str(school_id)+'/student_register/career_passport_'+str(student_id)+'.json','w',encoding="utf-8_sig")
        json.dump(result_data,f,ensure_ascii=False,indent=4,separators=(',', ': '))
        return '成功しました'
    except:
        return '失敗しました'

def occupational_aptitude(school_id,user_id):
    try:
        f=open('static/occupational_aptitude/'+str(school_id)+'/occupational_aptitude_'+str(user_id)+'.json','r',encoding="utf-8_sig")
        data=json.load(f)
        pre_store=[]
        data_result={}
        data_result['result']=data['result']
        for text in data['result']:
            pre_store.append(judge_np_occupational_aptitude(text))
        data_result['analize']=pre_store
        f=open('static/occupational_aptitude/'+str(school_id)+'/occupational_aptitude_'+str(user_id)+'.json','w',encoding="utf-8_sig")
        json.dump(data_result,f,ensure_ascii=False,indent=4,separators=(',', ': '))
        return '成功しました'
    except:
        return '失敗しました'