import cv2 as cv
import argparse
import os
import yaml
import tools
from tqdm import tqdm
from glob import glob

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Configuration file', required=True)
    args = parser.parse_args()
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    imgs_path = config.get('images_dir')
    out_path = config.get('output_dir')
    pred_path = config.get('predictions_path')

    preds = [os.path.join(pred_path, pred) for pred in os.listdir(pred_path) if pred.endswith('.json')]
    preds.sort()

    for subset in tqdm(glob(f'{imgs_path}/*'), 'Creating videos'):
        preds_subset = [pred for pred in preds if subset.split('/')[-1].lower() in pred]
        for pred in preds_subset:
            pred = tools.prepPred(pred)
            for day in glob(f'{subset}/*'):
                imgs = {}
                for img in glob(f'{day}/*.jpg'):
                    open_img = cv.imread(img, cv.IMREAD_COLOR)
                    imgs[img.split('/')[-1].split('.')[0]] = open_img

                imgs_keys = list(imgs.keys())
                imgs_keys.sort()

                h, w, l = imgs[list(imgs.keys())[0]].shape
                size = (w, h)

                day_split = day.split('/')
                file = day_split[-2] + '_' + day_split[-1] + '.mp4'
                file = os.path.join(out_path, file)

                vidWriter = cv.VideoWriter(file, cv.VideoWriter_fourcc(*"mp4v"), 1, size, True)
                tools.makeDay(imgs, imgs_keys, pred, vidWriter)
                vidWriter.release()

                # Comment this line to iterate all days
                #break
        # Comment this line to iterate all subsets
        #break

if __name__ == '__main__':
    main()
