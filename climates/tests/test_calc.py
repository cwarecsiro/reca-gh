#!/usr/bin/env python3
import subprocess

def test_calc():
    log = '/OSM/CBR/LW_BACKCAST/work/code/reca/climate_indicies/tests/log.txt'
    dst = '/OSM/CBR/LW_BACKCAST/work/code/reca/climate_indicies/tests'
    logger = []
    
    for I in ['TXx', 'TNx', 'TXn', "TNn", "FD", "R1", "Rx1day"]:
        print(I)
        call = ' '.join(['/home/war42q/.local/lib/python3.6/site-packages/climate_indicies/calc.py', \
            '-f', '/OSM/CBR/LW_BACKCAST/work/code/reca/climate_indicies/tests/data/filelist.txt', \
            '-i', I, \
            '-d', dst, \
            '-v'])
        make_call = subprocess.run(call, shell = True, stdout=subprocess.PIPE).stdout.decode('utf-8')
        logger.append(make_call)
        
        expected = '{0}/{1}.tif'.format(dst, I)
        assert os.path.exists('{0}/{1}.tif'.format(dst, I))
        
        data = sp.Raster(expected).read().array
        if I == 'FD':
            assert (data == 0).all()
        if I == 'R1':
            assert (data == 1).all()
        if I in ['TNn', 'TXn']:
            assert (data == 1.5).all()
        if I in ['TXx', 'TNx', 'Rx1day']:
            assert (data == 365.5).all()
            
    with open(log, 'w') as f:
        for entry in logger:
            f.write(entry + '\n')
        f.close()
        
        
        
            
        