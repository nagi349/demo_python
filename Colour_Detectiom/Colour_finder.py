import pandas as pd
import numpy as np
import cv2
index=["color", "color_name", "hex", "R", "G", "B"]
colour_label=pd.read_csv('colors.csv', names=index , header= None)

#  Color Recognition Function
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(colour_label)):
        d = abs(R- int(colour_label.loc[i,"R"])) + abs(G- int(colour_label.loc[i,"G"]))+ abs(B- int(colour_label.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = colour_label.loc[i,"color_name"]
    return cname


