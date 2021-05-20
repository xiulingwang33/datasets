import pickle as pk
import networkx as nx
DATASET = 'fb'
# DATASET='g+'
# DATASET='dblp'

###### "ginfo" in the following are to extract the gender information for each node in graph


G_EGO_USERS=['combined','0','106']


for ego_user in G_EGO_USERS:

    feat_dir = './' + str(ego_user) + '-adj-feat.pkl'
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

        gindex=0

    elif(DATASET == 'dblp'):# dblp

        gindex=0

    elif (DATASET == 'fb'): # facebook
        if ego_user !='combined':
            # featurename
            featname_dir = './' + str(ego_user) + '.featnames'
            # facebook feature map
            f = open(featname_dir)
            featnames = []
            for line in f:
                line = line.strip().split(' ')
                feats = line[1]
                feats = feats.split(';')
                feat = feats[0]
                featnames.append(feat)
            # print(featnames)
            # exit()
            f.close()

            # gender 77, gender 78
            gindex = featnames.index('gender')
            print(gindex)
            # rm = []
            #exit()
        else:
            gindex=77



        for i, n in enumerate(g.nodes()):
            if (ft[n][gindex]==1 and ft[n][gindex+1]!=1):
                ginfo = 1 #male
            elif (ft[n][gindex+1]==1and ft[n][gindex]!=1):
                ginfo = 2 #female

            else:
                print('***')
                ginfo = 0 #unknow gender

            print(ginfo)

            g.nodes[n]['gender'] = ginfo
        #print(g.nodes[1])





