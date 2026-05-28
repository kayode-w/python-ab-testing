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
**Groups:** Group A = basic plan, Group B = standard plan
**Metric:** Number of transactions per user

### Test 2 — KYC Verification
**Question:** Do KYC-verified users transact more than non-verified users?
**Tables used:** `users`, `transactions`
**Groups:** Group A = not KYC verified, Group B = KYC verified
**Metric:** Number of transactions per user

### Test 3 — Device Type
**Question:** Do iOS users perform more in-app events than Android users?
**Tables used:** `events`
**Groups:** Group A = Android, Group B = iOS
**Metric:** Number of events per user

---

## Project Structure

```
python_ab_test_project/
├── main.py          # entry point — runs the full pipeline
├── db_conn.py       # database connection
├── analysis.py      # statistical test functions
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

