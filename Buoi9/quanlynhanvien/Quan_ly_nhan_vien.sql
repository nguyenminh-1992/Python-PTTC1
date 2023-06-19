-- create database
DROP DATABASE IF EXISTS Quan_ly_nhan_vien;
CREATE DATABASE Quan_ly_nhan_vien;
USE Quan_ly_nhan_vien;

DROP TABLE IF EXISTS Nhanvien;
CREATE TABLE Nhanvien(
	ID 						TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	`Name` 					NVARCHAR(30) NOT NULL,
    Age						TINYINT UNSIGNED,
    Country					NVARCHAR(30) NOT NULL,
    Chucvu					NVARCHAR(30) NOT NULL,
    Songaylam				TINYINT UNSIGNED
);


INSERT INTO Nhanvien(`Name`,		Age,	Country,	Chucvu,	Songaylam) 
VALUES 				('Nguyen Van A', 20, 	'Ha Noi', 	'NV'  ,  30		),
					('Nguyen Van B', 21, 	'Da Nang', 	'GD'  ,  29		),
					('Nguyen Van C', 22, 	'Nha Trang', 	'TP'  ,  25		)
