import flask.json
import requests
import matplotlib.pyplot as plt
from flask import Flask
from flask import render_template, request, jsonify, make_response
from flask_json import FlaskJSON, JsonError, json_response
from matplotlib.figure import Figure

app = Flask(__name__)
json = FlaskJSON(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/karlsruhe', methods=['GET'])
def k_data():
    url = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID={}%20&outFields=OBJECTID,%20GEN,%20BEZ,%20BL,%20cases,%20deaths,%20cases_per_population,%20cases7_per_100k,%20cases7_lk,%20death7_lk,%20cases7_bl_per_100k,%20cases7_bl,%20death7_bl,last_update&outSR=4326&f=pjson'
    city_id = '193'
    r = requests.get(url.format(city_id)).json()

    name = r['objectIdFieldName']
    print(name)
    city = r['features'][0]['attributes']['GEN']
    print(city)

    data = {
        'city': r['features'][0]['attributes']['GEN'],
        'bez': r['features'][0]['attributes']['BEZ'],
        'state': r['features'][0]['attributes']['BL'],
        'cases': r['features'][0]['attributes']['cases'],
        'deaths': r['features'][0]['attributes']['deaths'],
        'cases_per_population': r['features'][0]['attributes']['cases_per_population'],
        'cases7_per_100k': r['features'][0]['attributes']['cases7_per_100k'],
        'cases7_lk': r['features'][0]['attributes']['cases7_lk'],
        'death7_lk': r['features'][0]['attributes']['death7_lk'],
        'cases7_bl_per_100k': r['features'][0]['attributes']['cases7_bl_per_100k'],
        'cases7_bl': r['features'][0]['attributes']['cases7_bl'],
        'death7_bl': r['features'][0]['attributes']['death7_bl'],
        'last_update': r['features'][0]['attributes']['last_update']
    }

    print(data)

    json_object = flask.json.dumps(data, indent=4)
    print(json_object)

    def write_json(new_data, filename='karlsruhe_data.json'):
        with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
            print(file_data)
            lines = 0
            for i in file_data["Karlsruhe"]:
                lines += 1
            check = file_data["Karlsruhe"][lines - 1]["last_update"]
            if check == timeu:
                print(check)
                pass
            else:
                file_data["Karlsruhe"].append(y)
                print(file_data)
                file.seek(0)
                flask.json.dump(file_data, file, indent=4)

    cases = data["cases7_lk"]
    death = data["death7_lk"]
    timeu = data["last_update"]
    y = {"cases7_lk": cases, "death7_lk": death, "last_update": timeu}
    write_json(y)

    def chart():
        filename = 'karlsruhe_data.json'
        with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
        lines = 0
        for i in file_data["Karlsruhe"]:
            lines += 1

        for j in range(0, lines):
            cases_k = file_data["Karlsruhe"][j]["cases7_lk"]
            y_data_k.append(cases_k)
            time_l = file_data["Karlsruhe"][j]["last_update"]
            time_l = time_l.split(", ")
            x_data_k.append(time_l[0])

        name_img_1 = 'static/karlsruhe.png'
        fig = plt.figure()
        plt.xlabel('date')
        plt.ylabel('incidents7_lk')
        plt.plot(x_data_k, y_data_k)
        fig.savefig(name_img_1,format='png')


    y_data_k = []
    x_data_k = []
    chart()

    def safe():
        total_inc = data["cases7_per_100k"]
        if total_inc < 100:
            msg = "Finally some relief. Schools & restaurants can reopen"
        else:
            msg= "Cases increses again, Night curfew may impose"
        return msg
    msg = safe()

    return render_template('corona.html', data=data, chart1="Karlsruhe Plot", msg=msg)

@app.route('/pforzheim', methods=['GET'])
def p_data():
    url = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID={}%20&outFields=OBJECTID,%20GEN,%20BEZ,%20BL,%20cases,%20deaths,%20cases_per_population,%20cases7_per_100k,%20cases7_lk,%20death7_lk,%20cases7_bl_per_100k,%20cases7_bl,%20death7_bl,last_update&outSR=4326&f=pjson'
    city_id = '200'
    r = requests.get(url.format(city_id)).json()

    name = r['objectIdFieldName']
    print(name)
    city = r['features'][0]['attributes']['GEN']
    print(city)

    data = {
        'city': r['features'][0]['attributes']['GEN'],
        'bez': r['features'][0]['attributes']['BEZ'],
        'state': r['features'][0]['attributes']['BL'],
        'cases': r['features'][0]['attributes']['cases'],
        'deaths': r['features'][0]['attributes']['deaths'],
        'cases_per_population': r['features'][0]['attributes']['cases_per_population'],
        'cases7_per_100k': r['features'][0]['attributes']['cases7_per_100k'],
        'cases7_lk': r['features'][0]['attributes']['cases7_lk'],
        'death7_lk': r['features'][0]['attributes']['death7_lk'],
        'cases7_bl_per_100k': r['features'][0]['attributes']['cases7_bl_per_100k'],
        'cases7_bl': r['features'][0]['attributes']['cases7_bl'],
        'death7_bl': r['features'][0]['attributes']['death7_bl'],
        'last_update': r['features'][0]['attributes']['last_update']
    }

    print(data)
    json_object = flask.json.dumps(data, indent=4)
    print(json_object)

    def write_json_p(new_data, filename='pforzheim_data.json'):
        with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
            print(file_data)
            lines = 0
            for i in file_data["Pforzheim"]:
                lines += 1
            check = file_data["Pforzheim"][lines-1]["last_update"]
            if check == timeu:
                print(check)
                pass
            else:
                file_data["Pforzheim"].append(y)
                print(file_data)
                file.seek(0)
                flask.json.dump(file_data, file, indent=4)

    cases = data["cases7_lk"]
    death = data["death7_lk"]
    timeu = data["last_update"]
    y = {"cases7_lk": cases, "death7_lk": death, "last_update": timeu}

    write_json_p(y)

    def chart_p():
        filename = 'pforzheim_data.json'
        with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
        lines = 0
        for i in file_data["Pforzheim"]:
            lines += 1

        for j in range(0, lines):
            cases_k = file_data["Pforzheim"][j]["cases7_lk"]
            y_data_k.append(cases_k)
            time_l = file_data["Pforzheim"][j]["last_update"]
            time_l = time_l.split(", ")
            x_data_k.append(time_l[0])

        name_img_1 = 'static/pforzheim.png'
        fig = plt.figure()
        plt.xlabel('date')
        plt.ylabel('incidents7_lk')
        plt.plot(x_data_k, y_data_k)
        fig.savefig(name_img_1, format='png')

    y_data_k = []
    x_data_k = []
    chart_p()

    def safe():
        total_inc = data["cases7_per_100k"]
        if total_inc < 100:
            msg = "Finally some relief. Schools & restaurants can reopen"
        else:
            msg= "Cases increses again, Night curfew may impose"
        return msg
    msg = safe()

    return render_template('pro.html', data=data, chart1="Pforzheim Plot", msg=msg)

@app.route('/stuttgart', methods=['GET'])
def s_data():
    url = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID={}%20&outFields=OBJECTID,%20GEN,%20BEZ,%20BL,%20cases,%20deaths,%20cases_per_population,%20cases7_per_100k,%20cases7_lk,%20death7_lk,%20cases7_bl_per_100k,%20cases7_bl,%20death7_bl,last_update&outSR=4326&f=pjson'
    city_id = '179'
    r = requests.get(url.format(city_id)).json()

    name = r['objectIdFieldName']
    print(name)
    city = r['features'][0]['attributes']['GEN']
    print(city)

    data = {
        'city': r['features'][0]['attributes']['GEN'],
        'bez': r['features'][0]['attributes']['BEZ'],
        'state': r['features'][0]['attributes']['BL'],
        'cases': r['features'][0]['attributes']['cases'],
        'deaths': r['features'][0]['attributes']['deaths'],
        'cases_per_population': r['features'][0]['attributes']['cases_per_population'],
        'cases7_per_100k': r['features'][0]['attributes']['cases7_per_100k'],
        'cases7_lk': r['features'][0]['attributes']['cases7_lk'],
        'death7_lk': r['features'][0]['attributes']['death7_lk'],
        'cases7_bl_per_100k': r['features'][0]['attributes']['cases7_bl_per_100k'],
        'cases7_bl': r['features'][0]['attributes']['cases7_bl'],
        'death7_bl': r['features'][0]['attributes']['death7_bl'],
        'last_update': r['features'][0]['attributes']['last_update']
    }

    print(data)
    json_object = flask.json.dumps(data, indent=4)
    print(json_object)

    def write_json_s(new_data, filename='stuttgart_data.json'):
        with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
            print(file_data)
            lines = 0
            for i in file_data["Stuttgart"]:
                lines += 1
            check = file_data["Stuttgart"][lines-1]["last_update"]
            if check == timeu:
                print(check)
                pass
            else:
                file_data["Stuttgart"].append(y)
                print(file_data)
                file.seek(0)
                flask.json.dump(file_data, file, indent=4)

    cases = data["cases7_lk"]
    death = data["death7_lk"]
    timeu = data["last_update"]
    y = {"cases7_lk": cases, "death7_lk": death, "last_update": timeu}

    write_json_s(y)

    def chart_s():
        filename = 'stuttgart_data.json'
        with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
        lines = 0
        for i in file_data["Stuttgart"]:
            lines += 1

        for j in range(0, lines):
            cases_k = file_data["Stuttgart"][j]["cases7_lk"]
            y_data_k.append(cases_k)
            time_l = file_data["Stuttgart"][j]["last_update"]
            time_l = time_l.split(", ")
            x_data_k.append(time_l[0])

        name_img_1 = 'static/stuttgart.png'
        fig = plt.figure()
        plt.xlabel('date')
        plt.ylabel('incidents7_lk')
        plt.plot(x_data_k, y_data_k)
        fig.savefig(name_img_1, format='png')

    y_data_k = []
    x_data_k = []
    chart_s()

    def safe():
        total_inc = data["cases7_per_100k"]
        if total_inc < 100:
            msg = "Finally some relief. Schools & restaurants can reopen"
        else:
            msg= "Cases increses again, Night curfew may impose"
        return msg
    msg = safe()

    return render_template('stu.html', data=data, chart1="Stuttgart Plot", msg=msg)

@app.route('/history_stuttgart', methods=['GET'])
def tableS():
    filename = 'stuttgart_data.json'
    with open(filename, 'r+') as file:
        file_data = flask.json.load(file)
        print(file_data)
    lines = 0
    for i in file_data["Stuttgart"]:
        lines += 1
    cases = []
    death = []
    last_update = []
    for j in range(0, lines):
        cases_value =file_data["Stuttgart"][j]["cases7_lk"]
        cases.append(cases_value)
        death_value = file_data["Stuttgart"][j]["death7_lk"]
        death.append((death_value))
        last_update_value = file_data["Stuttgart"][j]["last_update"]
        last_update.append(last_update_value)

    return render_template('table.html', cases=cases, death=death, update=last_update)

@app.route('/history_karlsruhe', methods=['GET'])
def tableK():
    filename = 'karlsruhe_data.json'
    with open(filename, 'r+') as file:
        file_data = flask.json.load(file)
        print(file_data)
    lines = 0
    for i in file_data["Karlsruhe"]:
        lines += 1
    cases = []
    death = []
    last_update = []
    for j in range(0, lines):
        cases_value =file_data["Karlsruhe"][j]["cases7_lk"]
        cases.append(cases_value)
        death_value = file_data["Karlsruhe"][j]["death7_lk"]
        death.append((death_value))
        last_update_value = file_data["Karlsruhe"][j]["last_update"]
        last_update.append(last_update_value)

    return render_template('table.html', cases=cases, death=death, update=last_update)

@app.route('/history_pforzheim', methods=['GET'])
def tableP():
    filename = 'pforzheim_data.json'
    with open(filename, 'r+') as file:
        file_data = flask.json.load(file)
        print(file_data)
    lines = 0
    for i in file_data["Pforzheim"]:
        lines += 1
    cases = []
    death = []
    last_update = []
    for j in range(0, lines):
        cases_value =file_data["Pforzheim"][j]["cases7_lk"]
        cases.append(cases_value)
        death_value = file_data["Pforzheim"][j]["death7_lk"]
        death.append((death_value))
        last_update_value = file_data["Pforzheim"][j]["last_update"]
        last_update.append(last_update_value)

    return render_template('table.html', cases=cases, death=death, update=last_update)

if __name__ == '__main__':
    app.run()
