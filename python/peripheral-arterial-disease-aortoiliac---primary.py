# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7A41.00","system":"readv2"},{"code":"7A41z00","system":"readv2"},{"code":"7A42.00","system":"readv2"},{"code":"7A42.11","system":"readv2"},{"code":"7A42000","system":"readv2"},{"code":"7A42011","system":"readv2"},{"code":"7A42012","system":"readv2"},{"code":"7A42100","system":"readv2"},{"code":"7A42111","system":"readv2"},{"code":"7A42z00","system":"readv2"},{"code":"7A43.00","system":"readv2"},{"code":"7A43.11","system":"readv2"},{"code":"7A43000","system":"readv2"},{"code":"7A43011","system":"readv2"},{"code":"7A43100","system":"readv2"},{"code":"7A43111","system":"readv2"},{"code":"7A43300","system":"readv2"},{"code":"7A44100","system":"readv2"},{"code":"7A44300","system":"readv2"},{"code":"7A44400","system":"readv2"},{"code":"7A44z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peripheral-arterial-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peripheral-arterial-disease-aortoiliac---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peripheral-arterial-disease-aortoiliac---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peripheral-arterial-disease-aortoiliac---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
