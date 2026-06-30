import os
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

class SubscriptionBillingClient:
    """
    Production-grade subscription billing coordinator. Computes next payment dates,
    tracks dunning states, and formats Stripe API payloads.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("BILLING_API_KEY")

    def process_lifecycle(
        self,
        customer_id: str,
        plan_id: str,
        start_date_str: str,
        interval: str,
        failures: int
    ) -> Dict[str, Any]:
        """
        Calculates subscription dates, dunning states, and structures mock payment gateway payload.
        """
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {start_date_str}. Use YYYY-MM-DD")

        # 1. Compute next billing date
        if interval == "month":
            # Simple 30 day offset
            next_billing = start_date + timedelta(days=30)
        else:
            # 365 day offset
            next_billing = start_date + timedelta(days=365)

        # 2. Determine dunning state
        if failures == 0:
            dunning = "active"
        elif failures == 1:
            dunning = "past_due_warning_1"
        elif failures == 2:
            dunning = "past_due_warning_2_grace"
        else:
            dunning = "suspended_canceled"

        # 3. Stripe Subscription payload draft
        action_payload = {
            "customer": customer_id,
            "items": [{"plan": plan_id}],
            "billing_cycle_anchor": int(next_billing.timestamp()),
            "proration_behavior": "create_prorations",
            "metadata": {
                "dunning_failures": failures,
                "lifecycle_status": dunning
            }
        }

        return {
            "next_billing_date": next_billing.strftime("%Y-%m-%d"),
            "dunning_status": dunning,
            "action_payload": action_payload
        }
