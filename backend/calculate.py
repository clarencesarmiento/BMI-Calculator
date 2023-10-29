# Constant Variable
cm_to_m_conversion_factor = 100


def calculate_bmi(height_cm: float or int, weight_kg: float or int) -> float:
    """
    Function to calculate the Body Mass Index

    :param height_cm: float, height in centimeter.
    :param weight_kg: float
    :return: float, calculated Body Mass Index
    """

    # Check parameter's datatypes
    if not isinstance(height_cm, (float, int)) or not isinstance(weight_kg, (float, int)):
        raise TypeError("height_cm and weight_kg must be of type float or int")

    if height_cm <= 0 or weight_kg <= 0:
        return 0

    # Calculate BMI using the formula: weight / (height^2)
    bmi = weight_kg / ((height_cm / cm_to_m_conversion_factor) ** 2)

    return bmi


def get_bmi_category(bmi: float or int) -> str:
    """
    Function to get the Category based on the Body Mass Index.

    :param bmi: float, calculated Body Mass Index
    :return: str, category based on the calculated Body Mass Index
    """

    # Check parameter datatype
    if not isinstance(bmi, (float, int)):
        raise TypeError('bmi must be of type float or int')

    if bmi == 0:
        return 'Inhuman'
    elif bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal Weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'
