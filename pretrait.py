from glob import glob
import os
# from scripts.Evaluation import Evaluation
# from scripts.Predict import Predict
from Evaluation import Evaluation
import spacy
predicted = []
expected = []

nlp=spacy.load('en_core_web_sm')
from Predict_V4 import Predict

def getFile(fic,pol):
    x = 0
    for f in glob(fic+'/*') :
        x += 1
        os.system(f'mv {f} {pol}/')
        if x == 500 :

            break


def getcontentlabel(file) :

    expect = ''
    if 'pos' in file :
        expect = 'pos'
    else :
        expect = 'neg'

    return open(file).read(),expect


def prediction(file,expect) :


    pred = Predict(file,nlp)
    pred.predict()
    predicted.append(pred.predicted)
    expected.append(expect)


if __name__ == '__main__':


    for fic in glob('./txt_sentoken/*/*.txt') :
        # print(fic)
        file, label = getcontentlabel(fic)
        # print(file)
        # print(label)

        prediction(file,label)


    #print(len(predicted))
    #print(len(expected))

    eval = Evaluation(expected,predicted)


    print(eval.getVraisPos())
    print(eval.getFauxNeg())
    print(eval.getFauxPos())
    print(eval.f_mesure())
