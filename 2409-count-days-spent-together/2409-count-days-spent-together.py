class Solution:

    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Helper function to convert "MM-DD" to day of the year (1-indexed)
        def date_to_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            return sum(days_in_months[: month - 1]) + day

        # Find the overlapping range
        latest_arrival = max(arriveAlice, arriveBob)
        earliest_departure = min(leaveAlice, leaveBob)

        # Check if there is an overlap
        if latest_arrival > earliest_departure:
            return 0

        # Calculate duration
        start_day = date_to_day_of_year(latest_arrival)
        end_day = date_to_day_of_year(earliest_departure)

        return end_day - start_day + 1