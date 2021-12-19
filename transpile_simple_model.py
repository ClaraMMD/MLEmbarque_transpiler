import joblib
import numpy as np

model = joblib.load('linear_regression.joblib')

def produce_linear_prediction_c_code(model):
    prediction_code = "float thetas[2] = {" + str(model.coef_[0]) + ", "+ str(model.coef_[1]) + "};"
    code = """
#include <stdlib.h>
#include <stdio.h>

float prediction(float *features, int n_features)
{
    float res = 0;\n    """ + prediction_code + """

    for (int i = 0; i < n_features; i++)
    {
        res += features[i] * thetas[i];
    }
    
    return res;
}

int main()
{
    float* features = calloc(2, sizeof(float));

    *features = 1.2;
    *(features + 1) = 0.4;

    printf("%f\\n", prediction(features, 2));
    return 1;
}    """

    return code

c_code = produce_linear_prediction_c_code(model)

f = open("main.c", "w")
f.write(c_code)

print(model.predict(np.array([[1.2, 0.4]])))
