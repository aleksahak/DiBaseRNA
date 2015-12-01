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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwdOfYdxA1UJYmFsbFNjYWxlcQRLB0c/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLB4h9h3EHVQlwb2ludFNpemVxCEsHRz/wAAAAAAAAfYdxCVUEbmFtZXEKSwdVEEFVX2RpYWdvbl8xMy5wZGJ9cQsoVRBBVV9kaWFnb25fMjEucGRicQxdcQ1LAmFVEUFVX3BsYW5hcl8xNDMucGRicQ5dcQ9LBWFVEEFVX2RpYWdvbl82Mi5wZGJxEF1xEUsEYVURQVVfZGlhZ29uXzEwMC5wZGJxEl1xE0sAYVUQQVVfZGlhZ29uXzYxLnBkYnEUXXEVSwNhVRBBVV9wbGFuYXJfODIucGRicRZdcRdLBmF1h3EYVQ9hcm9tYXRpY0Rpc3BsYXlxGUsHiX2HcRpVBWNvbG9ycRtLB0sAfXEcKEsBXXEdSwFhSwJdcR5LAmFLA11xH0sDYUsEXXEgSwRhSwVdcSFLBWFLBl1xIksGYXWHcSNVCG9wdGlvbmFscSR9cSVVCG9wZW5lZEFzcSaISwcoVTovaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQVUvc3BhdGlhbC9BVV9kaWFnb25fMjEucGRiVQNQREJxJ06JdHEofXEpKChVOy9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9BVS9zcGF0aWFsL0FVX2RpYWdvbl8xMDAucGRiaCdOiXRxKl1xK0sAYShVOi9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9BVS9zcGF0aWFsL0FVX2RpYWdvbl8xMy5wZGJoJ06JdHEsXXEtSwFhKFU6L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FVL3NwYXRpYWwvQVVfcGxhbmFyXzgyLnBkYmgnTol0cS5dcS9LBmEoVTovaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvQVUvc3BhdGlhbC9BVV9kaWFnb25fNjEucGRiaCdOiXRxMF1xMUsDYShVOi9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9BVS9zcGF0aWFsL0FVX2RpYWdvbl82Mi5wZGJoJ06JdHEyXXEzSwRhKFU7L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL0FVL3NwYXRpYWwvQVVfcGxhbmFyXzE0My5wZGJoJ06JdHE0XXE1SwVhdYeGcTZzVQpwZGJIZWFkZXJzcTddcTgofXE5fXE6fXE7fXE8fXE9fXE+fXE/ZVUMYXJvbWF0aWNNb2RlcUBLB0sBfYdxQVUDaWRzcUJLB0sASwCGfXFDKEsDSwCGcURdcUVLA2FLBksAhnFGXXFHSwZhSwJLAIZxSF1xSUsCYUsFSwCGcUpdcUtLBWFLAUsAhnFMXXFNSwFhSwRLAIZxTl1xT0sEYXWHcVBVDnN1cmZhY2VPcGFjaXR5cVFLB0e/8AAAAAAAAH2HcVJVCWF1dG9jaGFpbnFTSweIfYdxVFUKdmR3RGVuc2l0eXFVSwdHQBQAAAAAAAB9h3FWVQ1hcm9tYXRpY0NvbG9ycVdLB059h3FYVQZoaWRkZW5xWUsHiX2HcVpVCWxpbmVXaWR0aHFbSwdHP/AAAAAAAAB9h3FcVQpzdGlja1NjYWxlcV1LB0c/8AAAAAAAAH2HcV5VB2Rpc3BsYXlxX0sHiH2HcWBVEGFyb21hdGljTGluZVR5cGVxYUsHSwJ9h3FidS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsOiX2HcQVVBG5hbWVxBksOVQFBfXEHVQFVXXEIKEsBSwNLBUsHSwlLC0sNZXOHcQlVBWNoYWlucQpLDlUBQX1xC1UBQk5dcQwoSwFLAYZxDUsDSwGGcQ5LBUsBhnEPSwdLAYZxEEsJSwGGcRFLC0sBhnESSw1LAYZxE2WGcRRzh3EVVQ5yaWJib25EcmF3TW9kZXEWSw5LAn2HcRdVAnNzcRhLDomJiYd9h3EZVQhtb2xlY3VsZXEaSw5LAH1xGyhLAU5dcRxLAksChnEdYYZxHksCTl1xH0sESwKGcSBhhnEhSwNOXXEiSwZLAoZxI2GGcSRLBE5dcSVLCEsChnEmYYZxJ0sFTl1xKEsKSwKGcSlhhnEqSwZOXXErSwxLAoZxLGGGcS11h3EuVQtyaWJib25Db2xvcnEvSw5OfYdxMFUFbGFiZWxxMUsOVQB9h3EyVQpsYWJlbENvbG9ycTNLDk59h3E0VQhmaWxsTW9kZXE1Sw5LAX2HcTZVBWlzSGV0cTdLDol9h3E4VQtsYWJlbE9mZnNldHE5Sw5OfYdxOlUIcG9zaXRpb25xO11xPChLAUsChnE9SwFLAoZxPksBSwKGcT9LAUsChnFASwFLAoZxQUsBSwKGcUJLAUsChnFDZVUNcmliYm9uRGlzcGxheXFESw6JfYdxRVUIb3B0aW9uYWxxRn1xR1UEc3NJZHFISw5K/////32HcUl1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLFksVZV1xBShLFksXZV1xBihLF0sYZV1xByhLGUsYZV1xCChLGUsaZV1xCShLGUsVZV1xCihLF0sbZV1xCyhLG0scZV1xDChLHUscZV1xDShLHkscZV1xDihLG0sfZV1xDyhLIEsfZV1xEChLIEshZV1xEShLIEsiZV1xEihLFksiZV1xEyhLI0sVZV1xFChLJUskZV1xFShLJkskZV1xFihLJksnZV1xFyhLKEsnZV1xGChLKEspZV1xGShLKEsqZV1xGihLKksrZV1xGyhLKkssZV1xHChLLEskZV1xHShLLEstZV1xHihLLksnZV1xHyhLJksvZV1xIChLMUswZV1xIShLMkswZV1xIihLMkszZV1xIyhLM0s0ZV1xJChLNEs1ZV1xJShLNks1ZV1xJihLN0s1ZV1xJyhLNEs4ZV1xKChLOUs4ZV1xKShLOUs6ZV1xKihLOUs7ZV1xKyhLMks7ZV1xLChLM0s8ZV1xLShLPUs8ZV1xLihLPUs+ZV1xLyhLPUswZV1xMChLQEs/ZV1xMShLQEtBZV1xMihLQktAZV1xMyhLQktDZV1xNChLREtCZV1xNShLREtFZV1xNihLRktFZV1xNyhLR0tFZV1xOChLR0s/ZV1xOShLR0tIZV1xOihLREtJZV1xOyhLSks/ZV1xPChLTEtLZV1xPShLTEtNZV1xPihLTEtOZV1xPyhLT0tOZV1xQChLT0tQZV1xQShLUEtRZV1xQihLUktRZV1xQyhLUktTZV1xRChLUktUZV1xRShLVUtUZV1xRihLVUtPZV1xRyhLVUtLZV1xSChLUEtWZV1xSShLV0tWZV1xSihLWEtWZV1xSyhLWUtLZV1xTChLW0taZV1xTShLXEtbZV1xTihLXEtdZV1xTyhLXktcZV1xUChLXktfZV1xUShLXktgZV1xUihLYUtgZV1xUyhLYktgZV1xVChLYktjZV1xVShLYktaZV1xVihLW0tkZV1xVyhLZUtaZV1xWChLZ0tmZV1xWShLZ0toZV1xWihLaEtpZV1xWyhLaktpZV1xXChLaktrZV1xXShLaktmZV1xXihLaEtsZV1xXyhLbEttZV1xYChLbkttZV1xYShLbktvZV1xYihLbktwZV1xYyhLZ0twZV1xZChLbEtxZV1xZShLcktxZV1xZihLc0txZV1xZyhLdEtmZV1xaChLdkt1ZV1xaShLd0t2ZV1xaihLeEt3ZV1xayhLeEt5ZV1xbChLekt5ZV1xbShLe0t5ZV1xbihLe0t1ZV1xbyhLe0t8ZV1xcChLeEt9ZV1xcShLd0t+ZV1xcihLdkt/ZV1xcyhLgEt1ZV1xdChLgkuBZV1xdShLg0uBZV1xdihLg0uEZV1xdyhLg0uFZV1xeChLhkuFZV1xeShLhkuHZV1xeihLh0uIZV1xeyhLiUuIZV1xfChLiUuKZV1xfShLiUuLZV1xfihLjEuLZV1xfyhLjEuBZV1xgChLjEuGZV1xgShLh0uNZV1xgihLjkuNZV1xgyhLj0uNZV1xhChLkUuQZV1xhShLkkuRZV1xhihLkkuTZV1xhyhLlEuSZV1xiChLlEuVZV1xiShLlEuWZV1xiihLl0uWZV1xiyhLmEuWZV1xjChLmEuQZV1xjShLmEuZZV1xjihLkUuaZV1xjyhLm0uQZV1xkChLnUucZV1xkShLnUueZV1xkihLnUufZV1xkyhLoEufZV1xlChLoUugZV1xlShLoUucZV1xlihLoUuiZV1xlyhLo0uiZV1xmChLo0ukZV1xmShLo0ulZV1xmihLpkulZV1xmyhLpkunZV1xnChLqEunZV1xnShLqUunZV1xnihLoEumZV1xnyhLqkucZV1xoChLrEurZV1xoShLrUurZV1xoihLrUuuZV1xoyhLr0utZV1xpChLsEuvZV1xpShLsEuxZV1xpihLskuxZV1xpyhLs0uxZV1xqChLs0urZV1xqShLs0u0ZV1xqihLsEu1ZV1xqyhLr0u2ZV1xrChLuEu3ZV1xrShLuEu5ZV1xrihLuku5ZV1xryhLuku7ZV1xsChLuku8ZV1xsShLvUu8ZV1xsihLvUu+ZV1xsyhLv0u+ZV1xtChLwEu+ZV1xtShLwUu9ZV1xtihLuEvBZV1xtyhLwUvCZV1xuChLw0vCZV1xuShLw0u3ZV1xuihLw0vEZV1xuyhLxUu3ZV1xvChLx0vGZV1xvShLx0vIZV1xvihLyUvHZV1xvyhLyUvKZV1xwChLy0vJZV1xwShLy0vMZV1xwihLy0vNZV1xwyhLzkvNZV1xxChLz0vNZV1xxShLz0vQZV1xxihLz0vGZV1xxyhL0UvGZWVVBWxhYmVscchLxFUAfYdxyVUGcmFkaXVzccpLxEc/yZmZoAAAAH2HcctVC2xhYmVsT2Zmc2V0ccxLxE59h3HNVQhkcmF3TW9kZXHOS8RLAX2Hcc9VCG9wdGlvbmFscdB9cdFVB2Rpc3BsYXlx0kvESwJ9h3HTdS4='))
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
	pbInfo = {'category': ['distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 10, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = {0: ('_openColor00', (1, 1, 1, 1)), 1: ('_openColor01', (1, 0, 1, 1)), 2: ('_openColor02', (0, 1, 1, 1)), 3: ('_openColor03', (1, 1, 0, 1)), 4: ('_openColor04', (1, 0, 0, 1)), 5: ('_openColor05', (0, 0, 1, 1)), 6: ('_openColor06', (0.67, 1, 0, 1)), 7: ('N', (0.188235, 0.313725, 0.972549, 1)), 8: ('H', (1, 1, 1, 1)), 9: ('O', (1, 0.0509804, 0.0509804, 1)), 10: ('yellow', (1, 1, 0, 1)), 11: ('white', (1, 1, 1, 1)), 12: ('green', (0, 1, 0, 1))}
	viewerInfo = {'cameraAttrs': {'center': (45.701, 2.6095, 18.0006), 'fieldOfView': 26.2751, 'nearFar': (28.1594, 8.62876), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 20.526}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 9.94545, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.673419}, 'viewerHL': 12, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 11}

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
	residueData = [(7, 'Chimera default', 'rounded', 'unknown'), (8, 'Chimera default', 'rounded', 'unknown'), (9, 'Chimera default', 'rounded', 'unknown'), (10, 'Chimera default', 'rounded', 'unknown'), (11, 'Chimera default', 'rounded', 'unknown'), (12, 'Chimera default', 'rounded', 'unknown'), (13, 'Chimera default', 'rounded', 'unknown'), (14, 'Chimera default', 'rounded', 'unknown'), (15, 'Chimera default', 'rounded', 'unknown'), (16, 'Chimera default', 'rounded', 'unknown'), (17, 'Chimera default', 'rounded', 'unknown'), (18, 'Chimera default', 'rounded', 'unknown'), (19, 'Chimera default', 'rounded', 'unknown'), (20, 'Chimera default', 'rounded', 'unknown')]
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
	xformMap = {0: (((-0.565187, -0.824945, 0.00546407), 105.832), (55.5454, -35.8788, -10.2962), True), 1: (((0.439269, 0.779737, -0.446154), 139.781), (19.3101, 31.4256, 52.7816), True), 2: (((-0.715632, 0.685264, 0.135218), 155.761), (49.655, 1.75006, 30.5115), True), 3: (((0.664454, 0.742792, 0.0822245), 157.548), (43.9273, -3.74304, 19.397), True), 4: (((0.0847182, -0.289163, -0.953524), 84.2003), (41.8812, 16.5441, 14.85), True), 5: (((-0.45982, -0.847181, -0.266174), 128.154), (65.6229, -9.8093, -1.00984), True), 6: (((0.656362, -0.75389, 0.0289744), 175.246), (60.523, -1.54767, 30.9618), True)}
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

