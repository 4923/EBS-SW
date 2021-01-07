#터틀 임포트
import turtle

# 1. begin_fill은 그리기 직전에 호출
turtle.color("black", "red") # 선은 검은색, 채우기는 빨강색
turtle.begin_fill() # 채우기 시작
turtle.circle(80) # 반지름 80인 원
turtle.circle(80, steps =4) # 반지름 80인원, 스탭
turtle.end_fill() # 채우기 끝

#2. set_heading 은 터틀의 방향을 결정
turtle.setheading(90)
turtle.heading()

#3. goto는 주어진 좌표로 터틀을 이동
turtle.goto(200,0)

#4. 펜을 들고 움직이면 그려지지 않음
turtle.penup()
turtle.goto(-200,0)



turtle.getscreen()._root.mainloop()
