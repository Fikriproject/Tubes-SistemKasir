-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jul 2024 pada 13.57
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webapi`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dbjual_elektronik`
--

CREATE TABLE `dbjual_elektronik` (
  `id` int(11) NOT NULL,
  `kdpelanggan` int(11) NOT NULL,
  `nama_pelanggan` varchar(50) NOT NULL,
  `kdbarang` varchar(20) NOT NULL,
  `barang` varchar(30) NOT NULL,
  `harga` int(11) NOT NULL,
  `banyaknya` int(11) NOT NULL,
  `pembayaran` enum('Cash','Credit') NOT NULL,
  `status` enum('Lunas','Cicilan') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `dbjual_elektronik`
--

INSERT INTO `dbjual_elektronik` (`id`, `kdpelanggan`, `nama_pelanggan`, `kdbarang`, `barang`, `harga`, `banyaknya`, `pembayaran`, `status`) VALUES
(1, 1001, 'Fikri', 'KK2P114', 'Kulkas 2 Pintu', 1000000, 1, 'Cash', 'Lunas'),
(6, 1002, 'Dio', 'TvSSOL3308', 'TvSamsungOled32Inch', 3000000, 1, 'Credit', 'Cicilan'),
(7, 1003, 'Reihan', 'APS12036', 'SmartAirPurifiyer12036', 1500000, 1, 'Cash', 'Lunas'),
(12, 1001, 'Fikri', 'MCS-SS303', 'Sharp Mesin Cuci Super Speed 3', 2500000, 1, 'Cash', 'Lunas'),
(14, 1001, 'Fikri', 'LPEL-EM703', 'Lampu Emergency Lumos EM703', 120000, 3, 'Cash', 'Lunas');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dbjual_elektronik`
--
ALTER TABLE `dbjual_elektronik`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `dbjual_elektronik`
--
ALTER TABLE `dbjual_elektronik`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
