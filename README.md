1. Clone project về local <br />
git clone https://github.com/baquyptit2001/StudyEnglish.git <br />
2. Sau khi clone về mọi người cd StudyEnglish và tạo một branch mới và làm bình thường  <br />
git checkout -b [tên branch] <br />
3. Mỗi khi push thì mọi người sẽ checkout sang nhánh main và pull code lại rồi mới thực hiện push <br />
git checkout main <br />
git pull <br />
git checkout [nhánh của mọi người] <br />
git merge main <br />
4. Mọi người run app bằng <br />
python manage.py runserver --insecure<br />
5. Mỗi lần pull code mọi người check out về nhánh của mình rồi git merge main

# Tuyệt đối không merge vào nhánh main #


#Translate
App Translate sử dùng thư viên googletran để dịch từ 
Cách cài  pip install googletrans==3.1.0a0
phần speech to text sử dụng web speech api của JS
phân text to speech sử dung module  ResponsiveVoice (nguồn : https://responsivevoice.org/text-to-speech-languages)#

