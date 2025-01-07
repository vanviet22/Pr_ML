I)Cấu trúc folder<br>
  Project_ML/<br>
		  ├── .git<br>
		  ├── .idea<br>
		  ├── data<br>
		  │     └──raw<br>
		  │     └── processed<br>
		  │     └── img<br>
		  ├──documentation<br>
		  ├── notebooks<br>
		  │      └──exploratory<br>
		  │      └── inference<br>
		  │      └── imgmodeling<br>
		  ├── results<br>
		  │      └──img<br>
		  │      └──output_files<br>
		  └── scripts<br>
II) Dư án</br>
- Đây là bài toán phân lớp của học có giám sát.</br>
- Sử dụng bộ data '/kaggle/input/diabetes-health-indicators-dataset /diabetes_binary_5050split_health_indicators_BRFSS2015.csv'.Đây là Dataset lấy từ Kaggle, là một tập dữ liệu sạch gồm 70.692 phản hồi khảo sát từ chương trình BRFSS2015 của CDC. Tập dữ liệu có sự phân chia cân bằng 50-50 giữa những người không mắc bệnh tiểu đường và những người bị tiền tiểu đường hoặc tiểu đường.Dữ liệu hoàn toàn là số và có định dạng.Với biến mục tiêu là Diabetes_binary và 21 biến đặc trưng.</br>
- Thuật toán: Random Forest, logistic regression và kỹ thuật ensemble learning Stacking.</br>
- Chúng tôi khám phá và tiền xử lí dữ liệu sau đó xây dựng các mô hình.</br>
- Độ chính xác cao nhất đạt được là 75,21% của thuật toán Randomforest sau khi xử lí dữ liệu và fine-tune hyperparameter.</br>
- Thiết kế giao diện web và sử dụng fast API để làm API.
