# 🚀 SQL Practices & Database Management

<p align="center">
  <a href="#english">English</a> | <a href="#türkçe">Türkçe</a>
</p>

---

## <a id="english"></a>🇬🇧 English

This repository contains structured SQL exercises, data manipulation practices, and relational database management projects built with Microsoft SQL Server (SSMS) using T-SQL, focused on developing robust backend data skills.

<!-- ### 📂 Repository Structure

* **`Day-04-Basic-Commands/`**: Fundamental DML operations including database creation (`CREATE DATABASE`, `USE`), table design with `IDENTITY` primary keys, `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE` operations, alongside conditional filtering (`WHERE`, `BETWEEN`, `LIKE`, `IN`, `AND`, `OR`), distinct records (`DISTINCT`), and sorting (`ORDER BY`, `TOP / PERCENT`). -->

### 📝 Project Solutions & Evaluation Guide

Below is the structured overview of the practical SQL tasks completed in this section, along with technical assessments:

1. **Table Creation & Data Insertion (INSERT)**
   * **Status:** Excellent. Successfully created the `ETRADE2` database and `CUSTOMERS` table using proper data types. Adhered to the core rule by omitting the `ID` field during `INSERT` statements, allowing the `IDENTITY(1,1)` constraint to handle auto-incrementing safely. Date formats and string literals were structured correctly.

2. **Data Retrieval & Sorting (SELECT, TOP, ORDER BY)**
   * **Status:** Fully Correct. Accurately implemented `SELECT *`, `TOP 100`, and `TOP 50 PERCENT` clauses combined with `ORDER BY` using both ascending (`ASC`) and descending (`DESC`) ordering parameters.

3. **Data Modification & Dynamic Calculations (UPDATE & DATEDIFF)**
   * **Status:** Outstanding. Implemented automated data updates such as setting global country codes (`NATION = 'TR'`) and dynamically calculating customer ages using `DATEDIFF(YEAR, BIRTHDATE, GETDATE())`. Handled targeted updates using precise `WHERE` clauses for gender categorization (`'ERKEK'` and `'KADIN'`).

4. **Advanced Filtering & Conditional Logic (WHERE, OR, <>, NOT, BETWEEN, LIKE, IN)**
   * **Status:** Flawless. Correctly applied multi-condition filters including `OR`, negation operators (`<>` and `NOT`), range selections (`BETWEEN`), pattern matching (`LIKE`), and list memberships (`IN`). 
   * *Note on Collation:* Handled textual casing and character considerations (e.g., `'ISTANBUL'` vs `'İSTANBUL'`) correctly in query structures.

5. **Distinct Records & Positional Sorting (DISTINCT & ORDER BY Column Indexes)**
   * **Status:** Professional Grade. Utilized `DISTINCT` for retrieving unique cities and combined district-city subsets. Demonstrated advanced T-SQL capability by applying positional column sorting (`ORDER BY 3, 4, 2`) based on the `SELECT` projection sequence.

6. **Data Deletion & Table Reset (DELETE & TRUNCATE)**
   * **Status:** Correct. Executed conditional row removal via `DELETE FROM CUSTOMERS WHERE ID = 1` and properly documented table-level truncation principles (`TRUNCATE TABLE CUSTOMERS`).

### 🛠 Tech Stack & Tools

* **Database Management System:** Microsoft SQL Server (MS SQL)
* **Environment:** SQL Server Management Studio (SSMS)
* **Query Language:** T-SQL (Transact-SQL)
* **Version Control:** Git, GitHub

---

## <a id="türkçe"></a>🇹🇷 Türkçe

Bu repo, T-SQL kullanılarak Microsoft SQL Server (SSMS) üzerinde geliştirilmiş yapılandırılmış SQL egzersizleri, veri manipülasyon pratikleri ve ilişkisel veritabanı yönetim projeleri içermekte olup, sağlam backend veri becerileri geliştirmeyi amaçlamaktadır.

