# -*- coding: utf-8 -*-

import names

def main():
    test_suite_data = findFile("testdata", "test_suite_data.tsv")
    test_case_data = findFile("testdata", "test_case_data.csv")
    excel_data = findFile("testdata", "excel_data.xlsx")
    
    test.log(test_suite_data)
    test.log(test_case_data)
    test.log (excel_data)