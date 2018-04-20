from Other.openpyxl_test import openpyxl as xl
import logging
import logging_conf

LOGGER = logging.getLogger('Trail')

if __name__ == '__main__':

    # xl.pyxl()

    LOGGER.info("hello log")

    # print("heloer")

    work_book = xl.activate_xlsx()
    xl.write_excel(work_book, 'TestDataS', 1, 1, 'Vinodkumar')
    # xl.get_no_of_iteration(work_book, 'TestDataS', 0)
    # xl.get_no_of_iteration(work_book, 'TestDataS', 0)
    # xl.read_excel(work_book, 'TestDataS', 1, 2)
    xl.row_list(work_book, 'Test_Output', 'TC002')
    xl.save_excel(work_book, 'TestDataX.xlsx')
