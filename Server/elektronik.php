<?php
require_once 'database.php';

class elektronik

{
    private $db;
    private $table = 'dbjual_elektronik';
    public $kdpelanggan = "";
    public $nama_pelanggan = "";
    public $kdbarang = "";
    public $barang = "";
    public $harga = "";
    public $banyaknya = "";
    public $pembayaran = "";
    public $status = "";

    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }

    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }

    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function get_by_kdpelanggan(int $kdpelanggan)
    {
        $query = "SELECT * FROM $this->table WHERE kdpelanggan = $kdpelanggan";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kdpelanggan`, `nama_pelanggan`, `kdbarang`,`barang`, `harga`, `banyaknya`, `pembayaran`, `status`) VALUES ('$this->kdpelanggan', '$this->nama_pelanggan', '$this->kdbarang', '$this->barang', '$this->harga', '$this->banyaknya', '$this->pembayaran', '$this->status')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `kdpelanggan` = '$this->kdpelanggan', `nama_pelanggan` = '$this->nama_pelanggan', `kdbarang` = '$this->kdbarang', `barang` = '$this->barang', `harga` = '$this->harga',`banyaknya` = '$this->banyaknya', `pembayaran` = '$this->pembayaran', `status` = '$this->status' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_kdpelanggan($kdpelanggan): int
    {
        $query = "UPDATE $this->table SET `nama_pelanggan` = '$this->nama_pelanggan', `kdbarang` = '$this->kdbarang', `barang` = '$this->barang', `harga` = '$this->harga',`banyaknya` = '$this->banyaknya', `pembayaran` = '$this->pembayaran', `status` = '$this->status' WHERE kdpelanggan = $kdpelanggan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_kdpelanggan($kdpelanggan): int
    {
        $query = "DELETE FROM $this->table WHERE kdpelanggan = $kdpelanggan";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>