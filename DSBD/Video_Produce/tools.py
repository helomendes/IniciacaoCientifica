import json
import cv2 as cv
from datetime import datetime, timedelta

class Colors:
    def __init__(self):
        self.black = (0, 0, 0)
        self.blue = (255, 153, 51)
        self.light_red = (153, 153, 255)
        self.red = (50, 50, 255)
        self.white = (255, 255, 255)
        self.use = self.black

# Prepares the given json to be in a more suited format for the program
def prepPred(pred):
    with open(pred, 'r') as file:
        pred = json.load(file)
    new = {}
    for num in pred:
        for name in pred[num]:
            if name not in new:
                new[name] = {}
            new[name][pred[num][name]['annotation']['id']] = pred[num][name]
    return new

# Calculates the bounding box's center
def calcCenter(bbox):
    bbox = [int(x) for x in bbox]
    x, y, w, h = bbox
    x = x + (w//2)
    y = y + (h//2)
    return (x, y)

# Returns a formated string HOUR:MINUTES
def formatTime(time):
    if isinstance(time, timedelta):
        hr = time.seconds // 3600
        mn = (time.seconds % 3600) // 60
    else:
        hr = time[0]
        mn = time[1]
    if hr < 10:
        hr = f'0{hr}'
    if mn < 10:
        mn = f'0{mn}'
    str_time = f'{hr}:{mn}'
    return str_time

# Returns a datetime object
def getTime(name):
    name_ = name.split('_')
    date = name_[0]
    date = [int(i) for i in date.split('-')]
    if len(name_) > 2:
        hr = name_[1]
        mn = name_[2]
        time = [int(hr), int(mn)]
    else:
        time = name_[-1]
        time = [int(time[0:2]), int(time[2:4])]
    date = datetime(date[0], date[1], date[2], time[0], time[1])
    return time, date

# Sets color to be used based on the time spent
def setColor(max_diff, diff, colors):
    piece = max_diff // 3 
    if diff < piece:
        colors.use = colors.blue
    elif diff >= piece and diff < piece*2:
        colors.use = colors.light_red
    else:
        colors.use = colors.red

# Edit each image from a day for the video
def makeDay(imgs, imgs_keys, pred, vidWriter):
    _, min_date = getTime(imgs_keys[0])
    _, max_date = getTime(imgs_keys[-1])
    max_diff = max_date - min_date

    id_dict = {}
    for key in imgs_keys: 
        time, img_date = getTime(key)
        diff = timedelta(0)
        if key not in pred:
            continue
        for a in pred[key]:
            pred_id = pred[key][a]['predicted_car_id']
            if pred_id:
                if pred_id not in id_dict:
                    id_dict[pred_id] = {'start': img_date, 'end': img_date}
                else:
                    if img_date >= id_dict[pred_id]['start']:
                        id_dict[pred_id]['end'] = img_date
                    else:
                        id_dict[pred_id]['start'] = img_date
                diff = id_dict[pred_id]['end']-id_dict[pred_id]['start']
                txt = formatTime(diff)
            else:
                txt = ' '

            fontF = cv.FONT_HERSHEY_DUPLEX
            fontS = 0.45
            line = cv.LINE_AA
            x, y = calcCenter(pred[key][a]['annotation']['bbox'])
            txt_size = cv.getTextSize(txt, fontF, fontS, 3)
            x -= txt_size[0][0]//2
            y -= txt_size[0][1]//2
            colors = Colors()
            cv.putText(imgs[key], txt, (x, y), fontF, fontS, colors.black, 3, line)
            setColor(max_diff, diff, colors)
            cv.putText(imgs[key], txt, (x, y), fontF, fontS, colors.use, 1, line)

            fontF = cv.FONT_HERSHEY_SIMPLEX
            fontS = 1.5
            line = cv.LINE_AA
            h, w, l = imgs[key].shape
            size = cv.getTextSize(formatTime(time), fontF, fontS, 2)
            cv.putText(imgs[key], formatTime(time), (w-size[0][0]-10, size[0][1]+10), fontF, fontS, colors.black, 4, line)
            cv.putText(imgs[key], formatTime(time), (w-size[0][0]-10, size[0][1]+10), fontF, fontS, colors.white, 2, line)

        vidWriter.write(imgs[key])
