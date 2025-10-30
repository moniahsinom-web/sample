class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_max(self):
        return max(self.data)

    def get_min(self):
        return min(self.data)

    def get_range(self):
        return self.get_max() - self.get_min()

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_summary(self):
        print("Data Summary:")
        print("-------------")
        print(f"Data: {self.data}")
        print(f"Mean: {self.get_mean():.2f}")
        print(f"Median: {self.get_median():.2f}")
        print(f"Max: {self.get_max()}")
        print(f"Min: {self.get_min()}")
        print(f"Range: {self.get_range()}")


# Example usage
data_list = [10, 20, 30, 40, 50, 60]
analyzer = DataAnalyzer(data_list)
analyzer.get_summary()
