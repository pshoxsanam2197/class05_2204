# 10-m
class Kompyuter:
    def yoq(self):
        print("Kompyuter yoqildi")
    def ishla(self):
        self.yoq()
        print("Kompyuter ishlamoqda")
    def ochir(self):
        self.ishla()
        print("Kompyuter o'chirildi")

k1 = Kompyuter()
k1.yoq()
print("---------")
k1.ishla()
print("---------")
k1.ochir()
