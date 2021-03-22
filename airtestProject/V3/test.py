# createtime:2021/3/12 15:47
# user:luoli
# project:airtestProject
class aa:
    def bb(self):
        print(1)

if __name__ == '__main__':
    a=aa()
    a.__dict__['lalal']='lalla'
    s=a.__dict__
    print(s)