#in casapy
import numpy as np
import matplotlib.pyplot as plt
import glob

testms='Per50_extcom13_recenter.ms'
# set the uvrange in kilo lambda
# range for ext+com configuration at 1.3mm
uvmin = 20
uvmax = 120
# define steps in klambda
duv=5

uvsteps = np.arange(uvmin, uvmax, duv)

avg_amps = [] 
stddev_amps = [] 
numpoints = []
uvpoints = uvsteps[:-1] + np.diff(uvsteps)/2
# get array of uvmidpoints over which avg taken
model_amps = [] 
# define list to get model amplitudes after fourier transforming into the model data column

for ii in range(len(uvsteps[:-1])):
        tmp = visstat(vis = testms,axis = 'real',
                      uvrange = str(uvsteps[ii]) + '~' + str(uvsteps[ii+1]) + 'klambda',
                      datacolumn = 'data')
        print str(uvsteps[ii]) + '~' + str(uvsteps[ii+1]) + 'klambda'
        avg_amps.append(tmp['DATA']['mean'])
        stddev_amps.append(tmp['DATA']['stddev'])
        numpoints.append(tmp['DATA']['npts'])

# now build up the model values
for ii in range(len(uvsteps[:-1])):
        tmp = visstat(vis = testms,
                        axis = 'real', # you may want to change this to real...?
                        uvrange = str(uvsteps[ii]) + '~' + str(uvsteps[ii+1]) + 'klambda',
                        datacolumn = 'model')
        print str(uvsteps[ii]) + '~' + str(uvsteps[ii+1]) + 'klambda, from the model column'
        model_amps.append(tmp['MODEL']['mean'])

error_amps = stddev_amps/(np.sqrt(numpoints) - 1)

plt.clf()
plt.cla()

avg_amps_mjy = [x * 1000 for x in avg_amps]
model_amps_mjy = [x * 1000 for x in model_amps]
error_amps_mjy = [x * 1000 for x in error_amps]

plt.errorbar(uvpoints, avg_amps_mjy, yerr = error_amps_mjy, mfc='k', fmt='o', label='data')
plt.plot(uvpoints, model_amps_mjy, 'r-', label=r'model from $uvmodelfit$')

plt.legend(loc = 3, numpoints = 1)

plt.xlabel(r'UV Distance (k$\lambda$)')
plt.ylabel('Real Visibility (mJy)')

plt.show()
