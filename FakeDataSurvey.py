from selenium import webdriver
import time
import random
import numpy
from numpy.random import choice

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
web = webdriver.Chrome(options=options)
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfgteOa9-PJ4OtjSqNDkZtLIa_4HTTVTbhwI52pM_4aznvT3Q/viewform?usp=sf_link')
time.sleep(0.8)


age = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')]

sex = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')]

job = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
]

income = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div')
]

sq1 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

sq2 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

sq3 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]')
]

sa1 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]')
]

sa2 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

sa3 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

tru1 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

tru2 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

tru3 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

cm1 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

cm2 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

cm3 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

lo1 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

lo2 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

lo3 = [
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div'),
    web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
]

submit = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')

#again = web.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')

def rand_click(arr,po):
 random = choice(arr,1,p=po)
 random[0].click()
 time.sleep(0.02)

testin = [age,sex,job,income,sq1,sq2,sq3,sa1,sa2,sa3,tru1,tru2,tru3,cm1,cm2,cm3,lo1,lo2,lo3]


p = [[0.02, 0.93, 0.05],
     [0.44, 0.53, 0.03],
     [0.8, 0.09, 0.03, 0.07 , 0.01],
     [0.10, 0.5, 0.1, 0.1, 0.1, 0.1],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.05, 0.05, 0.05, 0.25, 0.6],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.05, 0.05, 0.05, 0.25, 0.6],
     [0.05, 0.05, 0.05, 0.25, 0.6],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.01, 0.01, 0.03, 0.04, 0.91],
     [0.1, 0.01, 0.36, 0.03, 0.5],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.03, 0.01, 0.01, 0.11, 0.84],
     [0.03, 0.01, 0.01, 0.11, 0.84]]



[rand_click(x, y) for x, y in zip(testin, p)]
submit.click()
time.sleep(0.3)
web.close()

#again.click()
