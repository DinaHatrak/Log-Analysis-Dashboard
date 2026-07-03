from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

app = FastAPI(title="Log Analysis API")

# السماح للواجهة الأمامية (Frontend) بالاتصال بالـ API دون قيود
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحديد مسار قاعدة البيانات تلقائياً في نفس المجلد
DB_PATH = os.path.join(os.path.dirname(__file__), "logs.db")

@app.get("/api/stats")
def get_stats():
    # التحقق من وجود قاعدة البيانات قبل محاولة القراءة منها
    if not os.path.exists(DB_PATH):
        return {"error": "Database not initialized yet. Please run parser first."}
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. حساب إجمالي عدد الطلبات المستلمة
    cursor.execute("SELECT COUNT(*) FROM server_logs")
    total_requests = cursor.fetchone()[0]
    
    # 2. حساب توزيع أكواد الحالة (مثل 200, 404, 500) وعدد تكرار كل كود
    cursor.execute("SELECT status, COUNT(*) FROM server_logs GROUP BY status")
    status_rows = cursor.fetchall()
    status_distribution = [{"status": r[0], "count": r[1]} for r in status_rows]
    
    # 3. جلب أكثر 5 عناوين (URLs) تم طلبها من السيرفر
    cursor.execute("SELECT url, COUNT(*) FROM server_logs GROUP BY url ORDER BY COUNT(*) DESC LIMIT 5")
    url_rows = cursor.fetchall()
    top_endpoints = [{"url": r[0], "count": r[1]} for r in url_rows]
    
    conn.close()
    
    # إرجاع البيانات المنظمة لتعرضها لوحة التحكم
    return {
        "total_requests": total_requests,
        "status_distribution": status_distribution,
        "top_endpoints": top_endpoints
    }
