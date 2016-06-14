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

    def location_print(self):       # 위치만 나타내기 ㅋㅋㅋ

        for a in self.root.iter("list"):
            print()
            print(("위치 :"),a.findtext("location"))
        pass

    def test_print(self):
        print(" 1. 알뜰 주유소")
        for a in self.root.iter("list"):
            print(a.findtext("location"))
            print(a.findtext("oilCompany"))
            print(a.findtext("routeCode"))
            print(a.findtext("routeName"))
            print(a.findtext("serviceAreaCode"))
            print(a.findtext("serviceAreaName"))
            print("-----------------------------------")

        print("------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------")

        print(" 2. LPG 주유쇼")
        for a in self.root2.iter("list"):
            print(a.findtext("location"))
            print(a.findtext("oilCompany"))
            print(a.findtext("routeCode"))
            print(a.findtext("routeName"))
            print(a.findtext("serviceAreaCode"))
            print(a.findtext("serviceAreaName"))
            print("-----------------------------------")




g_data = GetData()

g_data.save()
g_data.main()

#g_data.location_print() #위치만 나타내기
g_data.test_print()