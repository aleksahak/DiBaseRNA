import cPickle, base64
try:
	from SimpleSession.versions.v45 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 4, 29530])
import chimera
from chimera import replyobj
replyobj.status('Beginning session restore...', \
    blankAfter=0)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v45 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwVOfYdxA1UJYmFsbFNjYWxlcQRLBUc/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLBYh9h3EHVQlwb2ludFNpemVxCEsFRz/wAAAAAAAAfYdxCVUEbmFtZXEKSwVVEUNDX2RpYWdvbl8xMTEucGRifXELKFUQQ0NfZGlhZ29uXzcwLnBkYnEMXXENSwRhVRBDQ19kaWFnb25fNjkucGRicQ5dcQ9LA2FVEUNDX2RpYWdvbl8xMTAucGRicRBdcRFLAGFVEUNDX2RpYWdvbl8xMjEucGRicRJdcRNLAmF1h3EUVQ9hcm9tYXRpY0Rpc3BsYXlxFUsFiX2HcRZVBWNvbG9ycRdLBUsAfXEYKEsBXXEZSwFhSwJdcRpLAmFLA11xG0sDYUsEXXEcSwRhdYdxHVUIb3B0aW9uYWxxHn1xH1UIb3BlbmVkQXNxIIhLBShVOy9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9oX2JvbmRlZC9DQ19kaWFnb25fNjkucGRiVQNQREJxIU6JdHEifXEjKChVOy9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9oX2JvbmRlZC9DQ19kaWFnb25fNzAucGRiaCFOiXRxJF1xJUsEYShVPC9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9DQy9oX2JvbmRlZC9DQ19kaWFnb25fMTEwLnBkYmghTol0cSZdcSdLAGEoVTwvaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQ0MvaF9ib25kZWQvQ0NfZGlhZ29uXzExMS5wZGJoIU6JdHEoXXEpSwFhKFU8L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0NDL2hfYm9uZGVkL0NDX2RpYWdvbl8xMjEucGRiaCFOiXRxKl1xK0sCYXWHhnEsc1UKcGRiSGVhZGVyc3EtXXEuKH1xL31xMH1xMX1xMn1xM2VVDGFyb21hdGljTW9kZXE0SwVLAX2HcTVVA2lkc3E2SwVLA0sAhn1xNyhLAksAhnE4XXE5SwJhSwFLAIZxOl1xO0sBYUsASwCGcTxdcT1LAGFLBEsAhnE+XXE/SwRhdYdxQFUOc3VyZmFjZU9wYWNpdHlxQUsFR7/wAAAAAAAAfYdxQlUJYXV0b2NoYWlucUNLBYh9h3FEVQp2ZHdEZW5zaXR5cUVLBUdAFAAAAAAAAH2HcUZVDWFyb21hdGljQ29sb3JxR0sFTn2HcUhVBmhpZGRlbnFJSwWJfYdxSlUJbGluZVdpZHRocUtLBUc/8AAAAAAAAH2HcUxVCnN0aWNrU2NhbGVxTUsFRz/wAAAAAAAAfYdxTlUHZGlzcGxheXFPSwWIfYdxUFUQYXJvbWF0aWNMaW5lVHlwZXFRSwVLAn2HcVJ1Lg=='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksKVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsKiX2HcQVVBG5hbWVxBksKVQFDfYdxB1UFY2hhaW5xCEsKVQFBfXEJVQFCTl1xCihLAUsBhnELSwNLAYZxDEsFSwGGcQ1LB0sBhnEOSwlLAYZxD2WGcRBzh3ERVQ5yaWJib25EcmF3TW9kZXESSwpLAn2HcRNVAnNzcRRLComJiYd9h3EVVQhtb2xlY3VsZXEWSwpLAH1xFyhLAU5dcRhLAksChnEZYYZxGksCTl1xG0sESwKGcRxhhnEdSwNOXXEeSwZLAoZxH2GGcSBLBE5dcSFLCEsChnEiYYZxI3WHcSRVC3JpYmJvbkNvbG9ycSVLCk59h3EmVQVsYWJlbHEnSwpVAH2HcShVCmxhYmVsQ29sb3JxKUsKTn2HcSpVCGZpbGxNb2RlcStLCksBfYdxLFUFaXNIZXRxLUsKiX2HcS5VC2xhYmVsT2Zmc2V0cS9LCk59h3EwVQhwb3NpdGlvbnExXXEyKEsBSwKGcTNLAUsChnE0SwFLAoZxNUsBSwKGcTZLAUsChnE3ZVUNcmliYm9uRGlzcGxheXE4SwqJfYdxOVUIb3B0aW9uYWxxOn1xO1UEc3NJZHE8SwpK/////32HcT11Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLEEsPZV1xBShLEEsRZV1xBihLEksRZV1xByhLEksTZV1xCChLE0sUZV1xCShLE0sVZV1xCihLFUsPZV1xCyhLFUsWZV1xDChLEksXZV1xDShLGEsXZV1xDihLGUsXZV1xDyhLEEsaZV1xEChLG0sPZV1xEShLHUscZV1xEihLHUseZV1xEyhLH0sdZV1xFChLH0sgZV1xFShLIUsfZV1xFihLIUsiZV1xFyhLI0siZV1xGChLI0scZV1xGShLI0skZV1xGihLIUslZV1xGyhLJkslZV1xHChLJ0slZV1xHShLKEscZV1xHihLKkspZV1xHyhLK0spZV1xIChLK0ssZV1xIShLLUsrZV1xIihLLUsuZV1xIyhLL0stZV1xJChLL0swZV1xJShLMUswZV1xJihLMkswZV1xJyhLL0szZV1xKChLNEszZV1xKShLNEs1ZV1xKihLNEspZV1xKyhLN0s2ZV1xLChLOEs2ZV1xLShLOEs5ZV1xLihLOEs6ZV1xLyhLO0s6ZV1xMChLO0s8ZV1xMShLPEs9ZV1xMihLPEs+ZV1xMyhLPks2ZV1xNChLPks/ZV1xNShLO0tAZV1xNihLQUtAZV1xNyhLQktAZV1xOChLREtDZV1xOShLREtFZV1xOihLREtGZV1xOyhLR0tGZV1xPChLR0tIZV1xPShLSUtIZV1xPihLSktIZV1xPyhLR0tLZV1xQChLS0tMZV1xQShLS0tNZV1xQihLTUtDZV1xQyhLTUtOZV1xRChLT0tDZV1xRShLUUtQZV1xRihLUUtSZV1xRyhLU0tSZV1xSChLU0tUZV1xSShLVUtUZV1xSihLVktUZV1xSyhLU0tXZV1xTChLV0tYZV1xTShLV0tZZV1xTihLWUtaZV1xTyhLWUtQZV1xUChLUUtbZV1xUShLXEtQZV1xUihLXktdZV1xUyhLX0tdZV1xVChLX0tgZV1xVShLX0thZV1xVihLYkthZV1xVyhLYktjZV1xWChLY0tkZV1xWShLY0tlZV1xWihLZUtmZV1xWyhLZUtdZV1xXChLYktnZV1xXShLaEtnZV1xXihLaUtnZV1xXyhLa0tqZV1xYChLbEtrZV1xYShLbUtsZV1xYihLbUtuZV1xYyhLb0tuZV1xZChLb0twZV1xZShLb0tqZV1xZihLbUtxZV1xZyhLcktxZV1xaChLc0txZV1xaShLbEt0ZV1xaihLa0t1ZV1xayhLdktqZV1xbChLeEt3ZV1xbShLeEt5ZV1xbihLeEt6ZV1xbyhLe0t6ZV1xcChLe0t8ZV1xcShLfUt8ZV1xcihLfkt8ZV1xcyhLe0t/ZV1xdChLf0uAZV1xdShLf0uBZV1xdihLgUt3ZV1xdyhLgUuCZV1xeChLg0t3ZV1xeShLhUuEZV1xeihLhUuGZV1xeyhLh0uGZV1xfChLh0uIZV1xfShLiEuJZV1xfihLiEuKZV1xfyhLikuLZV1xgChLikuEZV1xgShLh0uMZV1xgihLjUuMZV1xgyhLjkuMZV1xhChLhUuPZV1xhShLkEuEZWVVBWxhYmVscYZLglUAfYdxh1UGcmFkaXVzcYhLgkc/yZmZoAAAAH2HcYlVC2xhYmVsT2Zmc2V0cYpLgk59h3GLVQhkcmF3TW9kZXGMS4JLAX2HcY1VCG9wdGlvbmFscY59cY9VB2Rpc3BsYXlxkEuCSwJ9h3GRdS4='))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'oneTransparentLayer': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, 'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, 'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, 'default'), 'Rf': ((0.8, 0, 0.34902), 1, 'default'), 'Ra': ((0, 0.490196, 0), 1, 'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, 'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, 'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, 'default'), 'Be': ((0.760784, 1, 0), 1, 'default'), 'Ba': ((0, 0.788235, 0), 1, 'default'), 'Bh': ((0.878431, 0, 0.219608), 1, 'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, 'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, 'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, 'default'), '_openColor00': ((1, 1, 1), 1, 'default'), '_openColor01': ((1, 0, 1), 1, 'default'), '_openColor02': ((0, 1, 1), 1, 'default'), '_openColor03': ((1, 1, 0), 1, 'default'), '_openColor04': ((1, 0, 0), 1, 'default'), '_openColor05': ((0, 0, 1), 1, 'default'), '_openColor06': ((0.67, 1, 0), 1, 'default'), '_openColor07': ((0.67, 0, 1), 1, 'default'), '_openColor08': ((0.67, 1, 1), 1, 'default'),
