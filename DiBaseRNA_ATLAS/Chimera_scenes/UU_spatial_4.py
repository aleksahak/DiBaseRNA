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
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwROfYdxA1UJYmFsbFNjYWxlcQRLBEc/0AAAAAAAAH2HcQVVFHJpYmJvbkhpZGVzTWFpbmNoYWlucQZLBIh9h3EHVQlwb2ludFNpemVxCEsERz/wAAAAAAAAfYdxCVUEbmFtZXEKSwRVEFVVX2RpYWdvbl85MC5wZGJ9cQsoVRBVVV9kaWFnb25fOTIucGRicQxdcQ1LAmFVEFVVX2RpYWdvbl85MS5wZGJxDl1xD0sBYVUQVVVfZGlhZ29uXzkzLnBkYnEQXXERSwNhdYdxElUPYXJvbWF0aWNEaXNwbGF5cRNLBIl9h3EUVQVjb2xvcnEVSwRLAH1xFihLAV1xF0sBYUsCXXEYSwJhSwNdcRlLA2F1h3EaVQhvcHRpb25hbHEbfXEcVQhvcGVuZWRBc3EdiEsEKFU6L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL1VVL3NwYXRpYWwvVVVfZGlhZ29uXzkwLnBkYlUDUERCcR5OiXRxH31xICgoVTovaG9tZS9hbGV4L0Rlc2t0b3AvZGlCYXNlX2xpYkYvVVUvc3BhdGlhbC9VVV9kaWFnb25fOTEucGRiaB5OiXRxIV1xIksBYShVOi9ob21lL2FsZXgvRGVza3RvcC9kaUJhc2VfbGliRi9VVS9zcGF0aWFsL1VVX2RpYWdvbl85Mi5wZGJoHk6JdHEjXXEkSwJhKFU6L2hvbWUvYWxleC9EZXNrdG9wL2RpQmFzZV9saWJGL1VVL3NwYXRpYWwvVVVfZGlhZ29uXzkzLnBkYmgeTol0cSVdcSZLA2F1h4ZxJ3NVCnBkYkhlYWRlcnNxKF1xKSh9cSp9cSt9cSx9cS1lVQxhcm9tYXRpY01vZGVxLksESwF9h3EvVQNpZHNxMEsESwNLAIZ9cTEoSwJLAIZxMl1xM0sCYUsBSwCGcTRdcTVLAWFLAEsAhnE2XXE3SwBhdYdxOFUOc3VyZmFjZU9wYWNpdHlxOUsER7/wAAAAAAAAfYdxOlUJYXV0b2NoYWlucTtLBIh9h3E8VQp2ZHdEZW5zaXR5cT1LBEdAFAAAAAAAAH2HcT5VDWFyb21hdGljQ29sb3JxP0sETn2HcUBVBmhpZGRlbnFBSwSJfYdxQlUJbGluZVdpZHRocUNLBEc/8AAAAAAAAH2HcURVCnN0aWNrU2NhbGVxRUsERz/wAAAAAAAAfYdxRlUHZGlzcGxheXFHSwSIfYdxSFUQYXJvbWF0aWNMaW5lVHlwZXFJSwRLAn2HcUp1Lg=='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksIVQEgfYdxA1ULZmlsbERpc3BsYXlxBEsIiX2HcQVVBG5hbWVxBksIVQFVfYdxB1UFY2hhaW5xCEsIVQFBfXEJVQFCTl1xCihLAUsBhnELSwNLAYZxDEsFSwGGcQ1LB0sBhnEOZYZxD3OHcRBVDnJpYmJvbkRyYXdNb2RlcRFLCEsCfYdxElUCc3NxE0sIiYmJh32HcRRVCG1vbGVjdWxlcRVLCEsAfXEWKEsBTl1xF0sCSwKGcRhhhnEZSwJOXXEaSwRLAoZxG2GGcRxLA05dcR1LBksChnEeYYZxH3WHcSBVC3JpYmJvbkNvbG9ycSFLCE59h3EiVQVsYWJlbHEjSwhVAH2HcSRVCmxhYmVsQ29sb3JxJUsITn2HcSZVCGZpbGxNb2RlcSdLCEsBfYdxKFUFaXNIZXRxKUsIiX2HcSpVC2xhYmVsT2Zmc2V0cStLCE59h3EsVQhwb3NpdGlvbnEtXXEuKEsBSwKGcS9LAUsChnEwSwFLAoZxMUsBSwKGcTJlVQ1yaWJib25EaXNwbGF5cTNLCIl9h3E0VQhvcHRpb25hbHE1fXE2VQRzc0lkcTdLCEr/////fYdxOHUu'))
	atomInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQdyZXNpZHVlcQJLYEsEfXEDKEsFTl1xBEsMSwyGcQVhhnEGSwZOXXEHSxhLDIZxCGGGcQlLB05dcQpLJEsMhnELYYZxDEsITl1xDUswSwyGcQ5hhnEPSwlOXXEQSzxLDIZxEWGGcRJLCk5dcRNLSEsMhnEUYYZxFUsLTl1xFktUSwyGcRdhhnEYdYdxGVUIdmR3Q29sb3JxGktgTn2HcRtVBG5hbWVxHEtgVQJPNH1xHShVAkgzcR5dcR8oSwtLE0seSypLOEtFS1JLXWVVAkgxcSBdcSEoSwFLF0sjSy9LMUs9S0lLX2VVAkg2cSJdcSMoSwpLFksaSy5LO0s/S1BLW2VVAkg1cSRdcSUoSwhLFUsiSydLNEtBS05LWWVVAkM2cSZdcScoSwlLDUsZSyVLMks+S09LWmVVAkMycShdcSkoSwJLEUsfSytLOUtGS0pLVWVVAk4xcSpdcSsoSwBLDEsYSyRLMEs8S0hLVGVVAk4zcSxdcS0oSwRLEEsdSylLN0tES0tLVmVVAk8ycS5dcS8oSwNLEksgSyxLOktHS1NLXmVVAkM1cTBdcTEoSwdLDksbSyZLM0tAS01LWGVVAkM0cTJdcTMoSwVLD0scSyhLNUtCS0xLV2V1h3E0VQN2ZHdxNUtgiX2HcTZVDnN1cmZhY2VEaXNwbGF5cTdLYIl9h3E4VQVjb2xvcnE5S2BOfXE6KEsEXXE7KEsASwRLDEsQSxhLHUskSylLMEs3SzxLREtIS0tLVEtWZUsFXXE8KEsBSwhLCksLSxNLFUsWSxdLGkseSyJLI0snSypLLksvSzFLNEs4SztLPUs/S0FLRUtJS05LUEtSS1lLW0tdS19lSwZdcT0oSwNLBksSSxRLIEshSyxLLUs2SzpLQ0tHS1FLU0tcS15ldYdxPlUJaWRhdG1UeXBlcT9LYIl9h3FAVQZhbHRMb2NxQUtgVQB9h3FCVQVsYWJlbHFDS2BVAH2HcURVDnN1cmZhY2VPcGFjaXR5cUVLYEe/8AAAAAAAAH2HcUZVB2VsZW1lbnRxR0tgSwF9cUgoSwhdcUkoSwNLBksSSxRLIEshSyxLLUs2SzpLQ0tHS1FLU0tcS15lSwZdcUooSwJLBUsHSwlLDUsOSw9LEUsZSxtLHEsfSyVLJksoSytLMkszSzVLOUs+S0BLQktGS0pLTEtNS09LVUtXS1hLWmVLB11xSyhLAEsESwxLEEsYSx1LJEspSzBLN0s8S0RLSEtLS1RLVmV1h3FMVQpsYWJlbENvbG9ycU1LYE59h3FOVQxzdXJmYWNlQ29sb3JxT0tgTn2HcVBVBnJhZGl1c3FRS2BHP/AAAAAAAAB9cVIoRz/6AAAAAAAAXXFTKEsASwRLDEsQSxhLHUskSylLMEs3SzxLREtIS0tLVEtWZUc/964UgAAAAF1xVChLA0sGSxJLFEsgSyFLLEstSzZLOktDS0dLUUtTS1xLXmVHP/szM0AAAABdcVUoSwJLBUsHSwlLDUsOSw9LEUsZSxtLHEsfSyVLJksoSytLMkszSzVLOUs+S0BLQktGS0pLTEtNS09LVUtXS1hLWmV1h3FWVQtsYWJlbE9mZnNldHFXS2BOfYdxWFUPc3VyZmFjZUNhdGVnb3J5cVlLYFUEbWFpbn2HcVpVCGRyYXdNb2RlcVtLYEsCfYdxXFUIb3B0aW9uYWxxXX1xXihVB2JmYWN0b3JxX4hLYEcAAAAAAAAAAH2HhnFgVQlvY2N1cGFuY3lxYYhLYEcAAAAAAAAAAH2HhnFidVUHZGlzcGxheXFjS2CIfXFkiU5dcWUoSwhLAYZxZksKSwGGcWdLFUsChnFoSxpLAYZxaUsiSwGGcWpLJ0sBhnFrSy5LAYZxbEs0SwGGcW1LO0sBhnFuSz9LAYZxb0tBSwGGcXBLTksBhnFxS1BLAYZxcktZSwGGcXNLW0sBhnF0ZYZxdXOHcXZ1Lg=='))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVhdG9tc3ECXXEDKF1xBChLDUsMZV1xBShLDksMZV1xBihLDksPZV1xByhLDksQZV1xCChLEUsQZV1xCShLEUsSZV1xCihLEUsTZV1xCyhLE0sUZV1xDChLE0sVZV1xDShLFUsMZV1xDihLFUsWZV1xDyhLF0sQZV1xEChLGUsYZV1xEShLGksZZV1xEihLG0saZV1xEyhLG0scZV1xFChLHUscZV1xFShLHUseZV1xFihLHUsYZV1xFyhLH0scZV1xGChLG0sgZV1xGShLGkshZV1xGihLGUsiZV1xGyhLI0sYZV1xHChLJUskZV1xHShLJUsmZV1xHihLJ0slZV1xHyhLKEsnZV1xIChLKEspZV1xIShLKkspZV1xIihLK0spZV1xIyhLK0skZV1xJChLK0ssZV1xJShLKEstZV1xJihLJ0suZV1xJyhLL0skZV1xKChLMUswZV1xKShLMksxZV1xKihLMkszZV1xKyhLNEsyZV1xLChLNEs1ZV1xLShLNks1ZV1xLihLN0s1ZV1xLyhLN0swZV1xMChLN0s4ZV1xMShLNEs5ZV1xMihLMUs6ZV1xMyhLO0swZV1xNChLPUs8ZV1xNShLPks8ZV1xNihLP0s+ZV1xNyhLP0tAZV1xOChLQUs/ZV1xOShLQUtCZV1xOihLQUtDZV1xOyhLREtDZV1xPChLRUtDZV1xPShLRUs8ZV1xPihLRUtGZV1xPyhLPktHZV1xQChLSUtIZV1xQShLSktIZV1xQihLSktLZV1xQyhLTEtKZV1xRChLTEtNZV1xRShLTktMZV1xRihLTktPZV1xRyhLTktQZV1xSChLUUtQZV1xSShLUktQZV1xSihLUktIZV1xSyhLUktTZV1xTChLVUtUZV1xTShLVktUZV1xTihLVktXZV1xTyhLWEtXZV1xUChLWEtZZV1xUShLWUtaZV1xUihLWUtbZV1xUyhLW0tcZV1xVChLW0tUZV1xVShLWEtdZV1xVihLXktXZV1xVyhLVktfZV1xWChLYUtgZV1xWShLYUtiZV1xWihLY0tiZV1xWyhLY0tkZV1xXChLZEtlZV1xXShLZEtmZV1xXihLZktgZV1xXyhLZktnZV1xYChLY0toZV1xYShLaUtiZV1xYihLYUtqZV1xYyhLa0tgZWVVBWxhYmVscWRLYFUAfYdxZVUGcmFkaXVzcWZLYEc/yZmZoAAAAH2HcWdVC2xhYmVsT2Zmc2V0cWhLYE59h3FpVQhkcmF3TW9kZXFqS2BLAX2HcWtVCG9wdGlvbmFscWx9cW1VB2Rpc3BsYXlxbktgSwJ9h3FvdS4='))
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
	viewerInfo = {'cameraAttrs': {'center': (21.0985, 28.453, 11.1709), 'fieldOfView': 26.2751, 'nearFar': (19.2646, 3.07721), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 12.581}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'viewSize': 9.84938, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 1, 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.552622}, 'viewerHL': 9, 'cameraMode': 'mono', 'detail': 1, 'viewerFog': None, 'viewerBG': 8}

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
	xformMap = {0: (((-0.75223, -0.635314, -0.17472), 102.033), (-5.19995, 0.912702, 13.3858), True), 1: (((0.44182, 0.503066, 0.742778), 164.14), (28.0685, 41.8142, -17.1341), True), 2: (((0.872789, -0.0817886, -0.481197), 120.939), (-1.5362, 38.2246, -5.90384), True), 3: (((0.804312, -0.504367, -0.31416), 142.58), (38.3804, 59.5414, -0.33396), True)}
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

