# 🚀 SQL Practices & Database Management

<p align="center">
  <a href="#english">English</a> | <a href="#türkçe">Türkçe</a>
</p>

---

## <a id="english"></a>🇬🇧 English

This repository contains structured SQL exercises, data manipulation practices, and relational database management scripts implemented in Microsoft SQL Server (SSMS) using T-SQL.

### 📂 Repository Structure

- **[`Basic-Commands/](./Basic-Commands/)**: Fundamental DML operations including database creation, table design with `IDENTITY` primary keys, `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE` operations, alongside conditional filtering (`WHERE`, `BETWEEN`, `LIKE`, `IN`, `AND`, `OR`), distinct records (`DISTINCT`), sorting (`ORDER BY`, `TOP / PERCENT`), and dynamic date calculations (`DATEDIFF`).
- **[`Data-Types/`](./Data-Types/)**: Superstore Sales & Operations Analysis project using the Kaggle Sales Forecasting dataset (`train.csv`, 9,800 rows) ingested into MS SQL Server (`ETRADE3.dbo.RAW_SUPERSTORE`) via Python (`pandas`, `SQLAlchemy`, `pyodbc`), covering `CONVERT` date parsing, `DATEPART`, `DATEDIFF`, `GROUP BY`, `COUNT(DISTINCT ...)`, `TOP`, and `WHERE` vs. `HAVING` filtering.

### 🛠 Tech Stack & Tools
- **Database Management System:** Microsoft SQL Server (MS SQL)
- **Environment:** SQL Server Management Studio (SSMS)
- **Query Language:** T-SQL (Transact-SQL)
- **Data Ingestion:** Python (`pandas`, `SQLAlchemy`, `pyodbc`)
- **Version Control:** Git, GitHub, GitHub Desktop

---

## <a id="türkçe"></a>🇹🇷 Türkçe

Bu repo, T-SQL kullanılarak Microsoft SQL Server (SSMS) üzerinde geliştirilmiş yapılandırılmış SQL egzersizleri, veri manipülasyon pratikleri ve ilişkisel veritabanı yönetim betikleri içermektedir.

### 📂 Depo Yapısı

- **[`Basic-Commands/](./Basic-Commands/)`**: Veritabanı oluşturma, `IDENTITY` birincil anahtarları ile tablo tasarımı, `INSERT`, `UPDATE`, `DELETE` ve `TRUNCATE` işlemlerini içeren temel DML operasyonları; koşullu filtreleme (`WHERE`, `BETWEEN`, `LIKE`, `IN`, `AND`, `OR`), tekilleştirme (`DISTINCT`), sıralama (`ORDER BY`, `TOP / PERCENT`) ve dinamik tarih hesaplamaları (`DATEDIFF`).
- **[`Data-Types/`](./Data-Types/)**: Kaggle Sales Forecasting veri seti (`train.csv`, 9.800 satır) kullanılarak hazırlanan Superstore Satış ve Operasyon Analizi projesi; Python (`pandas`, `SQLAlchemy`, `pyodbc`) ile MS SQL Server'a (`ETRADE3.dbo.RAW_SUPERSTORE`) veri aktarımı, `CONVERT` ile tarih dönüşümü, `DATEPART`, `DATEDIFF`, `GROUP BY`, `COUNT(DISTINCT ...)`, `TOP` ve `WHERE` / `HAVING` filtreleme uygulamaları.

### 🛠 Teknoloji Yığını ve Araçlar
- **Veritabanı Yönetim Sistemi:** Microsoft SQL Server (MS SQL)
- **Ortam:** SQL Server Management Studio (SSMS)
- **Sorgu Dili:** T-SQL (Transact-SQL)
- **Veri Aktarımı:** Python (`pandas`, `SQLAlchemy`, `pyodbc`)
- **Versiyon Kontrolü:** Git, GitHub, GitHub Desktop
