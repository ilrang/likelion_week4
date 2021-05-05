	
class Member:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def show_info(self):
        print("이름은", self.name)
        print("학과는", self.major)

    def work(self):
        print(self.name,"얼른 일하세요 일")

    def order_time(self, time):
        print("{0}씨 {1}까지 다 해오세요".format(self.name, time))
        
class HackathonMember(Member):
    def __init__(self,name,major,position):
        Member.__init__(self,name,major)
        self.position = position

    def show_info(self):
        print("이름은", self.name)
        print("학과는", self.major)
        print("포지션은", self.position)

member1 = HackathonMember("임영빈","컴퓨터공학과","프론트엔드")
member2 = HackathonMember("김민지","문화콘텐츠문화경영학과","디자인")

member1.show_info()
member1.work()
member2.order_time("10시")