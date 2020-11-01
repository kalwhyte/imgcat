#!/usr/bin/env python
# coding: utf-8

"Table generated from xterm-256color.yaml"

def _generate_dict():
    """
    This is what I typed in iPython to copy-paste the dict.  You will
    need PyYaml though::

        pip install --user PyYAML
    """
    import yaml
    with open('xterm-256color.yaml') as f:
        o = yaml.load(f)
    l = sum(o.values(), [])
    i = lambda x: int(x, 16)
    return {code: (i(x[1:3]), i(x[3:5]), i(x[5:7])) for code, x in l}

COLORS = {
 '000': (0, 0, 0),
 '001': (128, 0, 0),
 '002': (0, 128, 0),
 '003': (128, 128, 0),
 '004': (0, 0, 128),
 '005': (128, 0, 128),
 '006': (0, 128, 128),
 '007': (192, 192, 192),
 '008': (128, 128, 128),
 '009': (255, 0, 0),
 '010': (0, 255, 0),
 '011': (255, 255, 0),
 '012': (0, 0, 255),
 '013': (255, 0, 255),
 '014': (0, 255, 255),
 '015': (255, 255, 255),
 '016': (0, 0, 0),
 '017': (0, 0, 95),
 '018': (0, 0, 135),
 '019': (0, 0, 175),
 '020': (0, 0, 215),
 '021': (0, 0, 255),
 '022': (0, 95, 0),
 '023': (0, 95, 95),
 '024': (0, 95, 135),
 '025': (0, 95, 175),
 '026': (0, 95, 215),
 '027': (0, 95, 255),
 '028': (0, 135, 0),
 '029': (0, 135, 95),
 '030': (0, 135, 135),
 '031': (0, 135, 175),
 '032': (0, 135, 215),
 '033': (0, 135, 255),
 '034': (0, 175, 0),
 '035': (0, 175, 95),
 '036': (0, 175, 135),
 '037': (0, 175, 175),
 '038': (0, 175, 215),
 '039': (0, 175, 255),
 '040': (0, 215, 0),
 '041': (0, 215, 95),
 '042': (0, 215, 135),
 '043': (0, 215, 175),
 '044': (0, 215, 215),
 '045': (0, 215, 255),
 '046': (0, 255, 0),
 '047': (0, 255, 95),
 '048': (0, 255, 135),
 '049': (0, 255, 175),
 '050': (0, 255, 215),
 '051': (0, 255, 255),
 '052': (95, 0, 0),
 '053': (95, 0, 95),
 '054': (95, 0, 135),
 '055': (95, 0, 175),
 '056': (95, 0, 215),
 '057': (95, 0, 255),
 '058': (95, 95, 0),
 '059': (95, 95, 95),
 '060': (95, 95, 135),
 '061': (95, 95, 175),
 '062': (95, 95, 215),
 '063': (95, 95, 255),
 '064': (95, 135, 0),
 '065': (95, 135, 95),
 '066': (95, 135, 135),
 '067': (95, 135, 175),
 '068': (95, 135, 215),
 '069': (95, 135, 255),
 '070': (95, 175, 0),
 '071': (95, 175, 95),
 '072': (95, 175, 135),
 '073': (95, 175, 175),
 '074': (95, 175, 215),
 '075': (95, 175, 255),
 '076': (95, 215, 0),
 '077': (95, 215, 95),
 '078': (95, 215, 135),
 '079': (95, 215, 175),
 '080': (95, 215, 215),
 '081': (95, 215, 255),
 '082': (95, 255, 0),
 '083': (95, 255, 95),
 '084': (95, 255, 135),
 '085': (95, 255, 175),
 '086': (95, 255, 215),
 '087': (95, 255, 255),
 '088': (135, 0, 0),
 '089': (135, 0, 95),
 '090': (135, 0, 135),
 '091': (135, 0, 175),
 '092': (135, 0, 215),
 '093': (135, 0, 255),
 '094': (135, 95, 0),
 '095': (135, 95, 95),
 '096': (135, 95, 135),
 '097': (135, 95, 175),
 '098': (135, 95, 215),
 '099': (135, 95, 255),
 '100': (135, 135, 0),
 '101': (135, 135, 95),
 '102': (135, 135, 135),
 '103': (135, 135, 175),
 '104': (135, 135, 215),
 '105': (135, 135, 255),
 '106': (135, 175, 0),
 '107': (135, 175, 95),
 '108': (135, 175, 135),
 '109': (135, 175, 175),
 '110': (135, 175, 215),
 '111': (135, 175, 255),
 '112': (135, 215, 0),
 '113': (135, 215, 95),
 '114': (135, 215, 135),
 '115': (135, 215, 175),
 '116': (135, 215, 215),
 '117': (135, 215, 255),
 '118': (135, 255, 0),
 '119': (135, 255, 95),
 '120': (135, 255, 135),
 '121': (135, 255, 175),
 '122': (135, 255, 215),
 '123': (135, 255, 255),
 '124': (175, 0, 0),
 '125': (175, 0, 95),
 '126': (175, 0, 135),
 '127': (175, 0, 175),
 '128': (175, 0, 215),
 '129': (175, 0, 255),
 '130': (175, 95, 0),
 '131': (175, 95, 95),
 '132': (175, 95, 135),
 '133': (175, 95, 175),
 '134': (175, 95, 215),
 '135': (175, 95, 255),
 '136': (175, 135, 0),
 '137': (175, 135, 95),
 '138': (175, 135, 135),
 '139': (175, 135, 175),
 '140': (175, 135, 215),
 '141': (175, 135, 255),
 '142': (175, 175, 0),
 '143': (175, 175, 95),
 '144': (175, 175, 135),
 '145': (175, 175, 175),
 '146': (175, 175, 215),
 '147': (175, 175, 255),
 '148': (175, 215, 0),
 '149': (175, 215, 95),
 '150': (175, 215, 135),
 '151': (175, 215, 175),
 '152': (175, 215, 215),
 '153': (175, 215, 255),
 '154': (175, 255, 0),
 '155': (175, 255, 95),
 '156': (175, 255, 135),
 '157': (175, 255, 175),
 '158': (175, 255, 215),
 '159': (175, 255, 255),
 '160': (215, 0, 0),
 '161': (215, 0, 95),
 '162': (215, 0, 135),
 '163': (215, 0, 175),
 '164': (215, 0, 215),
 '165': (215, 0, 255),
 '166': (215, 95, 0),
 '167': (215, 95, 95),
 '168': (215, 95, 135),
 '169': (215, 95, 175),
 '170': (215, 95, 215),
 '171': (215, 95, 255),
 '172': (215, 135, 0),
 '173': (215, 135, 95),
 '174': (215, 135, 135),
 '175': (215, 135, 175),
 '176': (215, 135, 215),
 '177': (215, 135, 255),
 '178': (223, 175, 0),
 '179': (223, 175, 95),
 '180': (223, 175, 135),
 '181': (223, 175, 175),
 '182': (223, 175, 223),
 '183': (223, 175, 255),
 '184': (223, 223, 0),
 '185': (223, 223, 95),
 '186': (223, 223, 135),
 '187': (223, 223, 175),
 '188': (223, 223, 223),
 '189': (223, 223, 255),
 '190': (223, 255, 0),
 '191': (223, 255, 95),
 '192': (223, 255, 135),
 '193': (223, 255, 175),
 '194': (223, 255, 223),
 '195': (223, 255, 255),
 '196': (255, 0, 0),
 '197': (255, 0, 95),
 '198': (255, 0, 135),
 '199': (255, 0, 175),
 '200': (255, 0, 223),
 '201': (255, 0, 255),
 '202': (255, 95, 0),
 '203': (255, 95, 95),
 '204': (255, 95, 135),
 '205': (255, 95, 175),
 '206': (255, 95, 223),
 '207': (255, 95, 255),
 '208': (255, 135, 0),
 '209': (255, 135, 95),
 '210': (255, 135, 135),
 '211': (255, 135, 175),
 '212': (255, 135, 223),
 '213': (255, 135, 255),
 '214': (255, 175, 0),
 '215': (255, 175, 95),
 '216': (255, 175, 135),
 '217': (255, 175, 175),
 '218': (255, 175, 223),
 '219': (255, 175, 255),
 '220': (255, 223, 0),
 '221': (255, 223, 95),
 '222': (255, 223, 135),
 '223': (255, 223, 175),
 '224': (255, 223, 223),
 '225': (255, 223, 255),
 '226': (255, 255, 0),
 '227': (255, 255, 95),
 '228': (255, 255, 135),
 '229': (255, 255, 175),
 '230': (255, 255, 223),
 '231': (255, 255, 255),
 '232': (8, 8, 8),
 '233': (18, 18, 18),
 '234': (28, 28, 28),
 '235': (38, 38, 38),
 '236': (48, 48, 48),
 '237': (58, 58, 58),
 '238': (68, 68, 68),
 '239': (78, 78, 78),
 '240': (88, 88, 88),
 '241': (98, 98, 98),
 '242': (108, 108, 108),
 '243': (118, 118, 118),
 '244': (128, 128, 128),
 '245': (138, 138, 138),
 '246': (148, 148, 148),
 '247': (158, 158, 158),
 '248': (168, 168, 168),
 '249': (178, 178, 178),
 '250': (188, 188, 188),
 '251': (198, 198, 198),
 '252': (208, 208, 208),
 '253': (218, 218, 218),
 '254': (228, 228, 228),
 '255': (238, 238, 238)
}