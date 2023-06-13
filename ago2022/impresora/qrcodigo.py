#!/usr/bin/env python
# -*- coding: utf-8 -*-
import qrcode
img = qrcode.make("2 de septiembre")
f = open("fecha.png", "wb")
img.save(f)
f.close()
