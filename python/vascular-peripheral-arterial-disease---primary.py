# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14NB.00","system":"readv2"},{"code":"G73..00","system":"readv2"},{"code":"G73z.00","system":"readv2"},{"code":"G73zz00","system":"readv2"},{"code":"10500","system":"med"},{"code":"11624","system":"med"},{"code":"12735","system":"med"},{"code":"14796","system":"med"},{"code":"14797","system":"med"},{"code":"1517","system":"med"},{"code":"15272","system":"med"},{"code":"15302","system":"med"},{"code":"16260","system":"med"},{"code":"1826","system":"med"},{"code":"19155","system":"med"},{"code":"22834","system":"med"},{"code":"23497","system":"med"},{"code":"23871","system":"med"},{"code":"24327","system":"med"},{"code":"25954","system":"med"},{"code":"2760","system":"med"},{"code":"30484","system":"med"},{"code":"31053","system":"med"},{"code":"34152","system":"med"},{"code":"34638","system":"med"},{"code":"3530","system":"med"},{"code":"35399","system":"med"},{"code":"3715","system":"med"},{"code":"37806","system":"med"},{"code":"38907","system":"med"},{"code":"4317","system":"med"},{"code":"4325","system":"med"},{"code":"53634","system":"med"},{"code":"5414","system":"med"},{"code":"54212","system":"med"},{"code":"54899","system":"med"},{"code":"5650","system":"med"},{"code":"56803","system":"med"},{"code":"5702","system":"med"},{"code":"5943","system":"med"},{"code":"60699","system":"med"},{"code":"6308","system":"med"},{"code":"63357","system":"med"},{"code":"64446","system":"med"},{"code":"65025","system":"med"},{"code":"67401","system":"med"},{"code":"6827","system":"med"},{"code":"6853","system":"med"},{"code":"68698","system":"med"},{"code":"69124","system":"med"},{"code":"70448","system":"med"},{"code":"72632","system":"med"},{"code":"73961","system":"med"},{"code":"8801","system":"med"},{"code":"9204","system":"med"},{"code":"93468","system":"med"},{"code":"9561","system":"med"},{"code":"98174","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peripheral-arterial-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["vascular-peripheral-arterial-disease---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["vascular-peripheral-arterial-disease---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["vascular-peripheral-arterial-disease---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
