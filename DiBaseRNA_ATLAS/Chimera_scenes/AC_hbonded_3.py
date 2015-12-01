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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwNOfYdxA1UJYmFsbFNjYWxlcQRLA0c/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLA4h9h3EHVQlwb2ludFNpemVxCEsDRz/wAAAAAAAAfYdxCVUEbmFtZXEKSwNVEEFDX2RpYWdvbl85Ny5wZGJ9cQsoVRFBQ19kaWFnb25fMTM3LnBkYnEMXXENSwBhVRBBQ19kaWFnb25fNTAucGRicQ5dcQ9LAWF1h3EQVQ9hcm9tYXRpY0Rpc3BsYXlxEUsDiX2HcRJVBWNvbG9ycRNLA0sAfXEUKEsBXXEVSwFhSwJdcRZLAmF1h3EXVQhvcHRpb25hbHEYfXEZVQhvcGVuZWRBc3EaiEsDKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FDL2hfYm9uZGVkL0FDX2RpYWdvbl85Ny5wZGJVA1BEQnEbTol0cRx9cR0oKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FDL2hfYm9uZGVkL0FDX2RpYWdvbl81MC5wZGJoG06JdHEeXXEfSwFhKFU8L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FDL2hfYm9uZGVkL0FDX2RpYWdvbl8xMzcucGRiaBtOiXRxIF1xIUsAYXWHhnEic1UKcGRiSGVhZGVyc3EjXXEkKH1xJX1xJn1xJ2VVDGFyb21hdGljTW9kZXEoSwNLAX2HcSlVA2lkc3EqSwNLAksAhn1xKyhLAUsAhnEsXXEtSwFhSwBLAIZxLl1xL0sAYXWHcTBVDnN1cmZhY2VPcGFjaXR5cTFLA0e/8AAAAAAAAH2HcTJVCWF1dG9jaGFpbnEzSwOIfYdxNFUKdmR3RGVuc2l0eXE1SwNHQBQAAAAAAAB9h3E2VQ1hcm9tYXRpY0NvbG9ycTdLA059h3E4VQZoaWRkZW5xOUsDiX2HcTpVCWxpbmVXaWR0aHE7SwNHP/AAAAAAAAB9h3E8VQpzdGlja1NjYWxlcT1LA0c/8AAAAAAAAH2HcT5VB2Rpc3BsYXlxP0sDiH2HcUBVEGFyb21hdGljTGluZVR5cGVxQUsDSwJ9h3FCdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksGVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsGiX2HcQVVBG5hbWVxBksGVQFBfXEHVQFDXXEIKEsBSwNLBWVzh3EJVQVjaGFpbnEKSwZVAUF9cQtVAUJOXXEMKEsBSwGGcQ1LA0sBhnEOSwVLAYZxD2WGcRBzh3ERVQ5yaWJib25EcmF3TW9kZXESSwZLAn2HcRNVAnNzcRRLBomJiYd9h3EVVQhtb2xlY3VsZXEWSwZLAH1xFyhLAU5dcRhLAksChnEZYYZxGksCTl1xG0sESwKGcRxhhnEddYdxHlULcmliYm9uQ29sb3JxH0sGTn2HcSBVBWxhYmVscSFLBlUAfYdxIlUKbGFiZWxDb2xvcnEjSwZOfYdxJFUIZmlsbE1vZGVxJUsGSwF9h3EmVQVpc0hldHEnSwaJfYdxKFULbGFiZWxPZmZzZXRxKUsGTn2HcSpVCHBvc2l0aW9ucStdcSwoSwFLAoZxLUsBSwKGcS5LAUsChnEvZVUNcmliYm9uRGlzcGxheXEwSwaJfYdxMVUIb3B0aW9uYWxxMn1xM1UEc3NJZHE0SwZK/////32HcTV1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLVEsDfXEDKEsETl1xBEsPSw2GcQVhhnEGSwVOXXEHSxxLD4ZxCGGGcQlLBk5dcQpLK0sNhnELYYZxDEsHTl1xDUs4Sw+GcQ5hhnEPSwhOXXEQS0dLDYZxEWGGcRJ1h3ETVQh2ZHdDb2xvcnEUS1ROfYdxFVUEbmFtZXEWS1RVAkMyfXEXKFUCTzJxGF1xGShLGks1S1NlVQMxSDZxGl1xGyhLDUsoSz9lVQMxSDRxHF1xHShLGUsxS1FlVQMySDRxHl1xHyhLGEsyS1JlVQMySDZxIF1xIShLDEspS0BlVQJDOHEiXXEjKEsCSx5LOmVVAkM2cSRdcSUoSwVLFUshSyxLPUtOZVUCQzVxJl1xJyhLBEsTSyBLLks8S0xlVQJDNHEoXXEpKEsKSxJLJUsvS0RLS2VVAk45cSpdcSsoSwBLHEs4ZVUCTjFxLF1xLShLBksPSyJLK0tBS0dlVQJOM3EuXXEvKEsJSxFLJEszS0NLSmVVAk40cTBdcTEoSxdLMEtQZVUCTjZxMl1xMyhLC0snSz5lVQJON3E0XXE1KEsDSx9LO2VVAkg4cTZdcTcoSw5LKktGZVUCSDlxOF1xOShLAUsdSzllVQJIMnE6XXE7KEsISyZLRWVVAkgxcTxdcT0oSxtLN0tIZVUCSDZxPl1xPyhLFkstS09lVQJINXFAXXFBKEsUSzZLTWV1h3FCVQN2ZHdxQ0tUiX2HcURVDnN1cmZhY2VEaXNwbGF5cUVLVIl9h3FGVQVjb2xvcnFHS1RLBH1xSChOXXFJKEsCSwRLBUsHSwpLEEsSSxNLFUseSyBLIUsjSyVLLEsuSy9LNEs6SzxLPUtCS0RLSUtLS0xLTmVLA11xSihLAEsDSwZLCUsLSw9LEUsXSxxLH0siSyRLJ0srSzBLM0s4SztLPktBS0NLR0tKS1BlSwVdcUsoSxpLNUtTZXWHcUxVCWlkYXRtVHlwZXFNS1SJfYdxTlUGYWx0TG9jcU9LVFUAfYdxUFUFbGFiZWxxUUtUVQB9h3FSVQ5zdXJmYWNlT3BhY2l0eXFTS1RHv/AAAAAAAAB9h3FUVQdlbGVtZW50cVVLVEsBfXFWKEsIXXFXKEsaSzVLU2VLBl1xWChLAksESwVLB0sKSxBLEksTSxVLHksgSyFLI0slSyxLLksvSzRLOks8Sz1LQktES0lLS0tMS05lSwddcVkoSwBLA0sGSwlLC0sPSxFLF0scSx9LIkskSydLK0swSzNLOEs7Sz5LQUtDS0dLSktQZXWHcVpVCmxhYmVsQ29sb3JxW0tUTn2HcVxVDHN1cmZhY2VDb2xvcnFdS1ROfYdxXlUGcmFkaXVzcV9LVEc/8AAAAAAAAH1xYChHP/oAAAAAAABdcWEoSwBLA0sGSwlLC0sPSxFLF0scSx9LIkskSydLK0swSzNLOEs7Sz5LQUtDS0dLSktQZUc/964UgAAAAF1xYihLGks1S1NlRz/7MzNAAAAAXXFjKEsCSwRLBUsHSwpLEEsSSxNLFUseSyBLIUsjSyVLLEsuSy9LNEs6SzxLPUtCS0RLSUtLS0xLTmV1h3FkVQtsYWJlbE9mZnNldHFlS1ROfYdxZlUPc3VyZmFjZUNhdGVnb3J5cWdLVFUEbWFpbn2HcWhVCGRyYXdNb2RlcWlLVEsCfYdxalUIb3B0aW9uYWxxa31xbChVB2JmYWN0b3JxbYhLVEcAAAAAAAAAAH2HhnFuVQlvY2N1cGFuY3lxb4hLVEcAAAAAAAAAAH2HhnFwdVUHZGlzcGxheXFxS1SIfXFyiU5dcXMoSwhLAYZxdEsOSwGGcXVLFEsBhnF2SxZLAYZxd0smSwGGcXhLKksBhnF5Sy1LAYZxeks2SwGGcXtLRUsChnF8S01LAYZxfUtPSwGGcX5lhnF/c4dxgHUu'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLCksJZV1xBShLC0sJZV1xBihLC0sMZV1xByhLDUsMZV1xCChLDUsOZV1xCShLDksPZV1xCihLEEsPZV1xCyhLEEsRZV1xDChLEEsSZV1xDShLE0sSZV1xDihLE0sNZV1xDyhLE0sJZV1xEChLDksUZV1xEShLFUsUZV1xEihLFksUZV1xEyhLC0sXZV1xFChLGUsYZV1xFShLGUsaZV1xFihLG0saZV1xFyhLG0scZV1xGChLHEsdZV1xGShLHEseZV1xGihLHksYZV1xGyhLHksfZV1xHChLG0sgZV1xHShLIUsgZV1xHihLIksgZV1xHyhLGUsjZV1xIChLJEsYZV1xIShLJkslZV1xIihLJ0slZV1xIyhLJ0soZV1xJChLKUsoZV1xJShLKUsqZV1xJihLKksrZV1xJyhLLEsrZV1xKChLLEstZV1xKShLLkstZV1xKihLLkslZV1xKyhLLkspZV1xLChLLEsvZV1xLShLKkswZV1xLihLMUswZV1xLyhLMkswZV1xMChLJ0szZV1xMShLNUs0ZV1xMihLNUs2ZV1xMyhLN0s1ZV1xNChLOEs3ZV1xNShLOEs5ZV1xNihLOks5ZV1xNyhLO0s5ZV1xOChLOEs8ZV1xOShLPUs8ZV1xOihLPUs0ZV1xOyhLPUs+ZV1xPChLN0s/ZV1xPShLQEs0ZV1xPihLQktBZV1xPyhLQ0tBZV1xQChLQ0tEZV1xQShLRUtEZV1xQihLRUtGZV1xQyhLRktHZV1xRChLSEtHZV1xRShLSUtHZV1xRihLRktKZV1xRyhLS0tKZV1xSChLS0tMZV1xSShLTUtMZV1xSihLTUtBZV1xSyhLTUtFZV1xTChLS0tOZV1xTShLQ0tPZV1xTihLUUtQZV1xTyhLUktQZV1xUChLUktTZV1xUShLVEtTZV1xUihLVEtVZV1xUyhLVUtWZV1xVChLVUtXZV1xVShLV0tYZV1xVihLV0tQZV1xVyhLVEtZZV1xWChLWktZZV1xWShLW0tZZV1xWihLUktcZWVVBWxhYmVscVtLV1UAfYdxXFUGcmFkaXVzcV1LV0c/yZmZoAAAAH2HcV5VC2xhYmVsT2Zmc2V0cV9LV059h3FgVQhkcmF3TW9kZXFhS1dLAX2HcWJVCG9wdGlvbmFscWN9cWRVB2Rpc3BsYXlxZUtXSwJ9h3FmdS4='))
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
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 6, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('N', (0.188235, 0.313725, 0.972549, 1)), 4: ('H', (1, 1, 1, 1)), 5: ('O', (1, 0.0509804, 0.0509804, 1)), 6: ('yellow', (1, 1, 0, 1)), 7: ('white', (1, 1, 1, 1)), 8: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (10.6715, 42.045, 26.4516), 'fieldOfView': 26.2751, 'nearFar': (34.7633, 18.14), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 27.3285}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 9.84382, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.673419}, 'viewerHL': 8, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 7}

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
	residueData = [(3, 'Chimera default', 'rounded', 'unknown'), (4, 'Chimera default', 'rounded', 'unknown'), (5, 'Chimera default', 'rounded', 'unknown'), (6, 'Chimera default', 'rounded', 'unknown'), (7, 'Chimera default', 'rounded', 'unknown'), (8, 'Chimera default', 'rounded', 'unknown')]
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
	xformMap = {0: (((-0.424802, -0.285379, -0.859129), 146.654), (-27.1941, 55.2722, -6.01249), True), 1: (((0.713895, 0.0494788, -0.698503), 103.637), (13.8779, 45.3555, 10.0875), True), 2: (((-0.191902, -0.0638644, 0.979334), 50.2643), (-7.89693, 19.4431, 17.5053), True)}
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

