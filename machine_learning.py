import numpy as np
import pandas as pd
import pickle
from sklearn import svm
from sklearn.model_selection import train_test_split

def train():
    X = pd.read_csv("File/LoanData_X.csv")
    y = pd.read_csv("File/LoanData_Y.csv")

    clf = svm.SVC(kernel="linear")
    clf.fit(X,y)
    with open("File/SVM.pickle",'wb') as f:
        pickle.dump(clf,f)

def test(Dependents,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Male,NotGraduate,Semiurban,Urban,Married,Self_Employed):
    with open("File/SVM.pickle",'rb') as f:
        clf = pickle.load(f)
    y_pred = clf.predict([np.array([Dependents,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Male,NotGraduate,Semiurban,Urban,Married,Self_Employed])])
    return y_pred

