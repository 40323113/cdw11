# coding: utf-8
from flask import Flask, send_from_directory, request, redirect, render_template, session, make_response
import random
import math
import os
# init.py 為自行建立的起始物件
import init
import users.a.g1.ag1_40323105
import users.a.g2.ag2_40323120
import users.a.g10.ag10_40323129_task1
import users.a.g10.ag10_40323141_task1
import users.a.g10.ag10_40323139
import users.a.g9.ag9_40323132task
import users.a.g5.ag5_40323113task1
import users.a.g5.ag5_40323113_gears
import users.a.g5.ag5_40123145task1
import users.a.g5.ag5_40123145task2
import users.a.g5.ag5_40123145task3
import users.a.g4.ag4_40323138
import users.a.g4.ag4_40323138_task2bacd
import users.a.g4.ag4_40323138_task3abcd
import users.a.g8.ag8_40323131_task1
import users.b.g9.bg9_40323250
import users.a.g8.ag8_40323123
import users.a.g1.a40223153
import users.a.g3.ag3_40323108
import users.a.g3.ag3_40323108_task2bacd
import users.a.g3.ag3_40323108_task3abcd
import users.a.g4.ag4_40323109
import users.a.g4.ag4_40323109_task2bacd
import users.a.g4.ag4_40323109_task3abcd
#bg1
import users.b.g1.bg1_40123156
import users.b.g1.bg1_40123156_2
import users.b.g1.bg1_40123129
import users.b.g1.bg1_40123129_2
import users.b.g1.bg1_40123144
import users.b.g1.bg1_40123144_2
import users.b.g1.b40123131_cdw11
import users.b.g1.b40123131_cdw12
import users.b.g1.b40123131_cdw13

import users.b.g1.b40123131_cdw11
import users.b.g1.b40123131_cdw12
import users.b.g1.bg1_40123134
import users.b.g1.bg1_40123134_2
import users.b.g1.bg1_40123134_3
import users.b.g1.b40123133_cdw11
import users.b.g1.b40123133_cdw12
import users.b.g1.bg1_40123126
import users.b.g1.bg1_40123126_2
#bg2
import users.b.g2.bg2_40123235
import users.b.g2.bg2_40123235_cdw12
import users.b.g2.bg2_40123235_cdw14
import users.b.g2.bg2_40123202
import users.b.g2.bg2_40123202_cdw13
import users.b.g2.bg2_40123202_cdw14
import users.b.g2.bg2_40123226_cdw12
import users.b.g2.bg2_40123232_cdw12
import users.b.g2.bg2_40123214_cdw12
import users.b.g2.bg2_40123217_cdw12
import users.b.g2.bg2_40123244_cdw12
#bg4
import users.b.g4.bg4_40323203
import users.b.g4.bg4_40323205
import users.b.g4.bg4_40323208
import users.b.g4.bg4_40123128
import users.b.g4.bg4_40123128_cdw11
import users.b.g4.bg4_40123128_cdw14
#bg8
import users.b.g8.bg8_40323213
import users.b.g4.bg4_40323202
import users.b.g4.b40323201_cdw11

#bg5
#import users.b.g5.b40323206_cdw11_1
import users.b.g5.b40323204_cdw11_1
import users.b.g5.b40323204_cdw11
import users.b.g5.b40323204_cdw11_2

#bg5
#import users.b.g5.b40323206_cdw11_1
import users.b.g5.b40323204_cdw11_1
import users.b.g5.b40323204_cdw11_2
import users.b.g5.b40323206_cdw11_2
#bg11

import users.b.g11.bg11_40323252
#import users.b.g11.bg11_40323245_1
import users.b.g11.b40323252
import users.b.g11.bg11_40323245
#import users.b.g11.bg11_40323245_1
import users.b.g11.b40323252

#bg101
import users.b.g101.b40123200
#ag7
import users.a.g7.ag7_40123149_1
import users.a.g7.ag7_40123149_2
#ag8
import users.a.g8.a40323143
import users.a.g8.a40323137
import users.a.g8.a40323154
#ag10
import users.a.g10.a40323139
import users.a.g10.a40323141
#bg3
#import users.b.g3.b40123224
#import users.b.g3.b40123250
#import users.b.g3.b40123242
import users.b.g3.bg3_40123224
import users.b.g3.bg3_40123224_cdw11
import users.b.g3.bg3_40123250
import users.b.g3.bg3_40123250_cdw11
import users.b.g3.bg3_40123250_cdw14
import users.b.g3.bg3_40123224_cdw14
#import users.b.g3.b40123242
import users.b.g3.bg3_40123242_cdw12
#ag3
import users.a.g3.a40323108
#ag100
import users.a.g100.cdw13.a40123100
# 確定程式檔案所在目錄, 在 Windows 有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
    static_dir = os.environ['OPENSHIFT_REPO_DIR']+"/static"
    download_dir = os.environ['OPENSHIFT_DATA_DIR']+"/downloads"
