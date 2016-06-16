import os

import urllib.request
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ET

class GetData:
    key = "f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D"
    url = "http://data.ex.co.kr/exopenapi/business/frugalStationInfo?serviceKey=f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D&type=xml"
    url2 = "http://data.ex.co.kr/exopenapi/business/lpgServiceAreaInfo?serviceKey=f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D&type=xml"

    def main(self):
        self.tree = etree.parse("data.xml")
        self.root = self.tree.getroot()
        self.tree2 = etree.parse("data2.xml")
        self.root2 = self.tree2.getroot()

        self.location_list1 = []
        self.location_list2 = []
        self.serviceAreaName1 = []
        self.serviceAreaName2 = []

        self.check1 = False
        self.check2 = False

    def save(self):
        xml = urllib.request.urlopen(self.url).read()
        f = open("data.xml", "wb")
        f.write(xml)
        f.close()
################################################
        xml2 = urllib.request.urlopen(self.url2).read()
        f = open("data2.xml","wb")
        f.write(xml2)
        f.close()
        pass

    def PrintChip(self):
        for a in self.root.iter("list"):
            if(self.check1 == False):
                self.location_list1.append(a.findtext("location"))
                self.serviceAreaName1.append(a.findtext("serviceAreaName"))
                print(a.findtext("location"))
                print(a.findtext("serviceAreaName"))
            else:
                print(a.findtext("location"))
                print(a.findtext("serviceAreaName"))

            print(a.findtext("oilCompany"))
            print(a.findtext("routeCode"))
            print(a.findtext("routeName"))
            print(a.findtext("serviceAreaCode"))
            print("-----------------------------------")

    def PrintLPG(self):
        for a in self.root2.iter("list"):
            if(self.check2 == False):
                self.location_list2.append(a.findtext("location"))
                self.serviceAreaName2.append(a.findtext("serviceAreaName"))
                print(a.findtext("location"))
                print(a.findtext("serviceAreaName"))
            else:
                print(a.findtext("location"))
                print(a.findtext("serviceAreaName"))

            print(a.findtext("oilCompany"))
            print(a.findtext("routeCode"))
            print(a.findtext("routeName"))
            print(a.findtext("serviceAreaCode"))

            print("-----------------------------------")

    def locate(self, num):
        s = "self.location_list" + str(num)

        if(num == 1):
            for i in range(0, len(s)):
                print(self.location_list1[i])
        else:
            for i in range(0, len(s)):
                print(self.location_list2[i])


        pass


if __name__ == "__main__":
    g_data = GetData()

    g_data.save()
    g_data.main()

    while True:
        #os.system("cls")

        print("안녕하세요. 주유소를 친절하게 찾아드리겠습니다.")
        print("메뉴를 선택해주세요.")
        print("1. 알뜰 주유소")
        print("2. LPG 주유소")
        print("3. 거리순 주유소 찾기")
        print("4. 종료")

        select = input("선택 : ")

        finder = str()

        if ('4' == select):
            break

        elif ('1' == select):
            g_data.PrintChip()
            if(g_data.check1 == False):
                g_data.check1 = True



        elif ('2' == select):
            g_data.PrintLPG()
            if(g_data.check2 == False):
                g_data.check2 = True

        elif('3' == select):
            finder = input("알뜰? LPG? 검색 : ")

            if(finder == "알뜰"):
                for i in range(0, len(g_data.serviceAreaName1)):
                    print("알뜰 주유소" + g_data.serviceAreaName1[i] + " 는 " + g_data.location_list1[i] + "m 지점에 있습니다.")

            elif((finder == "LPG") or (finder == "lpg")):
                for i in range(0, len(g_data.serviceAreaName2)):
                    print("LPG 주유소" + g_data.serviceAreaName2[i] + " 는 " + g_data.location_list2[i] + "m 지점에 있습니다.")

            else:
                continue

        else:
            continue
