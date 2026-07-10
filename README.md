# genpark-commerce-subscription-billing-skill

> **GenPark AI Agent Skill** -- # Commerce Subscription Billing & Dunning Skill

This repository contains the **Commerce Subscription Billing & Dunning Skill** — an agent configuration skill config (`skill.json`), a production-ready Python SDK client (`subscription_billing.py`), and executable verification tests. It is designed to compute subscriber payment offsets, track collection failures (dunning), and format Stripe API payloads.

---

## 🚀 Capabilities

* **Dunning State Resolutions:** Automatically tags warning levels (`past_due_warning_1`, `past_due_warning_2_grace`, `suspended_canceled`) depending on billing retry loops.
* **Interval Date Mathematics:** Supports variable billing cycles (month or year offsets) to align dates.
* **Payload Compilations:** Generates standard anchors and metadata fields compatible with Stripe Subscription APIs.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 SDK Usage Reference

```python
from subscription_billing import SubscriptionBillingClient

client = SubscriptionBillingClient()

result = client.process_lifecycle(
    customer_id="cus_123",
    plan_id="plan_abc",
    start_date_str="2026-06-01",
    interval="month",
    failures=0
)

print(result["next_billing_date"])
```

---

## 📜 License
This project is licensed under the MIT License.