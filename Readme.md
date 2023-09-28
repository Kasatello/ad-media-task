# Django Spend and Revenue Statistics Project

This Django project consists of two applications: `spend` and `revenue` for tracking and aggregating spend and revenue statistics.

## Usage

1. Install the required packages `pip install -r requirements.txt`.
2. Run migrations: `python manage.py migrate`.
3. Start the development server: `python manage.py runserver`.

### Spend Statistics API

- Endpoint: `/api/ad/spend_statistic/statistic`
- Description: Get spend statistics with aggregated sums of spend, impressions, clicks, conversion, and associated revenue.
- HTTP Method: GET

### Revenue Statistics API

- Endpoint: `/api/ad/revenue_statistic/statistic`
- Description: Get revenue statistics with aggregated sums of revenue and associated spend, impressions, clicks, conversion.
- HTTP Method: GET