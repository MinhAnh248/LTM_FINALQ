# ai_module.py (local, dùng DB, dữ liệu nhập: danh_muc, so_tien, mo_ta)
from collections import defaultdict, OrderedDict
from datetime import datetime
import statistics

def full_financial_analysis(transactions):
    """
    Nhận list giao dịch từ DB (dict: so_tien, mo_ta, danh_muc, ngay)
    Nếu không có 'ngay', lấy datetime.utcnow()
    Trả về dự đoán chi tiêu, summary, cảnh báo, gợi ý
    """
    if not transactions:
        return {"status": "error", "error": "Không có dữ liệu"}

    month_map = defaultdict(float)
    parsed_items = []

    for tx in transactions:
        try:
            dt = tx.get('ngay') or tx.get('created_at') or datetime.utcnow()
            if isinstance(dt, str):
                dt = datetime.fromisoformat(dt)
            amt = float(tx.get('so_tien', 0))
            category = tx.get('danh_muc') or tx.get('mo_ta', 'khác')
            category = str(category).lower().strip() or 'khác'
            month = dt.strftime('%Y-%m')
            month_map[month] += amt
            parsed_items.append((dt, amt, category))
        except:
            continue

    sorted_months = OrderedDict(sorted(month_map.items()))
    history = list(sorted_months.values())
    history_months = list(sorted_months.keys())

    # Dự đoán tháng tiếp theo
    n = len(history)
    if n <= 1:
        pred = history[-1] if n else 0.0
        method = "not_enough_data"
    else:
        x_mean = (n-1)/2
        y_mean = sum(history)/n
        num = sum((i-x_mean)*(y-y_mean) for i,y in enumerate(history))
        den = sum((i-x_mean)**2 for i in range(n))
        if den == 0:
            pred = history[-1]
            method = "flat_data"
        else:
            a = num/den
            b = y_mean - a*x_mean
            pred = max(a*n + b, 0)
            method = "linear_regression"

    # Summary theo category
    cat_map = defaultdict(float)
    for _, amt, cat in parsed_items:
        cat_map[cat] += amt
    cat_map = OrderedDict(sorted(cat_map.items(), key=lambda x: -x[1]))

    # Cảnh báo chi tiêu tăng đột biến
    spikes = []
    month_cat = defaultdict(lambda: defaultdict(float))
    for dt, amt, cat in parsed_items:
        month_cat[dt.strftime('%Y-%m')][cat] += amt
    months = sorted(month_cat.keys())
    if len(months) >= 2:
        cats = {c for m in months for c in month_cat[m]}
        for cat in cats:
            values = [month_cat[m].get(cat,0.0) for m in months]
            last = values[-1]
            baseline = statistics.median(values[:-1])
            if baseline>0 and last/baseline >=1.5:
                spikes.append({
                    "category": cat,
                    "last_month": last,
                    "baseline": baseline,
                    "message": f"Chi tiêu '{cat}' tăng mạnh {round(last/baseline,2)}x so với trước."
                })

    # Gợi ý chi tiêu
    total = sum(history) or 1
    advice = []
    try:
        for cat, amt in list(cat_map.items())[:5]:
            pct = amt/total*100
            if pct >= 40:
                advice.append(f"Chi tiêu '{cat}' chiếm {pct:.1f}% — nên giảm xuống 25-30%.")
            elif pct >= 20:
                advice.append(f"Chi tiêu '{cat}' chiếm {pct:.1f}% — nên kiểm soát.")
        months_count = len(set([dt.strftime('%Y-%m') for dt,_,_ in parsed_items])) or 1
        avg_month = total / months_count
        advice.append(f"Trung bình mỗi tháng chi {avg_month:.0f}. Hãy dành 10% để tiết kiệm.")
    except:
        pass

    hist_list = [{"month": m, "amount": round(v,2)} for m,v in zip(history_months, history)]

    return {
        "status": "ok",
        "summary": {
            "months_count": len(history),
            "total_history_amount": round(total,2),
            "last_month": hist_list[-1] if hist_list else None
        },
        "monthly_prediction": {
            "predicted_amount": round(pred,2),
            "method": method,
            "history": hist_list
        },
        "category_summary": {k: round(v,2) for k,v in cat_map.items()},
        "category_warnings": spikes,
        "advice": advice
    }
