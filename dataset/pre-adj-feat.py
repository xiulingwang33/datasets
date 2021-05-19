import pickle as pk
import networkx as nx
DATASET = 'facebook'
# DATASET='g+'
# DATASET='dblp'

###### "ginfo" in the following are to extract the gender information for each node in graph


G_EGO_USERS=['3980']


for ego_user in G_EGO_USERS:

    feat_dir = './' +DATASET +'/'+ str(ego_user) + '-adj-feat.pkl'
    f2 = open(feat_dir, 'rb')

    adj, ft = pk.load(f2, encoding='latin1')
    # print(adj)
    # print(np.shape(adj))
    # print(ft)
    # print(np.shape(ft))


    g = nx.Graph(adj)
    # print(g.nodes)
    # print(g.edges)

    if (DATASET == 'g+'):# gplus

        for i, n in enumerate(g.nodes()):
            info = ft[n][:3].tolist()

    elif(DATASET == 'dblp'):# dblp

        for i, n in enumerate(g.nodes()):
            info = ft[n].tolist()

    elif (DATASET == 'fb'): # facebook
        f=open('./' + DATASET +'/' +'feature_map.txt','r')
        invert_index=eval(f.readline())
        f.close()
        #g1_index=invert_index[('gender',77)]
        #g2_index = invert_index[('gender', 78)]
        gindex = invert_index[('gender', 77)]

        for i, n in enumerate(g.nodes()):
            info = ft[n][gindex:gindex + 2].tolist()

            if sum(info) == 0:
                ginfo = 0
                # rm.append(n)
            elif sum(info) == 1:
                ginfo = info.index(1) + 1
                # if ginfo == 1:
                #     count_nodes[0] += 1
                # elif ginfo == 2:
                #     count_nodes[1] += 1
            else:
                # print(n)
                ginfo = -1
                # rm.append(n)
            g.nodes[n]['gender'] = ginfo
            print(g.nodes[1])