<!-- ### 📂 Depo Yapısı

* **`Day-04-Basic-Commands/`**: Veritabanı oluşturma (`CREATE DATABASE`, `USE`), `IDENTITY` birincil anahtarları ile tablo tasarımı, `INSERT`, `UPDATE`, `DELETE` ve `TRUNCATE` işlemlerini içeren temel DML operasyonları; koşullu filtreleme (`WHERE`, `BETWEEN`, `LIKE`, `IN`, `AND`, `OR`), tekilleştirme (`DISTINCT`) ve sıralama (`ORDER BY`, `TOP / PERCENT`) çalışmaları. -->

### 📝 Proje Çözümleri ve Değerlendirme Rehberi

Bu bölümde tamamlanan pratik SQL görevlerinin yapılandırılmış özeti ve teknik değerlendirmeleri aşağıdadır:

1. **Tablo Oluşturma ve Veri Ekleme (INSERT)**
   * **Durum:** Mükemmel. `ETRADE2` veritabanı ve uygun veri tipleriyle `CUSTOMERS` tablosu kuruldu. `INSERT` işlemlerinde `ID` alanı dışarıda bırakılarak `IDENTITY(1,1)` kuralına tam uyum sağlandı. Tarih formatları ve metinsel ifadeler hatasız işlendi.

2. **Veri Listeleme ve Sıralama (SELECT, TOP, ORDER BY)**
   * **Durum:** Tamamen Doğru. `SELECT *`, `TOP 100` ve `TOP 50 PERCENT` ifadeleri; `ORDER BY` ile artan (`ASC`) ve azalan (`DESC`) yönlü sıralamalarla kusursuz şekilde uygulandı.

3. **Veri Güncelleme ve Dinamik Hesaplama (UPDATE & DATEDIFF)**
   * **Durum:** Harika. Tüm müşteriler için ülke bilgisi güncellenirken, `DATEDIFF(YEAR, BIRTHDATE, GETDATE())` fonksiyonu kullanılarak yaşların veritabanından dinamik olarak hesaplatılıp güncellenmesi sağlandı. Cinsiyet kısaltmaları `WHERE` koşullarıyla doğru kategorilere (`'ERKEK'`, `'KADIN'`) aktarıldı.

4. **Gelişmiş Filtreleme ve Koşullar (WHERE, OR, <>, NOT, BETWEEN, LIKE, IN)**
   * **Durum:** Kusursuz. `OR`, olumsuzluk operatörleri (`<>` ve `NOT`), aralık seçimleri (`BETWEEN`), desen arama (`LIKE`) ve liste üyelikleri (`IN`) mantıksal olarak doğru uygulandı. 
   * *Dil/Karakter Notu:* Sorgu yazımında metin eşleşme mantığı tam oturtuldu.

5. **Tekilleştirme ve Sıralama Analizleri (DISTINCT & Sıra Numaralarıyla ORDER BY)**
   * **Durum:** Profesyonel Düzeyde. Benzersiz şehir ve ilçe kombinasyonları için `DISTINCT` başarıyla kullanıldı. `SELECT` içindeki sütun sıra numaralarına göre sıralama yapma (`ORDER BY 3, 4, 2`) gibi ileri düzey bir pratik başarıyla sergilendi.

6. **Veri Silme ve Tablo Sıfırlama (DELETE & TRUNCATE)**
   * **Durum:** Doğru. `DELETE FROM CUSTOMERS WHERE ID = 1` ile koşullu satır silme işlemi yapıldı ve tablonun tamamını sıfırlamak için `TRUNCATE TABLE CUSTOMERS` mantığı dokümante edildi.

### 🛠 Teknoloji Yığını ve Araçlar

* **Veritabanı Yönetim Sistemi:** Microsoft SQL Server (MS SQL)
* **Ortam:** SQL Server Management Studio (SSMS)
* **Sorgu Dili:** T-SQL (Transact-SQL)
* **Versiyon Kontrolü:** Git, GitHub

---
