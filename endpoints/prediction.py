from fastapi import APIRouter, Request
import pickle
import lifetimes
from api_functions import ResponseModel, ErrorResponseModel

router = APIRouter()

# Prediction
@router.post("/predict", name="Prediction", description="Returns churn prediction")
async def prediction(request: Request):
    """Returns churn prediction"""

    new_request_original = await request.json()

    try:
        new_request = eval(new_request_original)

        with open('models/model_pkl' , 'rb') as f:
            model = pickle.load(f)

        print('model_loaded')

        prediction = model.conditional_probability_alive(
        frequency = float(new_request['frequency']),
        recency = float(new_request['recency']),
        T = float(new_request['T']))

        print('prediction')
        print(prediction)

        return ResponseModel({"prob_alive":str(prediction[0])}, "success")
    except Exception:
        return ErrorResponseModel(503, {"INVALID REQUEST": new_request_original})