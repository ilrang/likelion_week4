	
class Member:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def show_info(self):
        print("이름은", self.name)
        print("학과는", self.major)

    def work(self):
        print(self.name,"일하세요 일")

    def order_time(self, time):
        print("{0}씨 {1}까지 다 해오세요".format(self.name, time))

#객체 생성
member1 = Member("임영빈", "컴퓨터공학과")
member2 = Member("김민지", "문화콘텐츠문화경영학과")
member3 = Member("김현조", "정보통신공학과")
member4 = Member("김재원", "전자공학과")
member5 = Member("한지훈", "컴퓨터공학과")

#영빈오빠 자기소개시키기
member1.show_info()
#민지언니 일시키기
member2.work()
#현조언니 재촉하기
member3.order_time("9시")
#김재원 이름출력
print(member4.name)
#한지훈 과 출력
print(member5.major)