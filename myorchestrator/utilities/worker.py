from dateutil.relativedelta import relativedelta




class Worker:

    def __init__(self):
        pass


    def recurrence_frequecy(
        self,
        recurrence_start,
        frequency
    ):
        if frequency == "annually":
            recur_at = recurrence_start + relativedelta(years=1)
            return recur_at


