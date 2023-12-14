class Bank:
    #member1 properti / atribut
    norek = ''
    nama = ''
    saldo = 0
    jmlNasabah = 0 # variabel static
    BANK = 'Bank Syariah Nurul Fikri' # variabel konstanta

    #member2 konstruktor
    # konstruktor akan dijalankan otomatis ketika class dipanggil
    def __init__(self,no,nasabah,saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlNasabah += 1

    #member3 method
    def nabung(self,uang):
        # self.saldo = self.saldo + uang
        self.saldo += uang

    def tarik(self,uang):
        # self.saldo = self.saldo - uang 
        self.saldo -= uang

    def cetak(self): print(Bank.BANK,
    '\n==========================',
    '\nNo. Rekening\t:',self.norek,
    '\nNama Nasabah\t:',self.nama,
    '\nSaldo\t\t: Rp. ',format(self.saldo, ','), '\n--------------------------'
    )
        
nasabah1 = Bank("1001", "Aldi", 50000)
nasabah2 = Bank("1002", "Edo", 70000)

nasabah1.nabung(4000)
print(nasabah1.saldo)