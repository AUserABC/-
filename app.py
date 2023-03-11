import string

from flask import Flask
from flask import jsonify
from flask import render_template
from jieba.analyse import extract_tags

import utils

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("main1.html")

@app.route('/tem')
def hello_world3():  # put application's code here
    return render_template("index.html")

@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

@app.route('/c2')
def get_c2_data():
    res = []
    print(res)
    data = utils.get_c2_data()
    for tup in data:
        print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})


@app.route('/l1')
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead=[],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})



    data = utils.get_c2_data()
    for tup in data:
        print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})


@app.route('/l21')
def get_l21_data():
        data = utils.get_l21_data()
        script = []
        mName = []
        mName.append(['score', 'amount', 'product','script'])
        start1 = data[0][0].rstrip(string.digits)
        start = data[0][0][len(start1):]  # 数字部分
        for i in data:
            d = []
            k = i[0].rstrip(string.digits)  # 文字部分
            print(k)
            v = i[0][len(k):]  # 数字部分
            k, s = k.split()  # k热词 s描述
            d.append(int(v)/int(start) * 100)
            d.append(int(v))
            d.append(k)
            d.append(s)
            mName.append(d)
            # script.append(s)
        print(mName)
        return jsonify({"source":mName});

@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    day,confirm_add,suspect_add=[],[],[]
    for a,b,c in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day":day,"confirm_add":confirm_add,"suspect_add":suspect_add})

@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        print(k)
        print(v)
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city":city,"confirm":confirm});

@app.route('/r2')
def get_r2_data():
    data = utils.get_r2_data()
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)#文字部分
        print(k)
        v = i[0][len(k):]#数字部分
        k,s = k.split() #k热词 s描述
        ks = extract_tags(k)
        d.append({"name": k, "value": v, "script": s})
        # for j in ks:
        #     if not j.isdigit():
        #         d.append({"name":j,"value":v,"script":s})
    return jsonify({"kws":d})

@app.route('/time')
def get_time():
    return utils.get_time()


if __name__ == '__main__':
    app.run()
    get_r1_data()


