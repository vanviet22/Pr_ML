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
II) Tổng quan và lí do 
- Và y tế luôn là vấn đề lớn được quan tâm hàng đầu. Trong đó, bệnh tiểu đường là một bệnh không lây nhiễm nhưng Tổ chức Y tế Thế giới (WHO) coi là ưu tiên hàng đầu trong chiến lược chăm sóc sức khỏe cộng đồng. Tiểu đường là tình trạng mãn tính biểu hiện qua mức đường huyết cao do cơ thể thiếu insulin. Đây là một căn bệnh có tính chất xã hội cao tại nhiều quốc gia, phát triển nhanh chóng và gây ra nhiều ảnh hưởng nghiêm trọng đến sức khỏe con người.
- Việt Nam tuy không nằm trong top 10 quốc gia có tỷ lệ mắc bệnh tiểu đường cao, nhưng lại có tốc độ gia tăng bệnh thuộc hàng nhanh nhất. Đây là một trong những nguyên nhân tử vong hàng đầu tại Việt Nam, chỉ đứng sau bệnh tim và ung thư.
- Chẩn đoán bệnh là một thách thức lớn trong lĩnh vực y tế, đặc biệt là đối với bệnh tiểu đường. Cùng với sự phát triển của khoa học dữ liệu và trí tuệ nhân tạo (AI), chúng ta có thể khai thác và phân tích lượng lớn dữ liệu y tế nhờ các phương pháp machine learning (ML).
- Những hệ thống chẩn đoán thông minh này có độ chính xác cao, giúp phát hiện sớm nguy cơ mắc bệnh và từ đó giảm thiểu các biến chứng nguy hiểm. Bên cạnh đó, AI còn hỗ trợ cá nhân hóa liệu trình điều trị, mang lại hiệu quả tối ưu cho từng bệnh nhân.
- Với những lí do trên thì nhóm tôi quyết định xây dựng ứng dụng mô hình Meachine Learning để dự đoán nguy cơ mắc bệnh tiểu đường.</br>
III) Đề tài</br>
- Đây là bài toán phân lớp của học có giám sát.</br>
- Sử dụng bộ data '/kaggle/input/diabetes-health-indicators-dataset /diabetes_binary_5050split_health_indicators_BRFSS2015.csv'.Đây là Dataset lấy từ Kaggle, là một tập dữ liệu sạch gồm 70.692 phản hồi khảo sát từ chương trình BRFSS2015 của CDC. Tập dữ liệu có sự phân chia cân bằng 50-50 giữa những người không mắc bệnh tiểu đường và những người bị tiền tiểu đường hoặc tiểu đường.Dữ liệu hoàn toàn là số và có định dạng.Với biến mục tiêu là Diabetes_binary và 21 biến đặc trưng.</br>
- Thuật toán: Random Forest, logistic regression và kỹ thuật ensemble learning Stacking.</br>
- Chúng tôi khám phá và tiền xử lí dữ liệu dữ liệu đã sạch nên tôi xây dụng 3 mô hình với các thuật toán trên trước sau đó loại bỏ các đặc trưng không quan trọng đối với từng thuật toán .Sau đó fine-tune các mô hình và so sánh.</br>
- Độ chính xác cao nhất đạt được là 75,21% của thuật toán Randomforest sau khi xử lí dữ liệu và fine-tune hyperparameter.</br>
- Thiết kế giao diện web và sử dụng fast API để làm API để dự đoán.