else:
    # 表示程式在近端執行
    data_dir = _curdir + "/local_data/"
    static_dir = _curdir + "/static"
    download_dir = _curdir + "/local_data/downloads/"

# 利用 init.py 啟動, 建立所需的相關檔案
initobj = init.Init()

# 必須先將 download_dir 設為 static_folder, 然後才可以用於 download 方法中的 app.static_folder 的呼叫
app = Flask(__name__)
#app.config['download_dir'] = download_dir

# 使用 session 必須要設定 secret_key
# In order to use sessions you have to set a secret key
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr9@8j/3yX R~XHH!jmN]LWX/,?R@T'






@app.route("/")
def index():
    #這是猜數字遊戲的起始表單, 主要在產生答案, 並且將 count 歸零
    # 將標準答案存入 answer session 對應區
    theanswer = random.randint(1, 100)
    thecount = 0
    # 將答案與計算次數變數存進 session 對應變數
    session['answer'] = theanswer
    session['count'] = thecount

    return render_template("index.html", answer=theanswer, count=thecount)
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)
@app.route('/red')
def red():
    # 重新導向 google
    return redirect("http://www.google.com")
@app.route('/guessform')
def guessform():
    session["count"] += 1
    guess = session.get("guess")
    theanswer = session.get("answer")
    count = session.get("count")
    return render_template("guessform.html", guess=guess, answer=theanswer, count=count)
@app.route('/docheck', methods=['POST'])
def docheck():
    # session[] 存資料
    # session.get() 取 session 資料
    # 利用 request.form[] 取得表單欄位資料, 然後送到 template
    guess = request.form["guess"]
    session["guess"] = guess
    # 假如使用者直接執行 doCheck, 則設法轉回根方法
    if guess is None:
        redirect("/")
    # 從 session 取出 answer 對應資料, 且處理直接執行 docheck 時無法取 session 值情況
    try:
        theanswer = int(session.get('answer'))
    except:
        redirect("/")
    # 經由表單所取得的 guess 資料型別為 string
    try:
        theguess = int(guess)
    except:
        return redirect("/guessform")
    # 每執行 doCheck 一次,次數增量一次
    session["count"] += 1
    count = session.get("count")
    # 答案與所猜數字進行比對
    if theanswer < theguess:
        return render_template("toobig.html", guess=guess, answer=theanswer, count=count)
    elif theanswer > theguess:
        return render_template("toosmall.html", guess=guess, answer=theanswer, count=count)
    else:
        # 已經猜對, 從 session 取出累計猜測次數
        thecount = session.get('count')
        return "猜了 "+str(thecount)+" 次, 終於猜對了, 正確答案為 "+str(theanswer)+": <a href='/'>再猜</a>"
    return render_template("docheck.html", guess=guess)
 
@app.route('/option', methods=["GET", "POST"])
def option():
    # 各組選出組長的方式, 若採遞增, 則各組內學號最小者為組長
    option_list1 = ["遞增", "遞減"]
    # 各組組長間的排序定組序, 若採遞增, 則學號最小的組長為第1組
    option_list2 = ["遞增", "遞減"]
    # 電腦教室共有 9 排電腦
    column = 9
    # 加上班級選擇
    option_list3 = ["2a", "2b"]
    # 根據班級的總人數, 以 9 去除, 算出需要排幾列才能夠容納的下, 而且若列數超過 7
    # 表示這些學員必須與其他同組學員共用電腦

    return render_template('option.html', option_list1=option_list1, option_list2=option_list2, option_list3=option_list3, column=column)
