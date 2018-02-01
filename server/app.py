from flask import Flask, render_template
import requests
import yaml
import json

app = Flask(__name__)

# Read config
with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

api_key = cfg['philips_hue']['bridge']['api_key']
hue_ip = cfg['philips_hue']['bridge']['ip']
entrance_lights_ids = cfg['philips_hue']['rooms']['entrance']
living_room_lights_ids = cfg['philips_hue']['rooms']['living_room']
study_lights_ids = cfg['philips_hue']['rooms']['study']


def switch_lights(ids, status):
    """
    Switch lights on/off by ids
    :param ids: ids of Philips Hue lights
    :param status: 0 for off, 1 for on
    :return:
    """
    if status == '1':
        # turn lights on
        for i in ids:
            url = 'http://{}/api/{}/lights/{}/state'.format(hue_ip, api_key, i)
            body = cfg['philips_hue']['lights'][i]
            body.update({"on": True})

            requests.put(url, data=json.dumps(body))

    elif status == '0':
        # turn lights off
        for i in ids:
            url = 'http://{}/api/{}/lights/{}/state'.format(hue_ip, api_key, i)
            body = {"on": False}

            requests.put(url, data=json.dumps(body))


@app.route('/')
def index():
    return 'Hello world'


@app.route('/my_home/entrance_lights/<value>')
def entrance_lights(status):
    switch_lights(entrance_lights_ids, status)
    return render_template('entrance.html', value=status)


@app.route('/my_home/living_room_lights/<value>')
def living_room_lights(status):
    switch_lights(living_room_lights_ids, status)
    return render_template('entrance.html', value=status)


@app.route('/my_home/study_lights/<value>')
def study_lights(status):
    switch_lights(study_lights_ids, status)
    return render_template('study.html', value=status)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
