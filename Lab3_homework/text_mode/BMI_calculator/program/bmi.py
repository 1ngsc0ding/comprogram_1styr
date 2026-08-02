def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    bmi = weight / (height ** 2)
    return bmi


def adult_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Class 1 Obesity"
    elif bmi < 40:
        return "Class 2 Obesity"
    else:
        return "Class 3 Obesity (Severe Obesity)"


def child_bmi_status(percentile, bmi=None):
    if percentile < 5:
        return "Underweight"
    elif percentile < 85:
        return "Healthy Weight"
    elif percentile < 95:
        return "Overweight"
    elif bmi is not None:
        if bmi >= 40:
            return "Class 3 Obesity (Severe Obesity)"
        elif bmi >= 35:
            return "Class 2 Obesity"
        else:
            return "Obesity"
    else:
        return "Obesity"


def obesity_class_child(bmi, percentile):
    if percentile < 95:
        return None
    return child_bmi_status(percentile, bmi)