@app.route('/optionaction', methods=['POST'])
def optionaction():
    # 最後傳回的字串為 out_string
    out_string = ""
    # 程式內需要暫時使用的 tmp_string
    tmp_string = ""
    # 傳回字串中, 用來說明排序原則的 desc_string
    desc_string = ""
    result = []
    group_sorted = []
    num_of_stud = 0
    # 每組至多 7 人
    max_num_in_one_group = 7
    # 電腦教室配置, 共有 9 排
    total_column = 9
    # 上面為相關變數的初始值設定, 以下開始取出 data_a 或 data_b 進行處理, 由 option3 傳回值決定
    if request.form["option3"]  == "2a":
        content = request.form["data_a"]
    else:
        content = request.form["data_b"]
    #result = content.splitlines()
    for line in content.splitlines():
        result.append(list(line.split(",")))
    # i 為行序
    for i in range(len(result)):
        # j 為組員序
        for j in range(len(result[i])):
            tmp_string += result[i][j] + ", "
        out_string += "第" + str(i+1) + "排資料:"+ tmp_string + "<br />"
        tmp_string = ""
    for i in range(len(result)):
        # 開始進入組內排序, 根據 request.form["option1"]  的值決定遞增或遞減
        if request.form["option1"]  == "遞增":
            group_list = sorted(list(filter(None, result[i])))
        else:
            group_list = sorted(list(filter(None, result[i])), reverse=True)
        group_sorted.append(group_list)
    if request.form["option1"]  == "遞增":
        desc_string += "組內學號最小者為組長."
    else:
         desc_string += "組內學號最大者為組長."
    # 開始進入組間組長學號排序, 根據 request.form["option2"] 的值決定遞增或遞減
    if request.form["option2"]  == "遞增":
        desc_string += "各組長中學號最小者為第1組."
        final_result = sorted(group_sorted)
    else:
        desc_string += "各組長中學號最大者為第1組."
        final_result = sorted(group_sorted, reverse=True)
    out_string += "<br />" + desc_string + "<br />"
    # i 為行序
    for i in range(len(final_result)):
        # j 為組員序
        for j in range(len(final_result[i])):
            num_of_stud += 1
            tmp_string += final_result[i][j] + ","
        out_string += "第" + str(i+1) + "組:"+ tmp_string + "<br />"
        tmp_string = ""
    #return "總共有" + str(i+) + "組"
    # group_num 為總組數
    group_num = i + 1
    # 截至這裡, 已經完成選組長, 以及定組序的工作 ,接下來要排座位, 並且印出座位表
    # 先算每班的總人數
    #return "總共有"+ str(num_of_stud) + "人"
    seat_by_column = []
    for row in range(max_num_in_one_group):
    # 每組最多 7 人
    #for row in range(7):
        # 這裡的 11 為總組數
        #for column in range(11):
        for column in range(group_num):
            # 因為各分組數列的長度並不相同, 但是最長的有 7 位組員, 因此若無法取得的資料 (因為索引超值), 就補上空字串
            try:
                seat_by_column.append(final_result[column][row])
            except:
                seat_by_column.append("")
    # seat_by_column 為去除空白字串前的座位數列
    # 然後利用 filter(None, seat_by_column) 去除空白字串, 就可以得到以 column 為主的座位排序
    seat_by_column = list(filter(None, seat_by_column))
    # 然後每 N 個取為 1 排, 即可得到以排為主的座位序列, 而 N 則視全班人數除以 9, 也就是 total_column 進位決定, 因為共有 9 排
    N = math.ceil(num_of_stud/total_column)
    # for debug
    #return str(num_of_stud) + ":" + str(total_column) + ":" + str(N)
    column_list = [seat_by_column[n:n+N] for n in range(0, len(seat_by_column), N)]
    # 列出每 N 個組員一排的數列 column_list
    # 接下來要納入以排為主的座位
    # 根據 column_list, 建立一個 dictionary, 其中學號為 index, 座位號為對應值
    seat_dict = {}
    for column in range(len(column_list)):
        for i in range(N):
            try:
                seat_dict.update({column_list[column][i]: (column, i)})
            except:
                seat_dict.update({"": ""})
                
    # 開始準備用順序列出學員座號
    # 根據學號, 排序 dictionary 的方法
    import operator
    seat_dict_sort = sorted(seat_dict.items(), key = operator.itemgetter(0), reverse = False)
    # 依照學號順序, 列出座位表
    out_string += "<br />按照學號次序列出座位表:<br /><br />"
    for i in range(1, len(seat_dict_sort)):
        out_string +=  str(i) + ":"+ str(seat_dict_sort[i]) + "<br />"
    # 結束準備用順序列出學員座號
    # dont know why .reverse() did not work, 只有 [::-1] 可以 reverse list elements
    #g.es(column_list[::-1])

    # 因為經由 zip 逐一重新 transpose 的列資料, 必須配合最大 (也就是總共有 7 列, 也就是 N 的值) 列數補上空白字串 (也就是空位)
    # 所以不能使用 zip, 而必須導入 zip_longest 模組方法
    from itertools import zip_longest
    final_seat = list(zip_longest(*column_list[::-1], fillvalue=""))
    # 列出最後的座位表
    #g.es(final_seat)
    # 最後轉成 html table 標註格式
    out_string += "<br /> <br />"
    out_string += "<table border='1' width='100%'>"
    out_string += "<tr><td colspan='9' style='text-align:center'>講台</td></tr>"
    for row in range(len(final_seat)):
        out_string += "<tr>"
        # 因為每一 row 有 9, 也就是 total_column 個位子
        for i in range(total_column):
            try:
                if i%2 != 0:
                    out_string += "<td style='text-align:center'  bgcolor='#FFD78C' height='30'>" + str(final_seat[row][i]) + "</td>"
                else:
                    out_string += "<td style='text-align:center' height='30'>" + str(final_seat[row][i]) + "</td>"
            except:
                out_string += "<td>&nbsp;</td>"
        out_string += "</tr>"
    out_string += "</table><br /><br /><br />"
    return out_string
    # 等運算或資料處理結束後, 再將相關值送到對應的 template 進行資料的展示
    #return render_template('optionaction.html', option_list1=option_list1, option_list2=option_list2)
    

