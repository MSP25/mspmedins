import json

import numpy as np
import pickle
import json
import numpy as np
import config

class MedicalInsurance:
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+region

    def load_data(self):
        with open (config.MODEL_PATH,'rb')as f:
            self.model=pickle.load(f)

        with open(config.PROJECT_DATA_PATH,'r') as f1:
            self.json_data=json.load(f1)

    def get_charges_insurance(self):
        self.load_data()
        test_array=np.zeros(len(self.json_data["column"]))
        
        test_array[0]=self.age
        test_array[1]=self.json_data["sex"][self.sex]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data["smoker"][self.smoker]
        
        region_index = self.json_data['column'].index(self.region)
        test_array[region_index]=1

        print(test_array)

        predicted_charge= np.around(   self.model.predict([test_array])[0]   , 2)
        return predicted_charge



if __name__ == "__main__":

    age  = 19
    sex  = 'male'
    bmi  = 25 
    children = 2
    smoker = 'yes'
    region = 'southwest'


    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    print(med_ins.get_charges_insurance())

