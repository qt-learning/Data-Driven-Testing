# -*- coding: utf-8 -*-

import names

def enterValue(val):
    flagNegative = False
    if val[0] == '-':
        flagNegative = True
        val = val[1:]
    for integer in val:
        obj = {"container": names.o_QQuickView, "text": integer, "type": "Text", "unnamed": 1, "visible": True}
        mouseClick(waitForObject(obj))
    if flagNegative:
        mouseClick(waitForObject(names.o_Text_3))

def main():
    startApplication("calqlatr")

    for record in testData.dataset("product_data.tsv"):
        left = testData.field(record, "Left")
        right = testData.field(record, "Right")
        product = testData.field(record, "Product")
    
        enterValue(left)
        mouseClick(waitForObject(names.o_Text))
        enterValue(right)
        mouseClick(waitForObject(names.o_Text_2))
        test.compare(str(waitForObjectExists(names.display_Display).displayedOperand), product)
        mouseClick(waitForObject(names.c_Text))