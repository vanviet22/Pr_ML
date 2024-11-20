#pip install fastapi :đây là thư viện về api
#pip install uvicorn :một ASGI (Asynchronous Server Gateway Interface) server nhẹ và nhanh hỗ trợ các tính năng bất đồng bộ
#đóng vai trò như một cầu nối giữa ứng dụng và môi trường mạng, xử lý các yêu cầu HTTP và chuyển chúng đến ứng dụng FastAPI 
#lấy địa chỉ ở terminal chạy uvicorn tên file:tên biến của fastAPI vd bài này là uvicorn app:app
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from joblib import load
import os
app = FastAPI()
# current_dir = os.path.dirname(__file__) 
# model_path = os.path.join(current_dir, '../../results/output_files/B4_RFmodel_finetune.pkl')
# model = load(os.path.abspath(model_path))
model=load('D:/vietcpp/Project_ML/results/output_files/B4_RFmodel_finetune.pkl')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],# cho phep tat ca nguon   
    allow_methods=["*"],# cho phep tat ca ham
    allow_headers=["*"],
)

# Định nghĩa DTO (Data Transfer Object)
class DiabetesDTO(BaseModel):
    bloodPressure: float
    cholesterol: float
    BMI: float
    levelHealth: float
    smoker: float
    mind: float
    exercise: float
    sex: float
    age: int
    education: float
    income: float
    eatFruits: float
    eatVeggies: float


@app.get("/")
async def home():
    return "Đây là hệ thống dự đoán bệnh tiểu đường"
@app.post("/predict")
async def predict(data: DiabetesDTO):
    try:
        print("Dữ liệu nhận được từ client:", data.dict()) 
        # Chuyển DTO thành mảng NumPy
        input_data = np.array([[data.bloodPressure, data.cholesterol, data.BMI, data.levelHealth,
                                data.smoker, data.mind, data.exercise, data.sex, data.age,
                                data.education, data.income, data.eatFruits, data.eatVeggies]])
        # Dự đoán kết quả
        prediction = model.predict(input_data)
        result = int(prediction)
        #result=prediction
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("notebooks.inference.app:app", host="127.0.0.1", port=8000, reload=True)