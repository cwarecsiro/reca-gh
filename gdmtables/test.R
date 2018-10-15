library(raster)
rasterOptions(tmpdir = 'R:/DEV/war42q/junk')
library(ff)

dst = 'R:/DEV/war42q/junk'

src = list.files('R:/DEV/AWAP_monthly/RECA/monthly/combined',
                 pattern = '.flt$', full.names = T)
# test with FWDis
FWDis = src[grep('FWDis', src)]
FWDis = stack(FWDis[1:10])

mat = ff(vmode = 'double',
         dim = c(ncell(FWDis), nlayers(FWDis)),
         filename = paste0(dst, '/FWDis_test.ffdata'))

for (i in 1:nlayers(FWDis)){
  mat[, i] = FWDis[[i]][]
}


close(mat)
?ff

gg = raster(FWDis[[1]])
gg[] = mat[,1]

print(load(paste0(dst, '/FWDis_test.RData')))
rm(list = ls())

class(mat)
save(mat, file = paste0(dst, '/FWDis_test.RData'))

mat[200000, 2]

f = paste0(dst, '/FWDis_test.ffdata')
fshort = paste0(dst, '/FWDis_test')
file.exists(f)
ffinfo(f)