@app.route('/fileaxupload', methods=['POST'])
# ajax jquery chunked file upload for flask
def fileaxupload():
    '''
    if not session.get('logged_in'):
        #abort(401)
        return redirect(url_for('login'))
    '''
    # need to consider if the uploaded filename already existed.
    # right now all existed files will be replaced with the new files
    filename = request.args.get("ax-file-name")
    flag = request.args.get("start")
    if flag == "0":
        file = open(data_dir+"downloads/"+filename, "wb")
    else:
        file = open(data_dir+"downloads/"+filename, "ab")
    file.write(request.stream.read())
    file.close()
    return "files uploaded!"

    
    
@app.route('/fileuploadform')
def fileuploadform():
    '''
    if not session.get('logged_in'):
        #abort(401)
        return redirect(url_for('login'))
    '''
    return "<h1>file upload</h1>"+'''
  <script src="/static/jquery.js" type="text/javascript"></script>
  <script src="/static/axuploader.js" type="text/javascript"></script>
  <script>
  $(document).ready(function(){
  $('.prova').axuploader({url:'fileaxupload', allowExt:['jpg','png','gif','7z','pdf','zip','flv','stl','swf'],
  finish:function(x,files)
{
    alert('All files have been uploaded: '+files);
},
  enable:true,
  remotePath:function(){
  return 'downloads/';
  }
  });
  });
  </script>
  <div class="prova"></div>
  <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
  <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
  </section></body></html>
  '''
@app.route('/imageaxupload', methods=['POST'])
# ajax jquery chunked file upload for flask
def imageaxupload():
    '''
    if not session.get('logged_in'):
        #abort(401)
        return redirect(url_for('login'))
    '''
    # need to consider if the uploaded filename already existed.
    # right now all existed files will be replaced with the new files
    filename = request.args.get("ax-file-name")
    flag = request.args.get("start")
    if flag == "0":
        file = open(data_dir+"images/"+filename, "wb")
    else:
        file = open(data_dir+"images/"+filename, "ab")
    file.write(request.stream.read())
    file.close()
    return "image file uploaded!"

    
    
@app.route('/imageuploadform')
def imageuploadform():
    '''
    if not session.get('logged_in'):
        #abort(401)
        return redirect(url_for('login'))
    '''
    return "<h1>file upload</h1>"+'''
  <script src="/static/jquery.js" type="text/javascript"></script>
  <script src="/static/axuploader.js" type="text/javascript"></script>
  <script>
  $(document).ready(function(){
  $('.prova').axuploader({url:'imageaxupload', allowExt:['jpg','png','gif','7z','pdf','zip','flv','stl','swf'],
  finish:function(x,files)
{
    alert('All files have been uploaded: '+files);
},
  enable:true,
  remotePath:function(){
  return 'images/';
  }
  });
  });
  </script>
  <div class="prova"></div>
  <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
  <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
  </section></body></html>
  '''
@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    #return send_from_directory(download_dir, filename=filename, as_attachment=True)
    return send_from_directory(download_dir, filename=filename)
    


# setup static directory
@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory(data_dir+"/images/", path)
# setup static directory
@app.route('/static/')
def send_static():
  return app.send_static_file('index.html')

