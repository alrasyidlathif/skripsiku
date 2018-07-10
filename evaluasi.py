def km(individu, titik):
# evaluation (kmeans)
    centroid = copy.deepcopy(individu)
    point = copy.deepcopy(titik)

    mm = len(centroid)
    nn = len(point)

    kluster_i = []
    kluster_imin1 = []
    for i in range(mm-3):
        kluster_i.append([])
        kluster_imin1.append([])

    jarak = []
    for i in range(mm-3):
        jarak.append(float('inf'))

    while True:
        for i in range(nn):
            for j in range(mm-3):
                jarak[j] = ((point[i][0] - centroid[j+1][0])**2
                + (point[i][1] - centroid[j+1][1])**2)**(1/2)
        
            for k in range(mm-3):
                if min(jarak) == jarak[k]:
                    kluster_i[k].append(point[i])

        z = 0
        for i in range(mm-3):
            if kluster_i[i] == kluster_imin1[i]:
                z = z + 1
        if z == mm-3:
            break
        
        for i in range(mm-3):
            if len(kluster_i[i]) != 0:
                a = 0 
                b = 0 
                for j in range(len(kluster_i[i])):
                    a = a + kluster_i[i][j][0]
                    b = b + kluster_i[i][j][1] 
                centroid[i+1] = [a/len(kluster_i[i]), b/len(kluster_i[i])]#,

        for i in range(mm-3):
            kluster_imin1[i] = kluster_i[i] + []

        kluster_i = []
        for i in range(mm-3):
            kluster_i.append([])

    return kluster_i, centroid


def RandIndex(titik, klusterbenar, klusterhasil):
# fungsi rand index
    n = len(titik)
    # print(klusterhasil)
    #nomor kluster
    nobenar = []
    for i in range(n):
        for j in range(len(klusterbenar)):
            if titik[i] in klusterbenar[j]:
                nobenar.append(j)
                break
    nohasil = []
    for i in range(n):
        for j in range(len(klusterhasil)):
            if titik[i] in klusterhasil[j]:
                nohasil.append(j)
                break

    # perhitungan a b c d
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (nobenar[i] == nobenar[j]) and (nohasil[i] == nohasil[j]):
                a = a + 1
            elif (nobenar[i] == nobenar[j]) and (nohasil[i] != nohasil[j]):
                b = b + 1
            elif (nobenar[i] != nobenar[j]) and (nohasil[i] == nohasil[j]):
                c = c + 1
            elif (nobenar[i] != nobenar[j]) and (nohasil[i] != nohasil[j]):
                d = d + 1
            else:
                print('ada kesalahan')

    # rand index
    RI = (a+d)/(a+b+c+d)
    return RI


def aa(x, himklus):
# def fungsi a() dan b() untuk mencari silhouete
    jar = 0

    for klus in himklus:
        if x in klus:
            if len(klus) == 1:
                return 0
            else:
                for z in klus:
                    if z != x:
                        dis = ((x[0] - z[0])**2 + (x[1] - z[1])**2)**(1/2)

                        jar = jar + dis

                return jar / ( len(klus)-1 )


def bb(x, himklus):
# def fungsi a() dan b() untuk mencari silhouete
    nilaimin = []
    for klus in himklus:
        jar = 0
        if x not in klus and len(klus) != 0:
            for z in klus:
                dis = ((x[0] - z[0])**2 + (x[1] - z[1])**2)**(1/2)

                jar = jar + dis

            nil = jar / len(klus)
            nilaimin.append(nil)

    if len(nilaimin) > 0:
        return min(nilaimin)
    else:
        return 0
