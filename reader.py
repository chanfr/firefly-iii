from transaction_element import TransactionElement


class BankFileReader():
    def __init__(self, input_path:str):
        self.path = input_path

    def __iter__(self) -> TransactionElement:
        with open(self.path, encoding='latin-1') as f:
            for line_raw in f:
                line = line_raw.strip("\r\n\t")
                yield TransactionElement(line)
                # working = line.rstrip().split(" ")
                # trad, simp = working[0], working[1]
                # working = " ".join(working[2:]).split("]")
                # pinyin = working[0][1:]
                # english = working[1][1:]
                # yield trad, simp, pinyin, english