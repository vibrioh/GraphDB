import logging
import rest_apis as r

if __name__ == '__main__':

    user_name = 'HW3_test' 
    data_conf_name = 'data'
    data_content = {
	#When you use your own data. Please just change the file name here
	#for example '/opt/graphen.ai/ml/data/your_own_data.csv'
        'locations': ['/opt/graphen.ai/ml/data/movie_three.csv'],
        'test_percent': 0.25,
        'scaler': 'StandardScaler'
    }

    print r.data(user_name, data_conf_name, data_content)
    #
    # # Modelx
    trainer = 'SVMC'
    model_conf_name = 'model_config'
    model_content = \
    {
         'params_to_tune': {'C': [1, 2, 3]},
         'params_to_provide': {},
         'cv_score': 'accuracy',
         'pred_score': [{'metric': 'accuracy'}]
    }
    print r.model(user_name, trainer, model_conf_name, model_content)
    # # Train
    model_name = 'model_test'
    print r.train(user_name, data_conf_name, model_conf_name, model_name)
    # same as training data, only change file's name in this file path
    #for example /opt/graphen.ai/ml/data/your_own_data_predict.csv
    file_path = '/opt/graphen.ai/ml/data/movie_three_predict.csv'
    output_path = '${MLDATAPATH}/output.csv'
    
    print r.predict(user_name, model_name, file_path, output_path)

