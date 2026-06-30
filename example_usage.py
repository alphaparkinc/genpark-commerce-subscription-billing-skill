import sys
import json
from subscription_billing import SubscriptionBillingClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Commerce Subscription Billing Agent Verification ===")
    client = SubscriptionBillingClient()

    # Scenario A: Healthy active subscriber
    print("\n--- Scenario A: Active Monthly Subscription ---")
    result_a = client.process_lifecycle(
        customer_id="cus_H198A2f190",
        plan_id="price_monthly_zenith",
        start_date_str="2026-06-15",
        interval="month",
        failures=0
    )
    print(json.dumps(result_a, indent=2))

    # Scenario B: Failed payment subscriber in warning state
    print("\n--- Scenario B: Past Due Dunning Warning ---")
    result_b = client.process_lifecycle(
        customer_id="cus_K290B8a112",
        plan_id="price_yearly_zenith",
        start_date_str="2026-01-01",
        interval="year",
        failures=3
    )
    print(json.dumps(result_b, indent=2))

if __name__ == "__main__":
    main()
