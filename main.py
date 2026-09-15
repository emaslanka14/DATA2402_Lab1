# this line imports some custom exceptions for use in this lab
# raise/handle them just like Exception, ValueError, or any other type of exception
from exceptions import TextFormatException, MissingValueException, MeasurementUnitException


def compute_BMI(weight: float, height: float) -> float:
    """
    compute body-mass-index:  weight / (mass**2)
    :param height: height in meters
    :param weight: weight in kg
    :return: BMI in kg/m**2
    """
    bmi = weight / (height ** 2)
    return float(bmi)


def parse_row(row: str) -> list:
  
    values = row.strip().split(",")

    exam_ID = int(values[0])
    Date = values[1]
    Patient_name = values[2]

    if "" in values:
        raise MissingValueException()

    try:
        exam_ID = int(values[0])
        weight = float(values[3])
        height = float(values[4])
    except ValueError:
        raise TextFormatException()

    if height > 3:
        raise MeasurementUnitException()
    
    return [exam_ID, Date, Patient_name, weight, height]


def main():
    
    input_file=open("data.csv", "r")

    output_file=open("output.csv", "w")

    output_file.write("Exam_ID,BMI\n")
    input_file.readline()  # skip the header row
    for row in input_file:
        exam_ID = row.strip().split(",")[0]
        try:
            exam_ID, Date, Patient_name, weight, height = parse_row(row)
            bmi = compute_BMI(weight, height)
            output_file.write(f"{exam_ID},{bmi:.2f}\n")
        except MissingValueException:
            print(f"Exam ID {exam_ID}: Missing Value")
        except MeasurementUnitException:
            print(f"Exam ID {exam_ID}: Measurement Unit Error")
        except TextFormatException:
            print(f"Exam ID {exam_ID}: Text Format Error")

    input_file.close()
    output_file.close()
        
main()