python -c "import random,string;print(''.join([random.SystemRandom().choice(\"{}-{}!!\".format(string.ascii_letters, string.digits)) for i in range(63)]).replace('\\'','\\'\"\\'\"\\''))";

