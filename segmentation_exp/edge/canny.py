import argparse
import yaml

class Image:
    def __init__(self, img):
        self.original = img
        self.rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def main:
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='YAML configuration file')
    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    imgs_dir = os.path.abspath(config.get('images_dir')) + '/'
    dest_dir = os.path.abspath(config.get('dest_dir')) + '/'
    os.makedirs(dest_dir, exist_ok=True)

    images = sorted(glob(f'{imgs_dir}/*'}))
    for image in images:
        img = Image(cv.imread(image))
