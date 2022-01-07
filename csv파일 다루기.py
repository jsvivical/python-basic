# csv 파일 객체 이용(읽기)
line_counter = 0
data_header = []
nation_list = []

with open("covid_19_data.csv", "r") as covid_data:
    while True:
        data = covid_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            nation_list.append(data.split(","))

        line_counter += 1

print("header : ", data_header)
for i in range(0, 10):
    print("data : ", i, nation_list[i][2])
print(len(nation_list))

# csv파일 쓰기
with open("covid_editted.csv", "w") as editted:
    for i in range(len(nation_list)):
        editted.write(
            str(i) + " " + "".join(nation_list[i][2]).strip("\n") + "\n")
