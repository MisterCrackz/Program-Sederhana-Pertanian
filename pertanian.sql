-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2025 at 05:06 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pertanian`
--

-- --------------------------------------------------------

--
-- Table structure for table `alat`
--

CREATE TABLE `alat` (
  `kd_alat` varchar(10) NOT NULL,
  `nama_alat` varchar(100) NOT NULL,
  `kondisi` varchar(50) DEFAULT 'Baik',
  `stok` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alat`
--

INSERT INTO `alat` (`kd_alat`, `nama_alat`, `kondisi`, `stok`, `created_at`) VALUES
('A001', 'Cangkul', 'Baik', 10, '2025-11-13 03:55:26'),
('A002', 'Traktor Mini', 'Baik', 5, '2025-11-13 03:55:26'),
('A003', 'Sprayer', 'Baik', 8, '2025-11-13 03:55:26'),
('A004', 'Garu', 'Baik', 7, '2025-11-13 03:55:26');

-- --------------------------------------------------------

--
-- Table structure for table `bibit`
--

CREATE TABLE `bibit` (
  `kd_bibit` varchar(10) NOT NULL,
  `nama_bibit` varchar(100) NOT NULL,
  `satuan` varchar(50) NOT NULL,
  `masuk` int(11) DEFAULT 0,
  `keluar` int(11) DEFAULT 0,
  `stok` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bibit`
--

INSERT INTO `bibit` (`kd_bibit`, `nama_bibit`, `satuan`, `masuk`, `keluar`, `stok`, `created_at`) VALUES
('B001', 'Bibit Padi Ciherang', 'Kg', 100, 20, 80, '2025-11-13 03:55:26'),
('B002', 'Bibit Jagung Manis', 'Kg', 150, 30, 120, '2025-11-13 03:55:26'),
('B003', 'Bibit Kedelai Unggul', 'Kg', 200, 50, 150, '2025-11-13 03:55:26'),
('B004', 'Bibit Cabai Merah', 'Kg', 90, 10, 80, '2025-11-13 03:55:26'),
('B005', 'Bibit Tomat Lokal', 'Kg', 120, 25, 95, '2025-11-13 03:55:26');

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id_pengguna` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama_lengkap` varchar(100) DEFAULT NULL,
  `level` enum('admin','petani') DEFAULT 'petani',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id_pengguna`, `username`, `password`, `nama_lengkap`, `level`, `created_at`) VALUES
(1, 'admin', 'admin123', 'Administrator Utama', 'admin', '2025-11-13 03:55:26'),
(2, 'petani1', 'bibit2024', 'Budi Santoso', 'petani', '2025-11-13 03:55:26');

-- --------------------------------------------------------

--
-- Table structure for table `pupuk`
--

CREATE TABLE `pupuk` (
  `kd_pupuk` varchar(10) NOT NULL,
  `nama_pupuk` varchar(100) NOT NULL,
  `jenis` varchar(50) NOT NULL,
  `stok` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pupuk`
--

INSERT INTO `pupuk` (`kd_pupuk`, `nama_pupuk`, `jenis`, `stok`, `created_at`) VALUES
('P001', 'Urea', 'Kimia', 500, '2025-11-13 03:55:26'),
('P002', 'ZA', 'Kimia', 300, '2025-11-13 03:55:26'),
('P003', 'Kompos', 'Organik', 200, '2025-11-13 03:55:26'),
('P004', 'NPK', 'Campuran', 400, '2025-11-13 03:55:26');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_bibit`
--

CREATE TABLE `transaksi_bibit` (
  `id_transaksi` int(11) NOT NULL,
  `kd_bibit` varchar(10) DEFAULT NULL,
  `jenis_transaksi` enum('masuk','keluar') NOT NULL,
  `jumlah` int(11) NOT NULL,
  `tanggal` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi_bibit`
--

INSERT INTO `transaksi_bibit` (`id_transaksi`, `kd_bibit`, `jenis_transaksi`, `jumlah`, `tanggal`) VALUES
(1, 'B001', 'masuk', 50, '2025-11-13 03:55:26'),
(2, 'B001', 'keluar', 10, '2025-11-13 03:55:26'),
(3, 'B002', 'masuk', 70, '2025-11-13 03:55:26'),
(4, 'B003', 'keluar', 20, '2025-11-13 03:55:26');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alat`
--
ALTER TABLE `alat`
  ADD PRIMARY KEY (`kd_alat`);

--
-- Indexes for table `bibit`
--
ALTER TABLE `bibit`
  ADD PRIMARY KEY (`kd_bibit`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id_pengguna`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `pupuk`
--
ALTER TABLE `pupuk`
  ADD PRIMARY KEY (`kd_pupuk`);

--
-- Indexes for table `transaksi_bibit`
--
ALTER TABLE `transaksi_bibit`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `kd_bibit` (`kd_bibit`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id_pengguna` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `transaksi_bibit`
--
ALTER TABLE `transaksi_bibit`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaksi_bibit`
--
ALTER TABLE `transaksi_bibit`
  ADD CONSTRAINT `transaksi_bibit_ibfk_1` FOREIGN KEY (`kd_bibit`) REFERENCES `bibit` (`kd_bibit`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
