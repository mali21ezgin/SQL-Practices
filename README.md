# 🚀 SQL Practices & Database Management

<p align="center">
  <a href="#english">English</a> | <a href="#türkçe">Türkçe</a>
</p>

---

## <a id="english"></a>🇬🇧 English

This repository contains structured SQL exercises, data manipulation practices, and relational database management scripts implemented in Microsoft SQL Server (SSMS) using T-SQL.

### 📂 Repository Structure

- **[`Basic-Commands/`](./Basic-Commands/)**: Fundamental DML operations including database creation, table design with `IDENTITY` primary keys, `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE` operations, alongside conditional filtering (`WHERE`, `BETWEEN`, `LIKE`, `IN`, `AND`, `OR`), distinct records (`DISTINCT`), sorting (`ORDER BY`, `TOP / PERCENT`), and dynamic date calculations (`DATEDIFF`).
- **[`Data-Types/`](./Data-Types/)**: Superstore Sales & Operations Analysis project using the Kaggle Sales Forecasting dataset (`train.csv`, 9,800 rows) ingested into MS SQL Server (`ETRADE3.dbo.RAW_SUPERSTORE`) via Python (`pandas`, `SQLAlchemy`, `pyodbc`), covering `CONVERT` date parsing, `DATEPART`, `DATEDIFF`, `GROUP BY`, `COUNT(DISTINCT ...)`, `TOP`, and `WHERE` vs. `HAVING` filtering.
- **[`Field-Service-Tracker-Tsql/`](./Field-Service-Tracker-Tsql/)**: Relational database schema and sample dataset (`FieldServiceDB`) for a Field Service Management system with six tables (`USERS`, `LOCATIONS`, `ASSETS`, `CATEGORIES`, `TICKETS`, `TICKETASSIGNMENTS`), `IDENTITY`, `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, and `DEFAULT` constraints, sample `INSERT` records, and an SSMS entity-relationship diagram (ERD).
- **[`Joins-GroupBy/`](./Joins-GroupBy/)**: Relational multi-table queries across `USERS`, `ADDRESS`, `COUNTRIES`, `CITIES`, `TOWNS`, and `DISTRICTS` covering `WHERE` joins, explicit `INNER JOIN ... ON ...`, column/table aliases, `DISTINCT`, `COUNT(DISTINCT ...)`, `GROUP BY` with `HAVING`, `ORDER BY`, and `INSERT` / `TRUNCATE` statements.
- **[`Subqueries-StringFunctions/`](./Subqueries-StringFunctions/)**: Aggregate grouping, correlated scalar subqueries across `ITEMS`, `ADDRESS`, `ORDERS`, and `PAYMENTS`, string parsing/cleaning/formatting (`LEFT`, `RIGHT`, `CHARINDEX`, `SUBSTRING`, `TRIM`, `LTRIM`, `RTRIM`, `CONCAT`, `CONCAT_WS`, `REPLICATE`, `REPLACE`, `LOWER`, `UPPER`, `REVERSE`, `ASCII`, `CHAR`), and date formatting (`FORMAT`, `CONVERT`, `GETDATE`).

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

- **[`Basic-Commands/`](./Basic-Commands/)**: Veritabanı oluşturma, `IDENTITY` birincil anahtarları ile tablo tasarımı, `INSERT`, `UPDATE`, `DELETE` ve `TRUNCATE` işlemlerini içeren temel DML operasyonları; koşullu filtreleme (`WHERE`, `BETWEEN`, `LIKE`, `IN`, `AND`, `OR`), tekilleştirme (`DISTINCT`), sıralama (`ORDER BY`, `TOP / PERCENT`) ve dinamik tarih hesaplamaları (`DATEDIFF`).
- **[`Data-Types/`](./Data-Types/)**: Kaggle Sales Forecasting veri seti (`train.csv`, 9.800 satır) kullanılarak hazırlanan Superstore Satış ve Operasyon Analizi projesi; Python (`pandas`, `SQLAlchemy`, `pyodbc`) ile MS SQL Server'a (`ETRADE3.dbo.RAW_SUPERSTORE`) veri aktarımı, `CONVERT` ile tarih dönüşümü, `DATEPART`, `DATEDIFF`, `GROUP BY`, `COUNT(DISTINCT ...)`, `TOP` ve `WHERE` / `HAVING` filtreleme uygulamaları.
- **[`Field-Service-Tracker-Tsql/`](./Field-Service-Tracker-Tsql/)**: Saha Servis Yönetimi sistemi için altı tablodan (`USERS`, `LOCATIONS`, `ASSETS`, `CATEGORIES`, `TICKETS`, `TICKETASSIGNMENTS`) oluşan ilişkisel veritabanı şeması ve örnek veri seti (`FieldServiceDB`); `IDENTITY`, `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK` ve `DEFAULT` kısıtları, test `INSERT` kayıtları ve SSMS veritabanı diyagramını (ERD) kapsar.
- **[`Joins-GroupBy/`](./Joins-GroupBy/)**: `USERS`, `ADDRESS`, `COUNTRIES`, `CITIES`, `TOWNS` ve `DISTRICTS` tabloları üzerinde `WHERE` ile birleştirme, açık `INNER JOIN ... ON ...`, tablo/sütun takma adları (`ALIAS`), `DISTINCT`, `COUNT(DISTINCT ...)`, `GROUP BY` ile `HAVING`, `ORDER BY` ve `INSERT` / `TRUNCATE` pratikleri.
- **[`Subqueries-StringFunctions/`](./Subqueries-StringFunctions/)**: `ITEMS`, `ADDRESS`, `ORDERS` ve `PAYMENTS` tablolarında toplulaştırma ve ilişkili alt sorgular, metin bölme/temizleme/biçimlendirme (`LEFT`, `RIGHT`, `CHARINDEX`, `SUBSTRING`, `TRIM`, `LTRIM`, `RTRIM`, `CONCAT`, `CONCAT_WS`, `REPLICATE`, `REPLACE`, `LOWER`, `UPPER`, `REVERSE`, `ASCII`, `CHAR`) ve tarih formatlama (`FORMAT`, `CONVERT`, `GETDATE`) uygulamaları.

### 🛠 Teknoloji Yığını ve Araçlar
- **Veritabanı Yönetim Sistemi:** Microsoft SQL Server (MS SQL)
- **Ortam:** SQL Server Management Studio (SSMS)
- **Sorgu Dili:** T-SQL (Transact-SQL)
- **Veri Aktarımı:** Python (`pandas`, `SQLAlchemy`, `pyodbc`)
- **Versiyon Kontrolü:** Git, GitHub, GitHub Desktop
