import requests
import json

class elektronik:

    def __init__(self):
        self.__id = None
        self.kdpelanggan = None
        self.__nama_pelanggan = None
        self.__kdbarang = None
        self.__barang = None
        self.__harga = None
        self.__banyaknya = None
        self.__pembayaran = None
        self.__status = None
        self.__url = "http://localhost/webapi/elektronik_api.php"

    @property
    def id(self):
        return self.__id

    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan

    @nama_pelanggan.setter
    def nama_pelanggan(self, value):
        self.__nama_pelanggan = value

    @property
    def kdbarang(self):
        return self.__kdbarang

    @kdbarang.setter
    def kdbarang(self, value):
        self.__kdbarang = value
        
    @property
    def barang(self):
        return self.__barang

    @barang.setter
    def barang(self, value):
        self.__barang = value
        
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value
        
    @property
    def banyaknya(self):
        return self.__banyaknya

    @banyaknya.setter
    def banyaknya(self, value):
        self.__banyaknya = value
        
    @property
    def pembayaran(self):
        return self.__pembayaran

    @pembayaran.setter
    def pembayaran(self, value):
        self.__pembayaran = value
        
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def getBykdpelanggan(self, kdpelanggan):
        url = f"{self.__url}?kdpelanggan={kdpelanggan}"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        if data:
            item = data[0]
            self.__id = item["id"]
            self.kdpelanggan = item["kdpelanggan"]
            self.__nama_pelanggan = item["nama_pelanggan"]
            self.__kdbarang = item["kdbarang"]
            self.__barang = item["barang"]
            self.__harga = item["harga"]
            self.__banyaknya = item["banyaknya"]
            self.__pembayaran = item["pembayaran"]
            self.__status = item["status"]
        return data

    def simpan(self):
        payload = {
            "kdpelanggan": self.kdpelanggan,
            "nama_pelanggan": self.__nama_pelanggan,
            "kdbarang": self.__kdbarang,
            "barang": self.__barang,
            "harga": self.__harga,
            "banyaknya": self.__banyaknya,
            "pembayaran": self.__pembayaran,
            "status": self.__status
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text

    def updateBykdpelanggan(self, kdpelanggan):
        url = f"{self.__url}?kdpelanggan={kdpelanggan}"
        payload = {
            "kdpelanggan": self.kdpelanggan,
            "nama_pelanggan": self.__nama_pelanggan,
            "kdbarang": self.__kdbarang,
            "barang": self.__barang,
            "harga": self.__harga,
            "banyaknya": self.__banyaknya,
            "pembayaran": self.__pembayaran,
            "status": self.status
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text

    def getAllData(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, headers=headers)
        return response.text

    def deleteBykdpelanggan(self, kdpelanggan):
        url = f"{self.__url}?kdpelanggan={kdpelanggan}"
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url, headers=headers)
        return response.text
