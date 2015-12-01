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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwROfYdxA1UJYmFsbFNjYWxlcQRLBEc/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLBIh9h3EHVQlwb2ludFNpemVxCEsERz/wAAAAAAAAfYdxCVUEbmFtZXEKSwRVEEdHX2RpYWdvbl84Ni5wZGJ9cQsoVRBHR19kaWFnb25fMjUucGRicQxdcQ1LAWFVEEdHX2RpYWdvbl8yMi5wZGJxDl1xD0sAYVUQR0dfZGlhZ29uXzg0LnBkYnEQXXERSwJhdYdxElUPYXJvbWF0aWNEaXNwbGF5cRNLBIl9h3EUVQVjb2xvcnEVSwRLAH1xFihLAV1xF0sBYUsCXXEYSwJhSwNdcRlLA2F1h3EaVQhvcHRpb25hbHEbfXEcVQhvcGVuZWRBc3EdiEsEKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0dHL2hfYm9uZGVkL0dHX2RpYWdvbl84Ni5wZGJVA1BEQnEeTol0cR99cSAoKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0dHL2hfYm9uZGVkL0dHX2RpYWdvbl8yMi5wZGJoHk6JdHEhXXEiSwBhKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0dHL2hfYm9uZGVkL0dHX2RpYWdvbl84NC5wZGJoHk6JdHEjXXEkSwJhKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0dHL2hfYm9uZGVkL0dHX2RpYWdvbl8yNS5wZGJoHk6JdHElXXEmSwFhdYeGcSdzVQpwZGJIZWFkZXJzcShdcSkofXEqfXErfXEsfXEtZVUMYXJvbWF0aWNNb2RlcS5LBEsBfYdxL1UDaWRzcTBLBEsDSwCGfXExKEsCSwCGcTJdcTNLAmFLAUsAhnE0XXE1SwFhSwBLAIZxNl1xN0sAYXWHcThVDnN1cmZhY2VPcGFjaXR5cTlLBEe/8AAAAAAAAH2HcTpVCWF1dG9jaGFpbnE7SwSIfYdxPFUKdmR3RGVuc2l0eXE9SwRHQBQAAAAAAAB9h3E+VQ1hcm9tYXRpY0NvbG9ycT9LBE59h3FAVQZoaWRkZW5xQUsEiX2HcUJVCWxpbmVXaWR0aHFDSwRHP/AAAAAAAAB9h3FEVQpzdGlja1NjYWxlcUVLBEc/8AAAAAAAAH2HcUZVB2Rpc3BsYXlxR0sEiH2HcUhVEGFyb21hdGljTGluZVR5cGVxSUsESwJ9h3FKdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksIVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsIiX2HcQVVBG5hbWVxBksIVQFHfYdxB1UFY2hhaW5xCEsIVQFBfXEJVQFCTl1xCihLAUsBhnELSwNLAYZxDEsFSwGGcQ1LB0sBhnEOZYZxD3OHcRBVDnJpYmJvbkRyYXdNb2RlcRFLCEsCfYdxElUCc3NxE0sIiYmJh32HcRRVCG1vbGVjdWxlcRVLCEsAfXEWKEsBTl1xF0sCSwKGcRhhhnEZSwJOXXEaSwRLAoZxG2GGcRxLA05dcR1LBksChnEeYYZxH3WHcSBVC3JpYmJvbkNvbG9ycSFLCE59h3EiVQVsYWJlbHEjSwhVAH2HcSRVCmxhYmVsQ29sb3JxJUsITn2HcSZVCGZpbGxNb2RlcSdLCEsBfYdxKFUFaXNIZXRxKUsIiX2HcSpVC2xhYmVsT2Zmc2V0cStLCE59h3EsVQhwb3NpdGlvbnEtXXEuKEsBSwKGcS9LAUsChnEwSwFLAoZxMUsBSwKGcTJlVQ1yaWJib25EaXNwbGF5cTNLCIl9h3E0VQhvcHRpb25hbHE1fXE2VQRzc0lkcTdLCEr/////fYdxOHUu'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLDUsMZV1xBShLDUsOZV1xBihLD0sOZV1xByhLD0sQZV1xCChLEEsRZV1xCShLEksRZV1xCihLE0sRZV1xCyhLE0sUZV1xDChLFUsUZV1xDShLFUsMZV1xDihLFUsPZV1xDyhLE0sWZV1xEChLF0sWZV1xEShLGEsWZV1xEihLEEsZZV1xEyhLDUsaZV1xFChLG0sMZV1xFShLHUscZV1xFihLHkscZV1xFyhLHksfZV1xGChLIEsfZV1xGShLIEshZV1xGihLIUsiZV1xGyhLIUsjZV1xHChLJEsjZV1xHShLJUsjZV1xHihLJUsmZV1xHyhLJ0smZV1xIChLJ0sgZV1xIShLJ0scZV1xIihLJUsoZV1xIyhLKUsoZV1xJChLKksoZV1xJShLHksrZV1xJihLLUssZV1xJyhLLUsuZV1xKChLLksvZV1xKShLL0swZV1xKihLMUswZV1xKyhLMkswZV1xLChLMkszZV1xLShLNEszZV1xLihLNUszZV1xLyhLMks2ZV1xMChLLUs2ZV1xMShLL0s3ZV1xMihLLks4ZV1xMyhLOUs4ZV1xNChLOUssZV1xNShLOUs6ZV1xNihLO0ssZV1xNyhLPUs8ZV1xOChLPUs+ZV1xOShLP0s+ZV1xOihLP0tAZV1xOyhLQEtBZV1xPChLQEtCZV1xPShLQ0tCZV1xPihLREtCZV1xPyhLREtFZV1xQChLRktFZV1xQShLR0tFZV1xQihLREtIZV1xQyhLSUtIZV1xRChLSUs8ZV1xRShLSUs/ZV1xRihLPUtKZV1xRyhLS0s8ZV1xSChLTUtMZV1xSShLTUtOZV1xSihLT0tOZV1xSyhLUEtPZV1xTChLUEtRZV1xTShLUktRZV1xTihLUktTZV1xTyhLVEtTZV1xUChLVUtTZV1xUShLUktWZV1xUihLV0tWZV1xUyhLWEtWZV1xVChLT0tYZV1xVShLWEtZZV1xVihLUEtMZV1xVyhLTUtaZV1xWChLW0tMZV1xWShLXUtcZV1xWihLXUteZV1xWyhLXktfZV1xXChLYEtfZV1xXShLYEtcZV1xXihLYEthZV1xXyhLXktiZV1xYChLYktjZV1xYShLZEtjZV1xYihLZEtlZV1xYyhLZktlZV1xZChLZ0tlZV1xZShLZEtoZV1xZihLXUtoZV1xZyhLaUtjZV1xaChLYktqZV1xaShLa0tcZV1xaihLbUtsZV1xayhLbUtuZV1xbChLb0tuZV1xbShLb0twZV1xbihLcUtwZV1xbyhLcktwZV1xcChLc0tyZV1xcShLc0t0ZV1xcihLdUt0ZV1xcyhLdUt2ZV1xdChLdUtsZV1xdShLbUtzZV1xdihLckt3ZV1xdyhLb0t4ZV1xeChLeUt4ZV1xeShLekt4ZV1xeihLe0tsZV1xeyhLfUt8ZV1xfChLfkt8ZV1xfShLfkt/ZV1xfihLfkuAZV1xfyhLgUuAZV1xgChLgkuBZV1xgShLgkt8ZV1xgihLgkuDZV1xgyhLhEuDZV1xhChLhEuFZV1xhShLhkuFZV1xhihLh0uFZV1xhyhLh0uIZV1xiChLgUuHZV1xiShLhEuJZV1xiihLikuJZV1xiyhLi0uJZWVVBWxhYmVscYxLiFUAfYdxjVUGcmFkaXVzcY5LiEc/yZmZoAAAAH2HcY9VC2xhYmVsT2Zmc2V0cZBLiE59h3GRVQhkcmF3TW9kZXGSS4hLAX2HcZNVCG9wdGlvbmFscZR9cZVVB2Rpc3BsYXlxlkuISwJ9h3GXdS4='))
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
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 7, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('_openColor03', (1, 1, 0, 1)), 4: ('N', (0.188235, 0.313725, 0.972549, 1)), 5: ('H', (1, 1, 1, 1)), 6: ('O', (1, 0.0509804, 0.0509804, 1)), 7: ('yellow', (1, 1, 0, 1)), 8: ('white', (1, 1, 1, 1)), 9: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (24.727, -3.756, 9.83202), 'fieldOfView': 26.2751, 'nearFar': (20.7041, -1.41861), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 12.855}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 11.9675, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.552622}, 'viewerHL': 9, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 8}

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
	residueData = [(4, 'Chimera default', 'rounded', 'unknown'), (5, 'Chimera default', 'rounded', 'unknown'), (6, 'Chimera default', 'rounded', 'unknown'), (7, 'Chimera default', 'rounded', 'unknown'), (8, 'Chimera default', 'rounded', 'unknown'), (9, 'Chimera default', 'rounded', 'unknown'), (10, 'Chimera default', 'rounded', 'unknown'), (11, 'Chimera default', 'rounded', 'unknown')]
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
	xformMap = {0: (((-0.0546528, 0.86494, -0.49889), 61.9062), (5.47514, 12.464, 20.127), True), 1: (((0.496178, -0.122838, -0.859487), 87.4937), (23.9241, 24.8881, 9.18068), True), 2: (((0.92719, -0.256877, -0.272642), 146.463), (14.1536, 27.6156, -11.1767), True), 3: (((-0.562007, -0.653896, -0.506525), 78.5735), (-10.7921, -12.0512, 7.65303), True)}
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

