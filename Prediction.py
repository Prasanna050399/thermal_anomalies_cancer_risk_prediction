from keras.models import load_model
import numpy as np

class Prediction:
        def __init__(self):
                self.model = load_model("90_90_model.h5")
                #self.model = load_model("90_65_cv_model.h5") ##
        def predict(self, arr):
                arr = [arr]
                #arr = np.array(arr) ##
                prediction = self.model.predict(arr)
                observation = round(prediction[0][0])
                if observation == 0:
                        observation = "Negative Breast Mass Characteristics"
                else:
                        observation = "Positive Breast Mass Characteristics"
                confidence = abs(prediction[0][0] - 0.5) * 2 * 100
                return [observation, str(confidence)]


##if __name__ == "__main__":
##        obj = Prediction()
##        X = []
##        y = []
##
##        '''
##        data = open("vectors.txt", "r")
##        data = data.readlines()
##        for entry in data:
##                entry = entry.strip()
##                entry = entry.split()
##                entry = [float(num) for num in entry]
##                X.append(entry[1:])
##                y.append(entry[0])
##        '''
##        
##        
##        data = open("training.txt", "r")
##        data = data.readlines()
##        for entry in data:
##                entry = entry.strip()
##                entry = entry.split()
##                entry = [float(num) for num in entry]
##                X.append(entry[1:])
##                y.append(entry[0])
##
##        
##        
##        testingdata = open("testing.txt", "r")
##        testingdata = testingdata.readlines()
##        for entry in testingdata:
##                entry = entry.strip()
##                entry = entry.split()
##                entry = [float(num) for num in entry]
##                X.append(entry[1:])
##                y.append(entry[0])
##
##        
##        count = 0
##        print("         Expected                                 Observed                         Confidence")
##        for i in range(len(X)):
##                expected = "Positive Breast Mass Characteristics"
##                if y[i] == 0:
##                        expected = "Negative Breast Mass Characteristics"
##                observed, confidence = obj.predict(X[i])
##                #print("Expected: ", y[i], "      Observed: ", res)
##                print(expected, "    ", observed, "  ", confidence, "%")
##                if observed == expected:
##                        count += 1
##        print("\nAccuracy: ", count/len(X)*100, "%")

