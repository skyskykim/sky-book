import urllib.request
import xml.etree.ElementTree as etree



class GetData:

    key ="f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D"
    url ="http://openapi.mpm.go.kr/openapi/service/RetrievePblinsttEmpmnInfoService/getClsfList"


# 이거는 문화 뭐있는지 그거
#  문화  key = "f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D"
 #  문화 url = "http://www.culture.go.kr/openapi/rest/cultureartspaces?_wadl&type=xml"

   # 이거는 곤충 인증키 #key = "f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D"
  #이거는 곤충 url #  url = "http://api.nature.go.kr/openapi/service/rest/KpniService/systemSearch?st=1&ServiceKey=f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D&region=5%EC%9B%94&type=xml"
    # url
   # url = "http://api.nature.go.kr/openapi/service/rest/KpniService/systemSearch?ServiceKey=f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D&region= 5%EC%9B%94&_type=xml"
    # http://api.nature.go.kr/openapi/service/rest/KpniService/systemSearch?ServiceKey=f3m3RPXAk63BbSomWLgUxBxPusrwo891R5kEPyezn2AgYQYS7gsGUKK8j5prylR%2B%2FkegJnDYQCH1GNxLOocbsg%3D%3D&region= 5%EC%9B%94&_type=xml


    def main(self):

        xml = urllib.request.urlopen(self.url).read()
        f = open("data.xml", "wb")
        f.write(xml)
        f.close()

        #self.tree = etree.parse("data.xml")
        #self.root = self.tree.getroot()


        pass

    def save(self):


        pass

    def test_print(self):

        # for a in self.root.iter("list"):
        #     print(a.findtext("batchMenu"))
        #     print(a.findtext("direction"))
        #     print(a.findtext("routeCode"))
        #     print(a.findtext("routeName"))
        #     print(a.findtext("salePrice"))
        #     print(a.findtext("serviceAreaCode"))
        #     print(a.findtext("serviceAreaName"))



        pass

g_data = GetData()

g_data.main()