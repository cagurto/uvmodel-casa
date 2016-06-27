# uvmodel-casa
# procedure to fit a Gaussian/pointsource/disk to Visibility data and plots
# step in miriad
fits in=visdata.uv op=uvout out=visdata_uv.fits

# Example for SMA Per50 data

#steps in CASA

importuvfits(fitsfile='Per50-ext_cont13mm_uv.fits',vis='Per50-13mmextcom.ms')
fixvis(vis="Per50-13mmextcom.ms",outputvis="Per50_extcom13_recenter.ms",field="",refcode="",reuse=True,phasecenter="J2000 3h29m07.76s +31d21m57.2s",datacolumn="all")

# To fit a disk or gaussian 
# IF comptype = ’G’ or ’D’, then
# sourcepar = [flux,xoff,yoff,majax,axrat,pos] where
# majax = FWHM along the major axis (arcsec)
# axrat < 1 is the ratio of minor to major axis
# pos=angle in deg

# to run a GAUSSIAN model
default uvmodelfit
vis='Per50_extcom13_recenter.ms'
field='0'
comptype='G'
# parameters from miriad task "imfit"
sourcepar=[0.131,0.032,0.016,1.929,0.964,0]
varypar=[T,F,F,T,T,T]
outfile='Per50_extcom13gauss.cl'
inp
go

default ft
vis='Per50_extcom13_recenter.ms'
complist='Per50_extcom13gauss.cl'
usescratch=True
inp
go


#to run a DISK model 
# is better

default uvmodelfit
vis='Per50_extcom13_recenter.ms'
field='0'
comptype='D'
# parameters from miriad task "imfit"
sourcepar=[0.131,0.032,0.016,1.929,0.964,0]
varypar=[T,F,F,T,T,T]
outfile='Per50_extcom13.cl'
inp
go

default ft
vis='Per50_extcom13_recenter.ms'
complist='Per50_extcom13.cl'
usescratch=True
inp
go

