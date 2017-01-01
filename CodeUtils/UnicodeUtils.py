# -*- coding: utf-8 -*-
import json

def unicodeToStr(Str):
    return json.loads('"%s"' % Str)