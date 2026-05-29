# Python A/B Testing Project

A hands-on A/B testing pipeline built in Python. Connects to a PostgreSQL database, defines user groups from real data, runs statistical significance tests using scipy, and interprets results. Built as a learning project covering experimental design, p-values, and structured Python project layout.

---

## Project Objectives

- Pull real data from a PostgreSQL database using SQLAlchemy and pandas
- Define meaningful user groups based on existing data attributes
- Calculate a measurable metric for each group
- Run a statistical significance test (t-test) using scipy
- Interpret the p-value and determine whether results can be trusted

---

## The Three Tests

### Test 1 — Plan Type
**Question:** Do standard plan users make more transactions than basic plan users?
**Tables used:** `users`, `transactions`
**Groups:** basic / standard / premium
**Metric:** Number of transactions per user

| Comparison | p-value | Significant? |
|------------|---------|--------------|
| Basic vs Standard | 0.18 | No |
| Standard vs Premium | 0.60 | No |
| Basic vs Premium | 0.58 | No |

**Finding:** Plan tier has no statistically significant effect on transaction frequency. Basic, standard, and premium users transact at roughly the same rate.

---

### Test 2 — KYC Verification
**Question:** Do KYC-verified users transact more than non-verified users?
**Tables used:** `users`, `transactions`
**Groups:** kyc_verified = True / False
**Metric:** Number of transactions per user

| Comparison | p-value | Significant? |
|------------|---------|--------------|
| Verified vs Unverified | 0.65 | No |

**Finding:** KYC verification status does not predict how often a user transacts. Verified and unverified users behave almost identically in terms of transaction volume.

---

### Test 3 — Device Type
**Question:** Do iOS users generate more in-app events than Android users?
**Tables used:** `events`
**Groups:** iOS / Android
**Metric:** Number of events per user

| Comparison | p-value | Significant? |
|------------|---------|--------------|
| iOS vs Android | 0.14 | No |

**Finding:** No statistically significant difference between iOS and Android users. iOS showed a slight signal but not strong enough to act on with current data.

---

## Business Interpretation

All three tests returned non-significant results. This is a meaningful finding in a sense.

The factors we assumed would separate active users from inactive ones i.e. their plan tier, their verification status, their device  do not actually explain the difference in transaction behaviour. In a real business context, this would prompt the following recommendation:

> "Based on our analysis of 1,656 users across three A/B tests, we found no statistically significant difference in transaction behaviour when grouping users by plan type, KYC status, or device type. P-values ranged from 0.14 to 0.65, all above our 0.05 significance threshold.
>
> This tells us that the levers we assumed were driving engagement are not the real drivers. We recommend investigating behavioural factors — such as time since onboarding, number of sessions, or first transaction date — as these are more likely to explain variance in transaction volume. Investing resources in plan upgrades or KYC push campaigns is unlikely to move the transaction needle based on this data."

A non-significant result is not a failure. It removes assumptions and points the business toward better questions.

---

## Project Structure

```
python_ab_test_project/
├── main.py          # entry point — runs the full pipeline
├── db_conn.py       # database connection
├── analytics.py     # all statistical test functions
└── .env             # credentials (not committed to git)
```

---

## Stack

- Python 3.13
- pandas
- scipy
- SQLAlchemy
- PostgreSQL
- python-dotenv
