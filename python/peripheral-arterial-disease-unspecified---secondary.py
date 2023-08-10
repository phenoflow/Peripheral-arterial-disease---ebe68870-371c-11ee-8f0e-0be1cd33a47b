# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"I738","system":"icd10"},{"code":"I739","system":"icd10"},{"code":"L50.8","system":"opcs4"},{"code":"L50.9","system":"opcs4"},{"code":"L51.8","system":"opcs4"},{"code":"L51.9","system":"opcs4"},{"code":"L52.8","system":"opcs4"},{"code":"L52.9","system":"opcs4"},{"code":"L58.8","system":"opcs4"},{"code":"L58.9","system":"opcs4"},{"code":"L59.8","system":"opcs4"},{"code":"L59.9","system":"opcs4"},{"code":"L60.8","system":"opcs4"},{"code":"L60.9","system":"opcs4"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peripheral-arterial-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peripheral-arterial-disease-unspecified---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peripheral-arterial-disease-unspecified---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peripheral-arterial-disease-unspecified---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
