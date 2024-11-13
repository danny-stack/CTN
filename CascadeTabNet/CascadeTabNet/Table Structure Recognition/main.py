from border import border
from mmdet.apis import inference_detector, init_detector
#from mmdet.apis import show_result_pyplot as show_result
import cv2
from Functions.blessFunc import borderless
import lxml.etree as etree
import glob

############ To Do ############
image_path = './Code_test/images/test_image.jpg'
xmlPath = './Code_test/xmlPath/output.xml'

config_fname = './Code_test/configs/your_config_file.py'
checkpoint_path = './Code_test/checkpoints/your_checkpoint_file.pth'
epoch = './Code_test/epoch'
##############################


model = init_detector(config_fname, checkpoint_path+epoch)

# List of images in the image_path
imgs = glob.glob(image_path)
for i in imgs:
    result = inference_detector(model, i)
    res_border = []
    res_bless = []
    res_cell = []
    root = etree.Element("document")
    ## for border
    for r in result[0][0]:
        if r[4]>.85:
            res_border.append(r[:4].astype(int))
    ## for cells
    for r in result[0][1]:
        if r[4]>.85:
            r[4] = r[4]*100
            res_cell.append(r.astype(int))
    ## for borderless
    for r in result[0][2]:
        if r[4]>.85:
            res_bless.append(r[:4].astype(int))

    ## if border tables detected 
    if len(res_border) != 0:
        ## call border script for each table in image
        for res in res_border:
            try:
                root.append(border(res,cv2.imread(i)))  
            except:
                pass
    if len(res_bless) != 0:
        if len(res_cell) != 0:
            for no,res in enumerate(res_bless):
                root.append(borderless(res,cv2.imread(i),res_cell))

    myfile = open(xmlPath+i.split('/')[-1][:-3]+'xml', "w")
    myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    myfile.write(etree.tostring(root, pretty_print=True,encoding="unicode"))
    myfile.close()