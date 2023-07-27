import csv

class DataProcessor:
    def __init__(self):
        pass

    def save_data_to_csv(self, data_dict):
        filepath = "data.csv"
        headings = ["First Name", "Last Name", "Title", "Age", "Nationality", "Courses", "Semesters", "Registration Status"]
        data = [data_dict[heading.lower()] for heading in headings]

        with open(filepath, "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write headings if the file is empty
            if csvfile.tell() == 0:
                csv_writer.writerow(headings)

            csv_writer.writerow(data)

        print("Data appended to CSV file:", filepath)