'H': ((1, 1, 1), 1, 'default'), 'P': ((1, 0.501961, 0), 1, 'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, 'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, 'default'), 'Gd': ((0.270588, 1, 0.780392), 1, 'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, 'default'), 'Pr': ((0.85098, 1, 0.780392), 1, 'default'), '_openColor12': ((1, 1, 0.5), 1, 'default'), '_openColor11': ((1, 0.67, 1), 1, 'default'), '_openColor10': ((0, 0.67, 1), 1, 'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, 'default'), 'Pu': ((0, 0.419608, 1), 1, 'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, 'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, 'default'), 'Pa': ((0, 0.631373, 1), 1, 'default'), 'Pd': ((0, 0.411765, 0.521569), 1, 'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, 'default'), 'Po': ((0.670588, 0.360784, 0), 1, 'default'), 'Pm': ((0.639216, 1, 0.780392), 1, 'default'), 'Hs': ((0.901961, 0, 0.180392), 1, 'default'), 'Ho': ((0, 1, 0.611765), 1, 'default'), 'Hf': ((0.301961, 0.760784, 1), 1, 'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, 'default'),
'He': ((0.85098, 1, 1), 1, 'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, 'default'), 'Mg': ((0.541176, 1, 0), 1, 'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, 'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, 'default'), 'O': ((1, 0.0509804, 0.0509804), 1, 'default'), 'Mt': ((0.921569, 0, 0.14902), 1, 'default'), 'S': ((1, 1, 0.188235), 1, 'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, 'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, 'default'), 'Eu': ((0.380392, 1, 0.780392), 1, 'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, 'default'), 'Er': ((0, 0.901961, 0.458824), 1, 'default'), '_openColor13': ((1, 0, 0.5), 1, 'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, 'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, 'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, 'default'), 'Nd': ((0.780392, 1, 0.780392), 1, 'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, 'default'), 'Np': ((0, 0.501961, 1), 1, 'default'), 'Fr': ((0.258824, 0, 0.4), 1, 'default'), '_openColor15': ((0.67, 0.67, 1), 1, 'default'), '_openColor14': ((0, 1, 0.5), 1, 'default'),
'Fe': ((0.878431, 0.4, 0.2), 1, 'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, 'default'), 'B': ((1, 0.709804, 0.709804), 1, 'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, 'default'), 'Sr': ((0, 1, 0), 1, 'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, 'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, 'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, 'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, 'default'), 'Sm': ((0.560784, 1, 0.780392), 1, 'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, 'default'), 'Sc': ((0.901961, 0.901961, 0.901961), 1, 'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, 'default'), 'Sg': ((0.85098, 0, 0.270588), 1, 'default'), 'Se': ((1, 0.631373, 0), 1, 'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, 'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, 'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, 'default'), 'Ca': ((0.239216, 1, 0), 1, 'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, 'default'), 'Ce': ((1, 1, 0.780392), 1, 'default'), 'Cd': ((1, 0.85098, 0.560784), 1, 'default'),
'Tm': ((0, 0.831373, 0.321569), 1, 'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, 'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, 'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, 'default'), 'La': ((0.439216, 0.831373, 1), 1, 'default'), 'Li': ((0.8, 0.501961, 1), 1, 'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, 'default'), 'Lu': ((0, 0.670588, 0.141176), 1, 'default'), 'Lr': ((0.780392, 0, 0.4), 1, 'default'), 'Th': ((0, 0.729412, 1), 1, 'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, 'default'), 'Te': ((0.831373, 0.478431, 0), 1, 'default'), 'Tb': ((0.188235, 1, 0.780392), 1, 'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, 'default'), 'Ta': ((0.301961, 0.65098, 1), 1, 'default'), 'Yb': ((0, 0.74902, 0.219608), 1, 'default'), 'Db': ((0.819608, 0, 0.309804), 1, 'default'), 'Dy': ((0.121569, 1, 0.780392), 1, 'default'), '_openColor09': ((1, 0.67, 0), 1, 'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, 'default'), 'I': ((0.580392, 0, 0.580392), 1, 'default'), 'U': ((0, 0.560784, 1), 1, 'default'), 'Y': ((0.580392, 1, 1), 1, 'default'),
'Ac': ((0.439216, 0.670588, 0.980392), 1, 'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, 'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, 'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, 'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, 'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, 'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, 'default'), 'Au': ((1, 0.819608, 0.137255), 1, 'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, 'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, 'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, 'default')}
	materials = {'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 8, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('_openColor03', (1, 1, 0, 1)), 4: ('_openColor04', (1, 0, 0, 1)), 5: ('N', (0.188235, 0.313725, 0.972549, 1)), 6: ('H', (1, 1, 1, 1)), 7: ('O', (1, 0.0509804, 0.0509804, 1)), 8: ('yellow', (1, 1, 0, 1)), 9: ('white', (1, 1, 1, 1)), 10: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (31.603, -5.656, 14.2444), 'fieldOfView': 26.2751, 'nearFar': (24.6232, 3.46195), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 11.166}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 7.35413, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.453494}, 'viewerHL': 10, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 9}

	replyobj.status("Initializing session restore...", blankAfter=0)
	init(colorInfo)
	replyobj.status("Restoring colors...", blankAfter=0)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0)


def restoreLightController():
	import Lighting
	c = Lighting.get().setFromParams({'quality': 'normal', 'shininess': (30.0, (0.84999999999999998, 0.84999999999999998, 0.84999999999999998), 1.0), 'key': (True, (1.0, 1.0, 1.0), 0.65327227115631104, (1.0, 1.0, 1.0), 1.0, (-0.35740674433659325, 0.66040155174814552, 0.66040155174814552)), 'fill': (True, (1.0, 1.0, 1.0), 0.49998998641967773, (1.0, 1.0, 1.0), 0.0, (0.25056280708573153, 0.25056280708573153, 0.9351131265310294))})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(5, 'Chimera default', 'rounded', 'unknown'), (6, 'Chimera default', 'rounded', 'unknown'), (7, 'Chimera default', 'rounded', 'unknown'), (8, 'Chimera default', 'rounded', 'unknown'), (9, 'Chimera default', 'rounded', 'unknown'), (10, 'Chimera default', 'rounded', 'unknown'), (11, 'Chimera default', 'rounded', 'unknown'), (12, 'Chimera default', 'rounded', 'unknown'), (13, 'Chimera default', 'rounded', 'unknown'), (14, 'Chimera default', 'rounded', 'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")
geomData = {'AxisManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restoreMidasBase():
	import chimera
	from SimpleSession import modelMap, modelOffset
	def deformatPosition(pos):
		xfDict = {}
		for molId, xfData in pos[5].items():
			mid, subid = molId
			trData, rotData = xfData
			xf = chimera.Xform.translation(*trData)
			xf.rotate(*rotData)
			xfDict[(mid+modelOffset, subid)] = xf
		try:
			from chimera.misc import KludgeWeakWrappyDict
			clipDict = KludgeWeakWrappyDict("Model")
		except ImportError:
			from weakref import WeakKeyDictionary
			clipDict = WeakKeyDictionary()
		for clipID, clipInfo in pos[6].items():
			mid, subid, className = clipID
			models = [m for m in modelMap.get((mid, subid), [])
					if m.__class__.__name__ == className]
			if not models:
				continue
			useClip, ox, oy, oz, nx, ny, nz, useThick, thickness = clipInfo
			if useClip:
				origin = chimera.Point(ox, oy, oz)
				normal = chimera.Vector(nx, ny, nz)
				plane = chimera.Plane(origin, normal)
			else:
				plane = chimera.Plane()
			for m in models:
				clipDict[m] = (useClip, plane,
							useThick, thickness)
		return pos[:5] + (xfDict, clipDict) + pos[7:]
	formattedPositions = {}
	positions = {}
	for name, fpos in formattedPositions.items():
		positions[name] = deformatPosition(fpos)
	import Midas
	if modelOffset == 0:
		Midas.positions.clear()
	Midas.positions.update(positions)
	positionStack = []
	Midas._positionStack = map(deformatPosition, positionStack)

def delayedMidasBase():
	try:
		restoreMidasBase()
	except:
		reportRestoreError('Error restoring Midas base state')
import SimpleSession
SimpleSession.registerAfterModelsCB(delayedMidasBase)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreRemainder():
	from SimpleSession.versions.v45 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1270, 607)
	xformMap = {0: (((0.739319, 0.345982, -0.577671), 131.663), (34.8007, 1.20655, 48.6882), True), 1: (((-0.272569, -0.724584, -0.632996), 143.982), (54.5727, -15.4013, -5.35467), True), 2: (((-0.467792, -0.72983, -0.498516), 94.6472), (33.8735, -45.8686, -8.66991), True), 3: (((0.891723, 0.301947, 0.337132), 159.36), (3.01243, -10.7975, 21.4627), True), 4: (((-0.175823, -0.512674, -0.840388), 61.5369), (23.2741, -5.79277, -16.5227), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}

	replyobj.status("Restoring window...", blankAfter=0)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0)
	restoreModelClip(clipPlaneInfo)

	replyobj.status("Restoring remaining extension info...", blankAfter=0)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v45 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v45 import endRestore
replyobj.status('Finishing restore...', blankAfter=0)
endRestore()
replyobj.status('Restore finished.')