# setup static directory
@app.route('/static/blog/')
def send_blog():
  return app.send_static_file('blog/index.html')

# setup static directory
@app.route('/static/<path:path>')
def send_file(path):
  return app.send_static_file(static_dir+path)

if __name__ == "__main__":
    app.run()
app.register_blueprint(users.a.g4.ag4_40323138.ag4_40323138)
app.register_blueprint(users.a.g10.ag10_40323141_task1.ag10_40323141)    
app.register_blueprint(users.a.g9.ag9_40323132task.ag9_40323132)
app.register_blueprint(users.a.g10.ag10_40323139.ag10_40323139)
app.register_blueprint(users.a.g5.ag5_40323113task1.ag5_40323113)
app.register_blueprint(users.a.g5.ag5_40323113_gears.a40323113)
app.register_blueprint(users.a.g5.ag5_40123145task1.ag5_40123145)
app.register_blueprint(users.a.g5.ag5_40123145task2.ag5_40123145_2)
app.register_blueprint(users.a.g5.ag5_40123145task3.ag5_40123145_3)
app.register_blueprint(users.a.g8.ag8_40323131_task1.ag8_40323131)
app.register_blueprint(users.a.g4.ag4_40323138_task2bacd.ag4_40323138bacd)
app.register_blueprint(users.a.g4.ag4_40323138_task3abcd.ag4_40323138task3)
app.register_blueprint(users.a.g8.ag8_40323123.ag8_40323123)
app.register_blueprint(users.a.g10.ag10_40323129_task1.ag10_40323129)
app.register_blueprint(users.a.g2.ag2_40323120.ag2_40323120)
app.register_blueprint(users.a.g1.ag1_40323105.ag1_40323105)
app.register_blueprint(users.a.g1.a40223153.ag1_40223153)
app.register_blueprint(users.a.g3.ag3_40323108.ag3_40323108)
app.register_blueprint(users.a.g3.ag3_40323108_task2bacd.ag3_40323108bacd)
app.register_blueprint(users.a.g3.ag3_40323108_task3abcd.ag3_40323108task3)
app.register_blueprint(users.b.g9.bg9_40323250.bg9_40323250)

app.register_blueprint(users.a.g4.ag4_40323109.ag4_40323109)
app.register_blueprint(users.a.g4.ag4_40323109_task2bacd.ag4_40323109bacd)
app.register_blueprint(users.a.g4.ag4_40323109_task3abcd.ag4_40323109task3)
#bg1
app.register_blueprint(users.b.g1.bg1_40123156.bg1_40123156)
app.register_blueprint(users.b.g1.bg1_40123156_2.bg1_40123156_2)

app.register_blueprint(users.b.g1.bg1_40123129.bg1_40123129)
app.register_blueprint(users.b.g1.bg1_40123129_2.bg1_40123129_2)

app.register_blueprint(users.b.g1.bg1_40123144.bg1_40123144)
app.register_blueprint(users.b.g1.bg1_40123144_2.bg40123144)
app.register_blueprint(users.b.g1.b40123131_cdw11.bg1_40123131)
app.register_blueprint(users.b.g1.b40123131_cdw12.bg1)
app.register_blueprint(users.b.g1.b40123131_cdw13.b40123131_cdw13)

app.register_blueprint(users.b.g1.b40123131_cdw11.bg1_40123131)
app.register_blueprint(users.b.g1.b40123131_cdw12.bg1)
app.register_blueprint(users.b.g1.bg1_40123134.bg1_40123134)
app.register_blueprint(users.b.g1.bg1_40123134_2.bg1_40123134_2)
app.register_blueprint(users.b.g1.bg1_40123134_3.bg1_40123134_3)
app.register_blueprint(users.b.g1.b40123133_cdw11.bg1_40123133)
app.register_blueprint(users.b.g1.b40123133_cdw12.bg1_40123133_2)
#app.register_blueprint(users.b.g1.bg1_40123131.bg1_40123131)
#app.register_blueprint(users.b.g1.bg1_40123131_2.bg40123131)

app.register_blueprint(users.b.g1.bg1_40123126.bg1_40123126)
app.register_blueprint(users.b.g1.bg1_40123126_2.bg1_40123126_2)

#bg2
app.register_blueprint(users.b.g2.bg2_40123235.bg2_40123235)
app.register_blueprint(users.b.g2.bg2_40123202.bg2_40123202)
app.register_blueprint(users.b.g2.bg2_40123235_cdw12.b40123235)

