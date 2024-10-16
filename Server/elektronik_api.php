<?php
require_once 'database.php';
require_once 'elektronik.php';

$db = new MySQLDatabase();
$elektronik = new elektronik($db);
$id=0;
$kdpelanggan=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kdpelanggan'])){
            $kdpelanggan = $_GET['kdpelanggan'];
        }
        
        if($id>0){    
            $result = $elektronik->get_by_id($id);
        }elseif($kdpelanggan>0){
            $result = $elektronik->get_by_kdpelanggan($kdpelanggan);
        } else {
            $result = $elektronik->get_all();
        }        
       
        $elektronik = array();
        while ($row = $result->fetch_assoc()) {
            $elektronik[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($elektronik);
        break;

    case 'POST':
        // Add a new elektronik$elektronik
        $elektronik->kdpelanggan = $_POST['kdpelanggan'];
        $elektronik->nama_pelanggan = $_POST['nama_pelanggan'];
        $elektronik->kdbarang = $_POST['kdbarang'];
        $elektronik->barang = $_POST['barang'];
        $elektronik->harga = $_POST['harga'];
        $elektronik->banyaknya = $_POST['banyaknya'];
        $elektronik->pembayaran = $_POST['pembayaran'];
        $elektronik->status = $_POST['status'];
        $elektronik->insert();
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Employee data created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Employee data not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        // Update an existing elektronik$elektronik
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kdpelanggan'])){
            $kdpelanggan = $_GET['kdpelanggan'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $elektronik->kdpelanggan = $_PUT['kdpelanggan'];
        $elektronik->nama_pelanggan = $_PUT['nama_pelanggan'];
        $elektronik->kdbarang = $_PUT['kdbarang'];
        $elektronik->barang = $_PUT['barang'];
        $elektronik->harga = $_PUT['harga'];
        $elektronik->banyaknya = $_PUT['banyaknya'];
        $elektronik->pembayaran = $_PUT['pembayaran'];
        $elektronik->status = $_PUT['status'];
        if($id>0){    
            $elektronik->update($id);
        }elseif($kdpelanggan>0){
            $elektronik->update_by_kdpelanggan($kdpelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Employee data updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Employee data update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kdpelanggan'])){
            $kdpelanggan = $_GET['kdpelanggan'];
        }
        if($id>0){    
            $elektronik->delete($id);
        }elseif($kdpelanggan>0){
            $elektronik->delete_by_kdpelanggan($kdpelanggan);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Employee data deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Employee data delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}
$db->close()
?>
