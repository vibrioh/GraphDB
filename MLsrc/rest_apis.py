import requests
import shutil
import json

URL = 'http://localhost:8020/'

def data(user_name, data_conf_name, data_content):
    dataURL = URL + 'data_conf?' + 'conf_name={0}'.format(data_conf_name)
    headers = {'X-Graphen-User': user_name}
    param = {'param': json.dumps(data_content)}


    r = requests.post(dataURL, data=param, files=None, headers=headers)
    return r.json()

def model(user_name, trainer, model_conf_name, model_content):

    modelURL = URL + 'model_conf?' + 'conf_name={0}&trainer={1}'.\
        format(model_conf_name, trainer)

    param = {'param': json.dumps(model_content)}
    headers = {'X-Graphen-User': user_name}
    r = requests.post(modelURL, data=param, files=None, headers=headers)
    return r.json()


def train(user_name, data_conf_name, model_conf_name, model_name, workers=1):
    trainURL = URL + 'train?' + 'data_conf_name={0}&model_conf_name={1}&model_name={2}&workers={3}'.\
        format( data_conf_name, model_conf_name, model_name, workers)
    headers = {'X-Graphen-User': user_name}
    r = requests.post(trainURL,  headers=headers)
    return r.json()


def predict(user_name, model_name, file_path, output_path):
    predictURL = URL + 'predict?' + 'user_name={0}&model_name={1}&file_path={2}'.format(user_name, model_name, file_path)
    r = requests.get(predictURL, stream=True)
    if r.status_code == 200:
        try:
            with open(output_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

        except Exception as error:
            return error.message
    else:
        return 'error'