app.register_blueprint(users.b.g2.bg2_40123202_cdw13.b40123202)
app.register_blueprint(users.b.g2.bg2_40123202_cdw14.bg2_40123202_cdw14)
app.register_blueprint(users.b.g2.bg2_40123235_cdw14.b40123235_1)
#app.register_blueprint(users.b.g2.bg2_40123202_1.b40123202)
app.register_blueprint(users.b.g2.bg2_40123226_cdw12.b40123226)
app.register_blueprint(users.b.g2.bg2_40123232_cdw12.b40123232)
app.register_blueprint(users.b.g2.bg2_40123214_cdw12.b40123214)
app.register_blueprint(users.b.g2.bg2_40123217_cdw12.b40123217)
app.register_blueprint(users.b.g2.bg2_40123244_cdw12.b40123244)
#bg4
app.register_blueprint(users.b.g4.bg4_40323203.bg4_40323203)
app.register_blueprint(users.b.g4.bg4_40323205.bg4_40323205)
app.register_blueprint(users.b.g4.bg4_40323208.bg4_40323208)
#bg8
app.register_blueprint(users.b.g8.bg8_40323213.bg8_40323213)
app.register_blueprint(users.b.g4.bg4_40323202.bg4_40323202)
app.register_blueprint(users.b.g4.b40323201_cdw11.b40323201)
app.register_blueprint(users.b.g4.bg4_40123128.bg4_40123128)
app.register_blueprint(users.b.g4.bg4_40123128_cdw11.b40123128)
app.register_blueprint(users.b.g4.bg4_40123128_cdw14.b40123128_1)
#bg5
app.register_blueprint(users.b.g5.b40323204_cdw11_1.bg5_40323204_1)
app.register_blueprint(users.b.g5.b40323204_cdw11_2.bg5_40323204_2)
app.register_blueprint(users.b.g5.b40323204_cdw11.bg5_40323204)
#app.register_blueprint(users.b.g5.b40323206_cdw11_1.bg5_40323206_1)
app.register_blueprint(users.b.g5.b40323206_cdw11_2.bg5_40323206_2)
#bg11
app.register_blueprint(users.b.g11.bg11_40323245.bg11_40323245)
app.register_blueprint(users.b.g11.bg11_40323252.bg11_40323252)
#app.register_blueprint(users.b.g11.bg11.bg11_40323245_1)
#app.register_blueprint(users.b.g11.bg11_40323245_1.bg11)
app.register_blueprint(users.b.g11.b40323252.bg11_1)

#app.register_blueprint(users.b.g11.bg11.bg11_40323245_1)

#app.register_blueprint(users.b.g11.bg11_40323245_1.bg11)
app.register_blueprint(users.b.g11.b40323252.bg11_1)
#bg101
app.register_blueprint(users.b.g101.b40123200.bg101)

#ag7
app.register_blueprint(users.a.g7.ag7_40123149_1.ag7_40123149_1)
app.register_blueprint(users.a.g7.ag7_40123149_2.ag7_40123149_2)
#ag8
#app.register_blueprint(users.a.g8.a40323143.ag8_40323143)
app.register_blueprint(users.a.g8.a40323137.ag8_40323137)
app.register_blueprint(users.a.g8.a40323154.ag8_40323154)
#ag10
app.register_blueprint(users.a.g10.a40323139.ag10_40323139_1)
#app.register_blueprint(users.a.g10.a40323141.ag10_40323141_1)
#ag3
app.register_blueprint(users.a.g3.a40323108.ag3_40323108_1)
#ag100
app.register_blueprint(users.a.g100.cdw13.a40123100.ag100)

#bg3
#app.register_blueprint(users.b.g3.bg3_40123224.bg3_40123224)
#app.register_blueprint(users.b.g3.bg3_.bg3_40123250)
#app.register_blueprint(users.b.g3.bg3_40123250.bg3_40123242)
app.register_blueprint(users.b.g3.bg3_40123224_cdw11.b40123224)
app.register_blueprint(users.b.g3.bg3_40123250.bg3_40123250)
app.register_blueprint(users.b.g3.bg3_40123250_cdw11.b40123250)
#app.register_blueprint(users.b.g3.bg3_40123250.bg3_40123242)
app.register_blueprint(users.b.g3.bg3_40123242_cdw12.b40123242)
app.register_blueprint(users.b.g3.bg3_40123250_cdw14.b40123250_1)
app.register_blueprint(users.b.g3.bg3_40123224_cdw14.b40123224_1)



