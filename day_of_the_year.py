class Solution(object):
    def dayOfYear(self, date):
        import datetime
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return input_date.timetuple().tm_yday
