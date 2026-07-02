from dateutil.relativedelta import relativedelta




class Worker:

    def __init__(self):
        pass


    def recurrence_frequecy(
        self,
        recurrence_start,
        frequency
    ):

        recur_at = None

        if frequency == "annual":
            recur_at = recurrence_start + relativedelta(years=1)

        if frequency == "bi-annual":
            recur_at = recurrence_start + relativedelta(months=6)

        if frequency == "monthly":
            recur_at = recurrence_start + relativedelta(months=1)

        if frequency == "weekly":
            recur_at = recurrence_start + relativedelta(weeks=6)

        if frequency == "fortnight":
            recur_at = recurrence_start + relativedelta(weeks=2)

        if frequency == "daily":
            recur_at = recurrence_start + relativedelta(days=1)

        return recur_at

        


