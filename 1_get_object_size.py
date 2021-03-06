#-*- coding: utf-8 -*-

""" Get information on training dataset."""

import object_detector.file_io as file_io
import object_detector.extractor as extractor
import argparse as ap

DEFAULT_CONFIG_FILE = "conf/faces.json"

if __name__ == "__main__":
    
    parser = ap.ArgumentParser()
    parser.add_argument('-c', "--config", help="Configuration File", default=DEFAULT_CONFIG_FILE)
    args = vars(parser.parse_args())
    
    conf_ = file_io.FileJson().read(args["config"])
    h, w = extractor.calc_average_patch_size(conf_["dataset"]["annotations_dir"], "*.mat")
    print "[INFO] average (height, width) = {:.2f}, {:.2f}".format(h, w)





    

