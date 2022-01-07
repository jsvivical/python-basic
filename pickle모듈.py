# pickle 모듈
# 필요한 객체를 파일로 저장해서 영속화시키는 모듈

import pickle
# 객체를 파일로 저장
f = open("list.pickle", "wb")
test = [1, 2, 3, 4, 5]
pickle.dump(test, f)  # test객체를 f파일에 저장
f.close()

# 저장한 객체 불러오기
f = open("list.pickle", "rb")
test_pickle = pickle.load(f)
print(test_pickle)
f.close()
