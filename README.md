# 📊 Live Log Analysis Dashboard | لوحة تحكم وتحليل السجلات الفورية



## 🌍 English Description

### 📝 Overview
This is a real-time **Full-Stack Data Engineering Pipeline** designed to monitor server performance, track incoming requests, and analyze user behavior on the fly. 

Instead of reading static log files, this system processes data dynamically as it generates, parses the raw strings into a structured database, and visualizes the insights instantly on an interactive web dashboard.

### ⚙️ How It Works (The Data Pipeline)
1. **The Log Generator (`generator.py`):** Simulates real-world user traffic by generating random server requests (IPs, URLs, and HTTP Status Codes) and writing them into a live `server.log` file every second. *(Note: In production, this generator is replaced by an actual live server like Nginx or Apache).*
2. **The Smart Parser (`backend/parser.py`):** Continuously monitors the log file using a `tail -f` logic. It uses **Regular Expressions (Regex)** to extract raw log text into distinct components (IP, Timestamp, Method, URL, Status Code) and saves them into an **SQLite database (`logs.db`)**.
3. **The FastAPI Backend (`backend/main.py`):** Acts as a secure **API Bridge** between the raw database and the user interface. It queries the database to calculate total requests, status code distributions, and top visited URLs, then serves this data as a standardized **JSON** payload.
4. **The Web Frontend (`frontend/index.html`):** A responsive web interface powered by **Chart.js** that sends fetch requests to the API every 2 seconds, dynamically updating charts and metrics in real-time.

### 🌐 What are HTTP Status Codes?
* **200 (OK):** The request was successful, and the page loaded perfectly.
* **404 (Not Found):** The user attempted to access a broken link or a non-existent page.
* **500 (Internal Server Error):** A backend crash or database error occurred during the process.

---

## 🇸🇦 الوصف باللغة العربية

### 📝 نبذة عن المشروع
هذا المشروع عبارة عن **خط إنتاج ومعالجة بيانات متكامل (Full-Stack Data Engineering Pipeline)** يعمل في الوقت الفعلي لمراقبة أداء السيرفرات، تتبع الطلبات المستلمة، وتحليل سلوك الزوار حياً.

بدلاً من قراءة ملفات السجلات الثابتة، يقوم هذا النظام بمعالجة البيانات ديناميكياً فور تولدها، وتفكيك النصوص العشوائية وحفظها في قاعدة بيانات منظمة، ثم عرضها مباشرة في لوحة تحكم رسومية تفاعلية.

### ⚙️ كيف يعمل المشروع؟ (رحلة تدفق البيانات)
1. **مولد السجلات (`generator.py`):** يقوم بمحاكاة زيارات وحركة مرور حقيقية للموقع عبر توليد طلبات عشوائية (عناوين IP، روابط صفحات، وأكواد حالة) وكتابتها ثانية بثانية داخل ملف `server.log`. *(ملاحظة: في بيئة العمل الحقيقية يتم حذف هذا المولد وربط النظام بسيرفر حقيقي مثل Nginx أو Apache).*
2. **المعالج الذكي (`backend/parser.py`):** يجلس في حالة استماع دائم لملف السجلات. يستعين بـ **التعبيرات النمطية (Regex)** لتفكيك الأسطر النصية المعقدة وفرزها (آي بي، وقت، رابط، كود الحالة) ومن ثم إدخالها مرتبة داخل قاعدة بيانات **SQLite (`logs.db`)**.
3. **خادم الـ API (`backend/main.py`):** يمثل **جسر الربط الآمن** المبني بإطار عمل **FastAPI**. يقوم بقراءة البيانات المعالجة من قاعدة البيانات وحساب الإحصائيات (إجمالي الطلبات، توزيع الأكواد، الصفحات الأكثر زيارة) ويغلفها في صيغة **JSON** الموحدة لإرسالها عبر الشبكة.
4. **الواجهة الأمامية (`frontend/index.html`):** لوحة تحكم تفاعلية مصممة بالـ HTML ومستعينة بمكتبة **Chart.js** الرسومية. تقوم بالاتصال بالـ API تلقائياً كل ثانيتين عبر أمر `fetch` لتحديث العدادات وتحريك الأعمدة البيانية حياً أمام المستخدم.

### 📊 ما هي أكواد الحالات الظاهرة في الرسم البياني؟ (HTTP Status Codes)
* **كود 200 (OK):** يعني نجاح الطلب؛ الزائر طلب صفحة وفتحت معه بشكل سليم تماماً.
* **كود 404 (Not Found):** يعني أن الصفحة غير موجودة؛ الزائر حاول الدخول لرابط تالف أو غير مدعوم.
* **كود 500 (Internal Server Error):** خطأ داخلي في السيرفر؛ حدث انهيار أو مشكلة برمجية في كود الخلفية منعته من تلبية الطلب.

---

### 🛠️ Tech Stack | التقنيات المستخدمة
* **Backend:** Python 3.13, FastAPI, Uvicorn
* **Database:** SQLite3
* **Data Processing:** Regular Expressions (Regex)
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API, Chart.js)# Log-Analysis-Dashboard
