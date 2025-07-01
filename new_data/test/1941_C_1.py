for i in range(int(input())):
    input()
    s = input()
    flag = 0
    length = len(s)
    mapie_s = filter(None, s.split("mapie"))
    s1 = ''.join(mapie_s)
    length_s1 = length - len(s1)
    flag += length_s1//5
    map_s = filter(None, s1.split("map"))
    s2 = ''.join(map_s)
    pie_s = filter(None, s2.split("pie"))
    s3 = ''.join(pie_s)
    length_s3 = len(s3)
    print((len(s1) - length_s3)//3 + flag)