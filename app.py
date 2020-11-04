from flask import Flask, render_template, url_for, request, redirect, Response
import random, json
from AG import AGFunction

app = Flask(__name__)
data1 = []
MAX_WEIGHT=0
MAX_VOLUME=0
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/valider', methods=['POST'])
def valider():
    jsdata = request.form['javascript_data']
    jada = json.loads(jsdata)[0]
    MAX_WEIGHT=int(jada['p_max'])
    MAX_VOLUME=int(jada['v_max'])
    data = []
    for i in data1:
        data.append((int(i['poids']), int(i['volume']), int(i['priorite'])))
    return str(Retourner(AGFunction(data,MAX_WEIGHT,MAX_VOLUME))),200
@app.route('/receiver', methods=['POST'])
def worker():
    jsdata = request.form['javascript_data']
    jada = json.loads(jsdata)[0]
    data1.append(jada)
    return "Added",200

def Retourner(result):
    print(result)
    final_tab=[]
    c = 0
    (l,j) = result
    for i in j:
        if i == 1:
            final_tab.append(data1[c])
        c = c+1
    jsonR = json.dumps(final_tab)
    return jsonR




if __name__ == '__main__':
    app.run(debug=True)